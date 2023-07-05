import requests
import os
import discord
from dotenv import load_dotenv

load_dotenv()

DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
TRANSLATION_BOT_ID = os.getenv("TRANSLATION_BOT_ID")
url = "https://api-free.deepl.com/v2/translate"

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("ログインしました")


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if not message.mentions:
        return

    for mention in message.mentions:
        if mention.id == int(TRANSLATION_BOT_ID):

            def make_api_request():
                data = {
                    "text": message.content,
                    "target_lang": "JA",
                    "auth_key": DEEPL_API_KEY,
                }

                response = requests.post(url, data=data)
                print(response)
                if response.status_code == 200:
                    json = response.json()
                    return json["translations"][0]["text"]
                else:
                    return None

            await message.channel.send(make_api_request())


client.run(DISCORD_TOKEN)
