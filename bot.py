import discord
import os
from dotenv import load_dotenv
from api import api_request

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
url = "https://hoge/data"

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("ログインしました")


@client.event
async def on_message(message):
    if message.author.bot:
        return

    await message.channel.send("メッセージが書き込まれました")

    flag = False

    if flag:
        response = api_request(url)
        print(response)


client.run(DISCORD_TOKEN)
