# bot.py
import os
import discord
from dotenv import load_dotenv
import random
import requests
from requests import get
import json

load_dotenv()
GUILD = os.getenv('DISCORD_GUILD')


client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hey {member.name}, don\'t you think you have done a fault in joining this channel?'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    hi = [
        'I\'m not of your age that you\'ll say me hello!!',
        'I don\'t talk with pigs!\n',
        (
            'Don\'t disturb me!'
            'I am not your friend!!'
        ),
    ]

    if message.content == 'Hello One Eye':
        response = random.choice(hi)
        await message.channel.send(response)

    helpc = [
        'Want help huh puppy?\n',
        'Why don\'t you clearly tell you want to see my commands?!\n',
    ]

    if message.content == 'Help me One Eye':
        embed=discord.Embed(title="You need some help in knowing me", description="The following bold words are the codes and their descriptions are given below. I you have a basic understanding, you will know it. Else get out of the server!!", color=0x017cda)
        embed.add_field(name="Hello One Eye", value="To hear a VERY VERY GOOD response!", inline=False)
        embed.add_field(name="Help me One Eye  ", value="Typing this will show you what you are reading!", inline=False)
        embed.add_field(name="Who are you?    ", value="If you want to know who the hell I am then you must type this.", inline=False)
        embed.add_field(name="Tell me some news", value="To see some half-true...half-false news", inline=False)
        embed.add_field(name="Show me some memes", value=" To see some real memes.", inline=False)
        embed.add_field(name="How are you?", value="If you\'re dying to know how I am, then you must type this.", inline=False)
        embed.set_footer(text="Want to know more? just type the commands in the server.")
        await message.channel.send(random.choice(helpc))
        await message.channel.send(embed=embed)

    if message.content == 'Who are you?':
        await message.channel.send('I am the one whom you see everyday in front of the mirror!')

    news = [
        f'{client.user.name} may be dead in one hour\n',
        'Ultron can come here and extract Vibranium in any moment\n',
        'The sky would be filled with pigs anytime between 6.0.0 a.m to 6.0.1 a.m\n',
        'People may turn to zombies tonight\n',
        f'Mozang stated that {client.user.name}\'s Minecraft account may be banned permanantly.\n',
        'some Discord accounts are now potential target for hackers\n',
    ]
    newstype=[
        'Do you really think this are good news?\n',
        'News always tells truth.\n',
        'Read the news carefully, who knows, maybe the news is about you...',
    ]

    if message.content == 'Tell me some news':
        response = random.choice(newstype)+'\n'+random.choice(news)
        await message.channel.send(response)

    if message.content == 'Show me some memes':
        content = get("https://meme-api.herokuapp.com/gimme").text
        data = json.loads(content,)
        meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
        await message.channel.send("MEMEY.....MEMEY.....MEMEY......\n")
        await message.channel.send(embed=meme)

    health=[
        'After she left me,, I am just depressed...\n',
        'I\'m feelin\' much better than you!!\n',
        'How dare you tellin\' me this!!!',
    ]
    if message.content == 'How are you?':
        await message.channel.send(random.choice(health))

    if message.content == 'Roast':
        roast=(ctx.message.author.mention())+random.choice(roastword)
        await message.channel.send(roast)

    if message.content == 'Introduce yourself':
        await message.channel.send("Hello   Hello   Hello!!!!\nI know you don\'t know me!!\n I don\'t think so\nSo as you have Invited me to your server, you have to make me your most beloved guest, or else...\nBYTHEWAY I AM ONE EYE, A BOT YOU HAVE NEVER THOUGHT OF!!")



client.run('ODgwNDgzNDk4NzMxOTAxMDAw.YSe8KA.moKfBhaWh6nKu4FZ2Vm7_aim0Tk')