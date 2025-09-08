import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import mangaClass
import random 

load_dotenv()
token = os.getenv("BOT_TOKEN")

description= ""
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.command()
async def recommend(ctx,*args):
    name = " ".join(args[:])
    manga = mangaClass.Manga(name)
    manga.getMangaData()
    await ctx.send(manga.mangaDesc())

@bot.command()
async def random(ctx):
    manga = mangaClass.Manga("")
    manga.mangaRandom()
    await ctx.send(manga.mangaDesc())


bot.run(token)
