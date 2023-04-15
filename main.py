import discord
from discord import app_commands
from reactionmenu import ViewMenu, ViewButton
from EpicGames.api_call import API_Call
import secret

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

@tree.command(name = 'freegames', description='Free Games on the Epic Games store!')
async def self(interaction: discord.Interaction):
    game_list = API_Call.callEpicAPI()[0]
    embed_list = []

    for item in game_list:
        embed=discord.Embed(title=f'**{item.title}**', description=item.desc, color=0xee0f14)
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
    game_list = API_Call.callEpicAPI()[1]
    embed_list = []

    for item in game_list:
        embed=discord.Embed(title=item.title, description=item.desc, color=0xee0f14)
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

client.run(secret.BOT_TOKEN)