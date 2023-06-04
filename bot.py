import discord
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

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


client.run(DISCORD_TOKEN)
