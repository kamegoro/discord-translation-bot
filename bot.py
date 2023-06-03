import discord
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()


@client.event
async def on_ready():
    print("ログインしました")


@client.event
async def on_message(message):
    if message.author.bot:
        return

    await message.channel.send("メッセージが書き込まれました")


client.run(DISCORD_TOKEN)
