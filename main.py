import discord
import os
from keep_alive import keep_alive


client = discord.Client()

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='my Masters'))
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('ayy'):
    await message.channel.send('lmao')

keep_alive()
client.run(os.environ['TOKEN']) 
