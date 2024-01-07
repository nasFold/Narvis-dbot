# main.py
import discord
from discord.ext import commands
from narvis_helper import NarvisHelper

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

DISCORD_BOT_TOKEN = 'MTE5MzQ5OTczMzA4ODU0Njg5Nw.GW7PCA.ne3rT5oSMnkZfCDPQCU_z3wMpaCpYgM-OzhpnY'

bot = commands.Bot(command_prefix='/', intents=intents)

narvis_helper = NarvisHelper()  # Menggunakan nilai default dari file config.py

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('/'):
        command = message.content[1:].split(' ')[0].lower()
        if command in narvis_helper.responses:
            response = narvis_helper.responses[command](message.content[len(command) + 2:])
            await message.channel.send(response)
    await bot.process_commands(message)

@bot.command(name='narvishelp', help='Show help message')
async def show_help(ctx):
    help_message = "Available Commands:\n"
    for command in narvis_helper.responses.keys():
        help_message += f"- {command}\n"
    await ctx.send(help_message)

bot.run(DISCORD_BOT_TOKEN)
