import discord
from discord import Message

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message: Message):
    if message.author == client.user:
            return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    elif message.content.startswith('$brat'):
        await message.channel.send(f"BRAT MOJ {message.author}")

client.run('TOKEN')


