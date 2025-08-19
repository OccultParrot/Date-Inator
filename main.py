import os

import discord
from discord import app_commands, Client
from dotenv import load_dotenv
from rich.console import Console

load_dotenv()

console = Console()


class DateInatorClient(Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

        try:
            self.__GUILD_ID = discord.Object(id=os.getenv("GUILD_ID"))
        except TypeError:
            print("GUILD_ID not in environment variables")
            exit(1)

    async def setup_hook(self) -> None:
        self.tree.copy_global_to(guild=self.__GUILD_ID)
        await self.tree.sync(guild=self.__GUILD_ID)


client = DateInatorClient()


@client.event
async def on_ready():
    console.line(2)
    console.rule(title=f'Logged in as [green]{client.user}[/] | [blue](ID: {client.user.id})[/]')


@client.tree.command(name="set-season", description="Sets the current season")
@app_commands.describe(season="The season you want to set")
async def set_season(interaction: discord.Interaction, season: int):
    pass


@client.tree.context_menu(name="Test Context Command")
async def test_context_menu(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message("Hello World")


@client.tree.command(name="set-year", description="Sets the current year")
async def set_year(interaction: discord.Interaction):
    pass


@client.tree.command(name="step-season", description="Steps to the next season")
async def step_season(interaction: discord.Interaction):
    pass


@client.tree.command(name="set-season-interval", description="Sets the amount of days between each season")
async def set_season_interval(interaction: discord.Interaction):
    pass


client.run(os.getenv('DISCORD_BOT_TOKEN'))
