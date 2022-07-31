import discord
import os
from keep_alive import keep_alive


client = discord.Client()

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='my Masters'), status=discord.Status.online)
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!!help'):
    await message.channel.send('As per my Masters\' commands, I am merely able to respond to the following!\n\nHELP\n!!help (or <#493910443463671818>, though not always up to date)```\n\n\nMISCELLANEOUS\ngoteem\nreverse\ndelet\nkys\nshrg\n!simp\ndonowall\nsimp\nsnipermonkey\n\nQUOTES\n.\na\nayy\ncri\nkms\ntasty\nloli\nsed\ntraps\ng1\n420\nnword\n69\nau\nadiltime\n!doc\n!val\n!remind\n!na\n!kira\n!listen\n!m1911a1\n!csgo\n!insane\n\nSTFUs\nshnen\nbrahim\nabss\nziad\nkif\nfan\n\nEMOTES\na!\nezclap```')

  if message.content.startswith('ayy'):
    await message.channel.send('lmao')

  if message.content.startswith('cri') and len(message.content) <=3:
    await message.channel.send('don\'t lose hope. you exist in the same world lolis do.')

  if message.content.startswith('goteem'):
    await message.channel.send('https://media.tenor.com/images/9ddea6899165d002b3a0e77185698599/tenor.gif')
  
  if message.content.startswith('kms'):
    await message.channel.send('ye do it')

  if message.content.startswith('tasty'):
    await message.channel.send('hmm, tastes like loli')
  
  if message.content.startswith('loli'):
    await message.channel.send('I\'m a simple man. When I see a loli, I- I\'m ready to go to jail.. ( ͡° ͜ʖ ͡°)')

  if message.content.startswith('sed'):
    await message.channel.send('lyf = sed; nwtns 9th law.')

  if message.content.startswith('tellmemore'):
    await message.channel.send('https://i.imgur.com/vUXbEx0h.jpg')

  if message.content.startswith('traps'):
    await message.channel.send('traps are gay only as much as you want them to be ( ͡° ͜ʖ ͡°)')

  if message.content.startswith('.') and len(message.content) <= 1:
    await message.channel.send('ᵏ')

  if message.content.startswith('reverse'):
    await message.channel.send('https://i.postimg.cc/7YPBWTJ0/bCYyRNGh.jpg')

  if message.content.startswith('g1'):
    await message.channel.send('yo thats a good one.')

  if message.content.startswith('delet') and len(message.content) <= 5:
    await message.channel.send('https://i.imgur.com/cApJ7Jf.png')

  if message.content.startswith('kys') or message.content.startswith('KYS'):
    await message.channel.send('https://i.imgur.com/VZEgsXk.jpg')

  if message.content.startswith('shrg'):
    await message.channel.send('https://media.tenor.com/images/6def41cfbfc28b3be8c20be9d6ef2dde/tenor.gif')

  if message.content.startswith('a') and len(message.content) <= 1:
    await message.channel.send('aaaaaaaaa')

  if message.content.startswith('420'):
    await message.channel.send('blaze it, fgt')

  if message.content.startswith('nword'):
    await message.channel.send('nice')

  if message.content.startswith('69'):
    await message.channel.send('nice')
  
  if message.content.startswith('au') and len(message.content) <= 2:
    await message.channel.send('Hi, this is a message informing you that the individual named "Akif" is unavailable at this moment. \nPlease try again later!')

  if message.content.startswith('!doc'):
    await message.channel.send('Let\'s talk about about me. Let\'s talk about the 6 8 frame, the 37 inch vertical leap, the black steel that drips down my back AKA the bullet proof mullet, the google prototype scopes with built in LCD LED 1080p 3D Sony technology. The Ethiopian poisonous caterpillar aka SLICK DADDY. let\'s talk about the cabinets right behind me that go 40ft deep into the wall that house the other 95% of my trophies, the awards, the certificates, all claiming first place, right? Let me give you a little inside glimpse into the hotshot video gaming lifestyle of the two-time international video gaming superstar. Because that\'s what this channel\'s about, that\'s what this domain\'s about, that\'s what this society is about. You\'re looking at the face of Twitch and God-damn. \n \nTwitch is lucky.')

  if message.content.startswith('!val'):
    await message.channel.send('valarante child game.... look to cartoon grapfix to make kid player happy like children show.. valarante cartoon world with rainbow unlike counter strike with dark corridorr and raelistic gun.. valarante like playhouse. valarant playor run from csgo fear of dark world and realism')

  if message.content.startswith('shnen'):
    await message.channel.send('https://i.imgur.com/EbgC2BS.png')

  if message.content.startswith('brahim'):
    await message.channel.send('https://i.imgur.com/vFTr3dh.png')

  if message.content.startswith('abss') and len(message.content) <=4:
    await message.channel.send('https://i.imgur.com/7pn6Rl7.png')

  if message.content.startswith('ziad'):
    await message.channel.send('https://i.imgur.com/UrOjMCh.png')

  if message.content.startswith('kif') and len(message.content) <=3:
    await message.channel.send('https://i.imgur.com/QQpoeMw.png')

  if message.content.startswith('fan') and len(message.content) <=3:
    await message.channel.send('https://i.imgur.com/nR9qorq.png')

  if message.content.startswith('!remind'):
    await message.channel.send('<@417955065018581003>, as per Masters\' command; I hereby remind you to watch One Piece!')

  if message.content.startswith('!simp'):
    await message.channel.send('https://tenor.com/view/simp-gif-18073694')

  if message.content.startswith('!na'):
    await message.channel.send('NA “Near Airport” is known as the fastest region to arrive at the Airport. In particular they are the current world record holders in Airport Any %.')

  if message.content.startswith('!kira'):
    await message.channel.send('My name is..... ***Sigh***\n\nMy name is Yoshikage Kira. I\'m 33 years old. My house is in the northeast section of Morioh, where all the villas are, and I am not married. I work as an employee for the Kame Yu department stores, and I get home every day by 8 PM at the latest. I don\'t smoke, but I occasionally drink. I\'m in bed by 11 PM, and make sure I get eight hours of sleep, no matter what. After having a glass of warm milk and doing about twenty minutes of stretches before going to bed, I usually have no problems sleeping until morning. Just like a baby, I wake up without any fatigue or stress in the morning. I was told there were no issues at my last check-up. I\'m trying to explain that I\'m a person who wishes to live a very quiet life. I take care not to trouble myself with any enemies, like winning and losing, that would cause me to lose sleep at night. That is how I deal with society, and I know that is what brings me happiness. Although, if I were to fight I wouldn\'t lose to anyone.')

  if message.content.startswith('!listen'):
    await message.channel.send('u guys need to listen 👂 to whats being said 🗣️')

  if message.content.startswith('a!'):
    await message.channel.send('<:ree02:663350363600060467>')

  if message.content.startswith('donowall'):
    await message.channel.send('https://tenor.com/view/dono-wall-talking-wall-bricks-gif-17741481')

  if message.content.startswith('adiltime'):
    await message.channel.send('Imagine Adil giving a time <:topkek:662796808673820745>')

  if message.content.startswith('!m1911a1'):
    await message.channel.send('The feeding ramp is polished to a mirror sheen. The slide\'s been reinforced. And the interlock with the frame is tightened for added precision. The sight system is original, too. The thumb safety is extended to make it easier on the finger. A long-type trigger with non-slip grooves. A ring hammer... The base of the trigger guard\'s been filed down for a higher grip. And not only that, nearly every part of this gun has been expertly crafted and customized.\n\nWhere\'d you get something like this?')
  
  if message.content.startswith('simp'):
    await message.channel.send('https://cdn.discordapp.com/attachments/899754498610847764/910312135060516884/sniper_monkey.mp4')

  if message.content.startswith('sniper monkey'):
    await message.channel.send('https://i.imgur.com/2vY7JqY.png')

  if message.content.startswith('ezclap'):
    await message.channel.send('<:EZ:891812903836065803> <a:Clap:919429091600515072>')

  if message.content.startswith('!csgo'):
    await message.channel.send('best game')

  if message.content.startswith('!insane'):
    await message.channel.send('he skilled player but that is not normally, This very very insane....They need to check him pc and game.....Maybe he not cheating but maybe he using the game deficit ...and this cant seem on game screen..He needs to check-up....')

keep_alive()
client.run(os.environ['TOKEN'])