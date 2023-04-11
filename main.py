import discord
from discord import app_commands
from EpicGames.database import Database
from reactionmenu import ViewMenu, ViewButton

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
            await self.wait_until_ready()
            if not self.synced:
                await tree.sync(guild = discord.Object(id = 1093910311523852390))
                self.synced = True
            print(f'We have logged in as {self.user}.')

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(guild = discord.Object(id=1093910311523852390), name = 'tester', description='testing')
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong!')

@tree.command(guild = discord.Object(id=1093910311523852390), name = 'freegames', description='Free Games on the Epic Games store!')
async def self(interaction: discord.Interaction):
    game_list = Database.retrieveActive()
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

@tree.command(guild = discord.Object(id=1093910311523852390), name = 'upcomingfreegames', description='Upcoming Free Games on the Epic Games Store!')
async def self(interaction: discord.Interaction):
    game_list = Database.retrieveUpcoming()
    embed_list = []

    for item in game_list:
        embed=discord.Embed(title=item.title, description=item.desc, color=0xee0f14)
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

client.run(open("token.txt","r").readline().strip())