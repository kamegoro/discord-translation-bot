import os
import discord
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
TRANSLATION_BOT_ID = os.getenv("TRANSLATION_BOT_ID")

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("ログインしました")


@client.event
async def on_message(message):
    if not message.mentions:
        return

    for mention in message.mentions:
        if mention.id == int(TRANSLATION_BOT_ID):
            await message.channel.send("翻訳botにメンションしました")


client.run(DISCORD_TOKEN)
