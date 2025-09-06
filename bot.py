import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
token = os.getenv("BOT_TOKEN")

description= ""
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.command()

async def hi(ctx):
    await ctx.send("hi")


bot.run(token)