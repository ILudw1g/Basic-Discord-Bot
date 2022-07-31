# Basic-Discord-Bot
Basic, self-hosting, Discord Bot via https://replit.com and https://uptimerobot.com.

# Prerequisites
Use Replit "Secrets" to hide your bot's Token (since Replit is public).

# Basic Template
Has status to Listening and a simple text return.

```
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
```
# Keep Alive
```
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
```

# Add weblink to uptimerobot
Set ping interval to 5 or 15 minutes (Replit shuts off after an hour of inactivity).

# Bot Status Templates
Listening: 

```
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='my Masters'), status=discord.Status.online)
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
```

Streaming:
```
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='with my Masters', url='[Twitch/Stream URL]'))
    
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
```
Watching:
```
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='The Boys'))
    
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
```
