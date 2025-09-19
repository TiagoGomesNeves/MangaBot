import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import mangaClass
import pymongo

load_dotenv()
token = os.getenv("BOT_TOKEN")
connection = os.getenv("DB_CONNECTION")
myclient = pymongo.MongoClient(connection)
mydb = myclient["discord"]
db = mydb["users"]


description= ""
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.command()
async def profile(ctx):
    user = ctx.message.author.mention
    if (not haveAccount(user)):
       db.insert_one({"account": user,"list": ["", "", "", "", ""]})
       await ctx.send("Account Created")
    else:
        list = listToString(user)
        await ctx.send(list)

def haveAccount(user):
    query = db.find({"account": user})
    for doc in query:
        print("")
    return (query.retrieved == 1)

def listToString(user):
    list = ""
    query2 = db.find({"account": user}, {"_id": 0, "list": 1})
    for doc in query2:
        for i in range(0,5):
            list = list + str(i+1) + ". "+ doc["list"][i] + "\n"
    return list

@bot.command()
async def setListAt(ctx, num, *args):
    try:
        num = int(num)
        if (num < 1 or num > 5):
            await ctx.send("Please ensure the first argument is a number 1-5")
            return
    except ValueError:
        await ctx.send("Please ensure the first argument is a number 1-5")
        return
    num = num - 1
    name = " ".join(args[:])
    user = ctx.message.author.mention
    if (not haveAccount(user)):
        await ctx.send("Create an Account first")
    
    query = db.find({"account": user}, {"_id": 0, "list": 1})
    for doc in query:
        list = doc["list"]
    list[num] = name

    db.update_one({"account": user}, {"$set": {"list": list}})
    newList = listToString(user)
    await ctx.send(newList)


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

@bot.command()
async def commands(ctx):
    message = "?Profile : this command if not used before generates a profile for the user and stores it on a database. The next ?profile commands will show that users top 5 list.\n?setListAt number mangaName : this allows users to alter their top 5 list by choosing a mangaName and a position on the list to place it in\n?random: this generates a random number which corresponds to a myanimelist id and uses an api to retrive that manga's information\n?recommend mangaName: this uses the mangaName and an api to grab information about that manga like its name, author, genres, and synopsis"
    await ctx.send(message)

bot.run(token)
