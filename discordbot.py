import os
import discord
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("ログインしました")


@client.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    channel = reaction.message.channel
    await channel.send(f"{user.name}さんがリアクションしました")


client.run(DISCORD_TOKEN)
