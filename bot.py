# bot.py
import os
import discord
from discord.ext import bot
from discord.ext import commands
from dotenv import load_dotenv
import random
import requests
from requests import get
import json
import asyncio
import datetime 
from discord_slash import SlashCommand, SlashContext
import pyjokes

load_dotenv()



client = discord.Client()

def get_quote():
  response = requests.get ("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def todaydate():
    current_time = datetime.datetime.now() 
    month=current_time.month
    day=current_time.day
    print("Date: ",str(day),"/",str(month))

def checkbirth():
    current_time = datetime.datetime.now() 
    birthday='26/ 8'
    month=current_time.month
    day=current_time.day
    todaydate=(str(day)+"/"+str(month))
    print("Birthday: "+str(birthday))
    if birthday==todaydate:
        print("Birthday today!!\nAge: "+str((int(today.strftime("%Y"))-2021)))

print("Author: Captain Tiger.")
checkbirth()
todaydate()
print("Connecting with  the bot...")

@client.event
async def on_ready():
    print(f'{client.user.name} has been connected to the following servers,\n')
    activeservers = client.guilds
    for guild in activeservers:
        print(guild.name)

    print("/```````````````````````EXCEPTIONS AND HISTORY```````````````````````\\")
    await client.change_presence(activity=discord.Game('Forza Horizon 4'))



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


    if message.content.startswith(""):
            if client.user.mentioned_in(message):
                k=str(message.author)
                myid = k
                tst=message.author
                string=str(tst)
                total=str(string[0:-5])
                print("mentioned by ",total)
                mentioning=["Stop mentioning me you fool!!", 'Why are you mentioning me @'+total+"?", "This is my last warning to you, stop mentioning me "+total, "Stop mentioning me and try visiting my blog\nhttps://oneeyebot.blogspot.com/"]
                await message.channel.send(random.choice(mentioning))

    if message.content.startswith(""):
        k=str(message.author)
        myid = k
        tst=message.author
        string=str(tst)
        total=str(string[0:-5])    
        if total=="MoshPoT":
            textformosh=["I agree with "+total,
            "Hey "+total+", try to write somethin\' new in your code.",
            ]
            await message.channel.send(random.choice(textformosh))

        if total=="Philosopher":
            textforphil=["I agree with "+total,
            "Hey "+total+", try to write somethin\' new in your code.",
            ]
            await message.channel.send(random.choice(textforphil))

        if total=="SOLFLARE":
            textforsol=["I agree with "+total,
            "Hey "+total+", try to write somethin\' new in your code.",
            ]
            await message.channel.send(random.choice(textforsol))



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
            embed.add_field(name="Roast <anyone>", value="This is my favorite. I wont say anythin\' \'bout it.", inline=False)
            embed.add_field(name="Show me quote of the minute.", value="If you are a little literate, you should type this.", inline=False)
            embed.add_field(name="Crack a joke", value="Type to hear jokes", inline=False)
            embed.add_field(name="Show infection status", value="Wan\'t to know how many servers I have infected??", inline=False)
            embed.add_field(name="Share One Eye", value="Type this and copy everything I reply and share with everyone. That\'s my order!!", inline=False)
            embed.add_field(name="Show One Eye\'s Blog", value="Type to see my infected blog", inline=False)           
            embed.set_footer(text="Want to know more? just type the commands in the server.")
            await message.channel.send(random.choice(helpc))
            await message.channel.send(embed=embed)

        if message.content == 'Who are you?':
            await message.channel.send('I am the one whom you see everyday in front of the mirror!')


        if message.content == 'Tell me some news':
            k=str(message.author)
            myid = k
            tst=message.author
            string=str(tst)
            total=str(string[0:-5])
            news = [
            (total+' may be dead in one hour\n'),
            'Ultron can come here and extract Vibranium in any moment\n',
            'The sky would be filled with pigs anytime between 6.0.0 a.m to 6.0.1 a.m\n',
            'People may turn to zombies tonight\n',
            ('Mojang stated that '+total+'\'s Minecraft account may be banned permanently.\n'),
            'some Discord accounts are now potential target for hackers\n',
            'Peoples are not advised to go outside today because meteorologists have detected that there would be rain of eggs. \n',
            ]
            newstype=[
            'Do you really think this are good news?\n',
            'News always tells truth.\n',
            'Read the news carefully, who knows, maybe the news is about you...',
            ]
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
            await message.channel.send("You Idiot! don\'t you know you have to mention a user!!")

        if message.content == 'Introduce yourself':
            await message.channel.send("Hello   Hello   Hello!!!!\nI know you don\'t know me!!\n I don\'t think so\nSo as you have Invited me to your server, you have to make me your most beloved guest, or else...\nBYTHEWAY I AM ONE EYE, A BOT YOU HAVE NEVER THOUGHT OF!!")

        n=0
        if message.content == 'I vote for One Eye':
            await message.channel.send("Thanks for voting me! By the way, I don\'t even need your votes!!")
            n=n+1

        vot=str(n)

        if message.content == 'How much vote you got?':
            vote='OMG!! I forgot! wait, wait, wait!!! Oh yes, I got '+vot+' votes.'
            await message.channel.send(vote)

        if message.content== 'test':
            k=str(message.author)
            myid = k
            tst=message.author
            string=str(tst)
            total=str(string[0:-5])
            await message.channel.send(total)

        if message.content == 'Share One Eye':
            share='If you want to spread the disease of roasting and insulting, share this link with everyone.\nhttps://discord.com/api/oauth2/authorize?client_id=880483498731901000&permissions=0&scope=bot\n:D :D :D'
            await message.channel.send(share)



        if message.content.startswith('Rhoaast '):
            text=str(message)
            print(text)
            word='roast '
            wordlist = text.split()
            if word in wordlist:
                text = text.replace(str(word), "")
                print("\nNew String without \"" +word+ "\":")
                print(text)
            roast=''
            await message.channel.send(text)

        if message.content.startswith('Roast '):
            roast=[
            "You should be lucky as mirrors can't talk, or else they would laugh at you.",
            "Someday you have to go far and I hope you are stayin\' there",
            "You don't deserve to use this command!",
            "I think you have born on a highway, because it\'s where most accidents happens.",
            "Did you asked your parents that from where you have born?",
            "If laughter is the best medicine, your face must be curing the world",
            "Is your ass jealous because of the large amount of shit coming from your mouth?",
            "You don\'t deserve to get roasted!!",
            "Did you ate the garbage I left for you piggy?",
            "Your life is a shit and you are the undigested fish of it.",
            "I must admit I have foolish friends, but not as foolish as you.",
            "Don\'t think people love you because you are attractive. People love you because they love dogs.",
            "Think about someone special...and think about him\\her dumping you...",
            "Whenever I see your face, I change nothing but only the direction I was walking in.",
            "People like you are the cause of hatred.",
            "First wash your dirty hands before typing anythin\'",
            "If you know the reason why people hate you, then you wouldn\'t be alive till now.",
            ]
            roastword=random.choice(roast)
            await message.channel.send(roastword)

        if message.content==('Roaast'):
            k=str(message.author)
            myid = k
            tst=message.author
            string=str(tst)
            total=str(string[0:-5])
            roast=['',
            ]
            roastfinal=""
            await message.channel.send()
            

        if message.content == 'Show infection status':
            status="Till now, i have infected "+str(len(client.guilds))+" servers!!\nSpread the disease more,\nClick on https://discord.com/api/oauth2/authorize?client_id=880483498731901000&permissions=0&scope=bot"
            await message.channel.send(status)

        if message.content == 'Hey One Eye! ,hows goin brother...?':
            k=str(message.author)
            myid = k
            tst=message.author
            string=str(tst)
            total=str(string[0:-5])
            status=total+" you shut up!!"
            await message.channel.send(status) 

        if message.content == 'Show me quote of the minute.':
            quote = "Today\' quote of the minute is,\n\n"+get_quote()
            await message.channel.send(quote)

        if message.content == 'Show me Infectious victims':
            activeservers = client.guilds
            await message.channel.send("I have infected the following servers:")
            for guild in activeservers:
                await message.channel.send(guild.name)

        if message.content == 'Show One Eye\'s Blog':
            blog='You have to visit my Blog.\nhttps://oneeyebot.blogspot.com/'
            await message.channel.send(blog)

        if message.content == 'Crack a joke':
            joke='Let\'s crack it!!\n\n'+pyjokes.get_joke(language="en", category="all")
            await message.channel.send(joke)



@commands.is_owner() 
async def broadcast(ctx, message):     
    for guild in client.guilds:
        # get the owner of guild
        owner = guild.owner

        # check if dm exists, if not create it
        if owner.dm_channel is None:
            await owner.create_dm()
      
        # if creation of dm successful
        if owner.dm_channel != None:
            await owner.dm_channel.send(message)
   
        for channel in guild.channels:             
            if(channel.name == 'Don\' you think you have done a fault in joining me in your channel?'):                 
                await channel.send(message)


client.run('ODgwNDgzNDk4NzMxOTAxMDAw.YSe8KA.moKfBhaWh6nKu4FZ2Vm7_aim0Tk')