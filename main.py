import discord
from discord import app_commands
from reactionmenu import ViewMenu, ViewButton
from EpicGames.api_call import Epic_API_Call
from Steam.api_call import Steam_API_Call
import secret
import random

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f'We have logged in as {self.user}.')

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = 'ping', description='Simple Ping Command!')
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong! Command took {round(client.latency, 4)}s round trip!')

@tree.command(name = 'pet', description='Pet the pup!')
async def self(interaction: discord.Interaction):
    pet_response_list = ['Ruff!', 'Arf!!', 'Woof!', 'Bark!', 'Beep Boop Arf!']

    await interaction.response.send_message(random.choice(pet_response_list))

@tree.command(name = 'freegames', description='Free Games on the Epic Games store!')
async def self(interaction: discord.Interaction):
    game_list = Epic_API_Call.callEpicAPI()[0]
    embed_list = []

    for item in game_list:
        embed=discord.Embed(title=f'**{item.title}**', description=item.desc, color=0x8d1212)
        embed.set_author(name="Epic Store")
        embed.add_field(name='Original Price', value=f'~~{item.price}~~', inline=False)
        embed.add_field(name='Start Time', value=f'<t:{item.startTime}>', inline=True)
        embed.add_field(name='End Time', value=f'<t:{item.endTime}>', inline=True)
        embed.set_image(url=item.image_url)
        embed_list.append(embed)

    menu = ViewMenu(interaction, menu_type=ViewMenu.TypeEmbed)
    for item in embed_list:
        menu.add_page(item)

    menu.add_button(ViewButton.back())
    menu.add_button(ViewButton.next())

    await menu.start()

@tree.command(name = 'upcomingfreegames', description='Upcoming Free Games on the Epic Games Store!')
async def self(interaction: discord.Interaction):
    game_list = Epic_API_Call.callEpicAPI()[1]
    embed_list = []

    for item in game_list:
        embed=discord.Embed(title=item.title, description=item.desc, color=0x8d1212)
        embed.set_author(name="Epic Store")
        embed.add_field(name='Original Price', value=f'~~{item.price}~~', inline=False)
        embed.add_field(name='Start Time', value=f'<t:{item.startTime}>', inline=True)
        embed.add_field(name='End Time', value=f'<t:{item.endTime}>', inline=True)
        embed.set_image(url=item.image_url)
        embed_list.append(embed)

    menu = ViewMenu(interaction, menu_type=ViewMenu.TypeEmbed)
    for item in embed_list:
        menu.add_page(item)

    menu.add_button(ViewButton.back())
    menu.add_button(ViewButton.next())

    await menu.start()


@tree.command(name = 'steamspecials', description='Specials & Sales on the Steam Store!')
async def self(interaction: discord.Interaction):
    game_list = Steam_API_Call.callSteamAPI()
    embed_list = []

    for item in game_list:
        embed=discord.Embed(title=item.title, color=0x0000a0, url=item.store_link)
        embed.set_author(name="Steam Store")
        embed.add_field(name='Original Price', value=f'~~{item.original_price}~~', inline=True)
        embed.add_field(name='Sale Price', value=item.sale_price, inline=True)
        embed.add_field(name='Offer Ends', value=f'<t:{item.end_time}>', inline=True)
        embed.set_image(url=item.header_image)
        embed_list.append(embed)

    menu = ViewMenu(interaction, menu_type=ViewMenu.TypeEmbed)
    for item in embed_list:
        menu.add_page(item)

    menu.add_button(ViewButton.back())
    menu.add_button(ViewButton.next())

    await menu.start()

client.run(secret.BOT_TOKEN)