import time

import discord

from stock import Stock

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
TOKEN = ""
PREFIX = '!'


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    print(message.content)
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith("!stock tsla"):
        await message.channel.send(Stock("tsla"))

    if "!ping" in message.content:
        test = message.content.split()

        userid = test[1]
        pings = test[2]

        for i in range(int(pings)):
            await message.channel.send(userid + " get on lethal company");
            time.sleep(1)


client.run(TOKEN)
