# Local Code Imports
from EpicGames.api_call import Epic_API_Call
from Steam.api_call import Steam_API_Call
import secret
import version

# Outside Packages
from discord import app_commands
from reactionmenu import ViewMenu, ViewButton
import discord
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

# Simple command to show the round trip time for a command, helps with debugging.
@tree.command(name = 'ping', description='Simple Ping Command!')
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong! Command took {round(client.latency, 4)}s round trip!')

# Fun command for petting Pupperino! It selects a response from a premade list.
@tree.command(name = 'pet', description='Pet the pup!')
async def self(interaction: discord.Interaction):
    pet_response_list = ['Ruff!', 'Arf!!', 'Woof!', 'Bark!', 'Beep Boop Arf!']

    await interaction.response.send_message(random.choice(pet_response_list))

# Calls an API hosted by Epic Games, to show information about free games on the Epic Store.
@tree.command(name = 'epicfree', description='Free Games on the Epic Games Store!')
async def self(interaction: discord.Interaction):
    # Calls the Epic api and organizes them into two different lists, one for the current free games, and one for the upcoming ones.
    game_list_current = Epic_API_Call.callEpicAPI()[0]
    game_list_upcoming = Epic_API_Call.callEpicAPI()[1]
    embed_list = []

    # These loops define the embed objects that are then sent to the reactionmenu functions that display them.
    for item in game_list_current:
        embed=discord.Embed(title=f'**{item.title}**', description=item.desc, color=0x8d1212)
        embed.set_author(name="Epic Store")
        embed.add_field(name='Original Price:', value=f'~~{item.price}~~', inline=False)
        embed.add_field(name='Start Time:', value=f'<t:{item.startTime}>', inline=True)
        embed.add_field(name='End Time:', value=f'<t:{item.endTime}>', inline=True)
        embed.add_field(name='Status:', value=f'{item.status}', inline=True)
        embed.set_image(url=item.image_url)
        embed_list.append(embed)

    for item in game_list_upcoming:
        embed=discord.Embed(title=f'**{item.title}**', description=item.desc, color=0x8d1212)
        embed.set_author(name="Epic Store")
        embed.add_field(name='Original Price:', value=f'~~{item.price}~~', inline=False)
        embed.add_field(name='Start Time:', value=f'<t:{item.startTime}>', inline=True)
        embed.add_field(name='End Time:', value=f'<t:{item.endTime}>', inline=True)
        embed.add_field(name='Status:', value=f'{item.status}', inline=True)
        embed.set_image(url=item.image_url)
        embed_list.append(embed)

    # Adds all the embeds into the created menu so that they can be displayed.
    menu = ViewMenu(interaction, menu_type=ViewMenu.TypeEmbed)
    for item in embed_list:
        menu.add_page(item)

    menu.add_button(ViewButton.back())
    menu.add_button(ViewButton.next())

    await menu.start()

# Calls an API hosted by Steam, to show information about specials and sales on the Steam store.
@tree.command(name = 'steamspecials', description='Specials & Sales on the Steam Store!')
async def self(interaction: discord.Interaction):
    # Creates a list of all the specials the Steam store is currently running.
    game_list = Steam_API_Call.callSteamAPI()
    embed_list = []

    # Creates the embeds based on the data returned by the API
    for item in game_list:
        embed=discord.Embed(title=item.title, color=0x0000a0, url=item.store_link)
        embed.set_author(name="Steam Store")
        embed.add_field(name='Original Price', value=f'~~{item.original_price}~~', inline=True)
        embed.add_field(name='Sale Price', value=item.sale_price, inline=True)
        embed.add_field(name='Offer Ends', value=f'<t:{item.end_time}>', inline=True)
        embed.set_image(url=item.header_image)
        embed_list.append(embed)

    # Adds all the embeds into the created menu so that they can be displayed.
    menu = ViewMenu(interaction, menu_type=ViewMenu.TypeEmbed)
    for item in embed_list:
        menu.add_page(item)

    menu.add_button(ViewButton.back())
    menu.add_button(ViewButton.next())

    await menu.start()

@tree.command(name = 'about', description='Find out more about Pupperino!')
async def self(interaction: discord.Interaction):
    embed = discord.Embed(title=f'Pupperino {version.VERSION}', description=f'Arf! I am currently serving {len(client.guilds)} Discord servers!\n\nThank you for using Pupperino!', colour=0xffffa6)
    embed.set_thumbnail(url="https://i.imgur.com/WtWKT0K.jpg")
    embed.set_footer(text="Created by CinderGN#0001")
    await interaction.response.send_message(embed=embed)

client.run(secret.BOT_TOKEN)