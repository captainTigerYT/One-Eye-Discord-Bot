#2021 Raunak Manna 

# bot.py
import keep_alive
import os
import discord
from dotenv import load_dotenv
import random
import json
#import asyncio
import requests
from requests import get
import datetime 
#from discord_slash import SlashCommand, SlashContext
import pyjokes
import sys
import time
#from hangman import Hangman
#import helpembed
#import youtube_dl
#import pyrandmeme

load_dotenv()

#version
botversion="1.4.1"


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

print(sys.version)
print('\n')
print("Author: Captain Tiger.")
checkbirth()
todaydate()
print("Connecting with  the bot...")

pfp_path = 'icon.JPG'

fp = open(pfp_path, 'rb')
pfp = fp.read()

@client.event
async def on_ready():
    await client.user.edit(avatar=pfp)
    print(f'{client.user.name} has been connected to '+str(len(client.guilds))+' servers,\n')
    print("\n/```````````````````````EXCEPTIONS AND HISTORY```````````````````````\\")
    #await client.change_presence(activity=discord.Game('Forza Horizon 4'))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=''+str(len(client.guilds))+' servers!!'))



@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hey {member.name}, don\'t you think you have done a fault in joining this channel?'
    )

@client.event
async def on_message(message):
    online = False
    try:

      if message.author == client.user:
          return

      
      if online == False:
        message.channel.send(":expressionless: :expressionless: Back Online :expressionless: :expressionless: ")
        online = True


        #if message.content.startswith(""):
                #if client.user.mentioned_in(message):
                    #k=str(message.author)
                    #myid = k
                    #tst=message.author
                    #string=str(tst)
                    #total=str(string[0:-5])
                    #print("mentioned by ",total)
                    #mentioning=["Stop mentioning me you fool!!", 'Why are you mentioning me @'+total+"?", "This is my last warning to you, stop mentioning me "+total, "Stop mentioning me and try visiting my blog\nhttps://oneeyebot.blogspot.com/"]
                    #await message.channel.send(random.choice(mentioning))

        #if message.content.startswith(""):
      k=str(message.author)
      myid = k
      tst=message.author
      string=str(tst)
      total=str(string[0:-5])    
          
        


      hi = ['I\'m not of your age that you\'ll say me hello!!',
                'I don\'t talk with pigs!\n',
                (
                    'Don\'t disturb me!'
                    'I am not your friend!!'
                ),
            ]

            #test for exception
      if message.content == 'faf':
            print(faf)

      if message.content == 'Hello One Eye':
                response = random.choice(hi)
                await message.channel.send(response)

      helpc = [
                'Want help huh puppy?\n',
                'Why don\'t you clearly tell you want to see my commands?!\n',
            ]

      if message.content == 'Help me One Eye':
                embed=discord.Embed(title="You need some help in knowing me", description="The following bold words are the codes and their descriptions are given below. I you have a basic understanding, you will know it. Else get out of the server!!", color=0x026424)
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
                embed.add_field(name="Hack <anyone>", value="Type to Hack anybody!!", inline=False) 
                embed.add_field(name="Laugh at <anyone>", value="Type to laugh at the idiotic face of anyone!!", inline=False) 
                embed.add_field(name="Penis size of <anyone>", value="Type to see the length of anyone\'s pennis!!", inline=False)
                embed.add_field(name="Gay rate of <anyone>", value="Type to see the gayness of anybody!!", inline=False) 
                embed.add_field(name="Kill <anyone>", value="Type to Kill anyone instantly!!", inline=False) 
                embed.add_field(name="Educate <anyone>", value="Type to Educate all the fools here!!", inline=False) 
                embed.add_field(name="Humour of <anyone>", value="Type to start the world-famous humor-o-meter", inline=False)
                embed.add_field(name="Horoscope of <anyone>", value="Type to see anyone\'s horoscope withi seconds.", inline=False)
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
                #content = get("https://www.reddit.com/r/dankmemes/new.json?sort=hot").text
                data = json.loads(content,)
                meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
                await message.channel.send("MEMEY.....MEMEY.....MEMEY......\n")
                await message.channel.send(embed=meme)
                #await message.channel.send(embed=await pyrandmeme())

      health=[
                'After she left me, I am just depressed...\n',
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
                share='If you want to spread the disease of roasting and insulting, share this link with everyone.\nhttps://oneeyebot.blogspot.com\n:laughing:  :laughing:  :laughing: '
                await message.channel.send(share)

      if message.content.startswith('Roast '):
                victim = message.content.replace('Roast',"").strip()
                roast=[
                victim+" should be lucky as mirrors can't talk, or else they would laugh at him.",
                "Someday "+victim+" have to go far and I hope he are stayin\' there",
                "I think "+victim+" have born on a highway, because it\'s where most accidents happens.",
                "Did you asked your parents "+victim+" that from where you have born?",
                "If laughter is the best medicine, "+victim+"\'s face must be curing the world",
                "Is your ass jealous "+victim+" because of the large amount of shit coming from your mouth?",
                victim+" don\'t deserve to get roasted!!",
                "Did "+victim+" ate the garbage I left for him?",
                victim+"\'s life is a shit and he is the undigested fish of it.",
                "I must admit I have foolish friends, but not as foolish as "+victim+".",
                "Please don\'t think people love you "+victim+" because you are attractive. People love you because they love dogs.",
                "Think about someone special...and think about him\\her dumping "+victim+"...",
                "Whenever I see "+victim+"\' face, I change nothing but only the direction I was walking in.",
                "People like "+victim+" are the cause of hatred.",
                "First wash your dirty hands before typing anythin\' "+victim,
                "If "+victim+" knows the reason why people hate him, then he wouldn\'t be alive till now.",
                ]
                roastword=random.choice(roast)
                await message.channel.send(roastword)

      if message.content == 'Show infection status':
                status="Till now, i have infected "+str(len(client.guilds))+" servers!!\nSpread the disease more,\nClick on https://oneeyebot.blogspot.com"
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
                joke='Let\'s crack it!!\n\n'+pyjokes.get_joke(language="en", category="neutral")
                await message.channel.send(joke+"\n:laughing: :laughing: :laughing: ")


      if message.content.lower().find("lol") != -1:
                await message.channel.send("Yeah LOL!! :sweat_smile: ")

      if message.content.startswith('Laugh at '):
                if message.content != 'Laugh at':
                    victim = message.content.replace('Laugh at',"").strip()
                    laughlink=[
                    'https://tenor.com/view/john-jonah-jameson-lol-laughing-hysterically-laughing-out-loud-funny-gif-17710543',
                    'https://tenor.com/view/ryan-gosling-laugh-laughing-lol-giggle-gif-4925536',
                    'https://tenor.com/view/laugh-cant-hold-it-in-nicolas-cage-thinking-gif-5547928',
                    'https://tenor.com/view/saturday-baby-laugh-giggle-gif-12859194',
                    'https://tenor.com/view/spit-take-laughing-lmao-gif-9271317',
                    'https://tenor.com/view/emilia-clarke-laughing-happy-pretty-laughing-hysterically-gif-16328308',
                    ]
                    laughword="I realy can\'t help but laughing at "+victim
                    await message.channel.send(laughword)
                    await message.channel.send(random.choice(laughlink))

                else:
                    await message.channel.send("You are not giving any name in the arguments, so let me think that you mean that I will laugh at you. Your face is so toxic that even I can\'t laugh at you.\n:smirk:   ")

      email=[
            'bigbadboy101@gmail.com',
            'iamidiot.always@gmail.com',
            'mycodenameis420@gmail.com',
            'dontseethis2@gmail.com',
            'blahblahblah@gmail.com',
            'thedoomschool@tds.edu'
            'iknowiwasgointobehacked@dankmemer.lol'
            ]
      password=[
            'youcantstopme',
            'mo*+er_fu\'*er',
            'me_irl',
            'irealyloveher...',
            'goin\'upanddown',
            'shut_up_fool!!',
            'groin',
            'Ihatedankmemer'
            ]


      if message.content.startswith('Hack '):
                if message.content != 'Hack':
                    victim = message.content.replace('Hack',"").strip()
                    await message.channel.send("Hacking "+victim+'...')
                    time.sleep(2)
                    await message.channel.send("Gathering data") 
                    time.sleep(2)
                    await message.channel.send("Gathering Email ID(This may take a while)...") 
                    time.sleep(3)
                    eid=random.choice(email)
                    await message.channel.send("Email ID: `"+eid+"`") 
                    time.sleep(2)
                    await message.channel.send("Gathering password(This may take a minute)...") 
                    time.sleep(4)
                    passo=random.choice(password)
                    await message.channel.send("Password: `"+passo+"`") 
                    time.sleep(3)
                    embed=discord.Embed(title="Haking result: Success", description="Email and password of "+victim+" is succesfully leaked!!", color=0x026424)
                    embed.add_field(name="Email ID: ", value=eid, inline=False)
                    embed.add_field(name="Password: ", value=passo, inline=False)
                    embed.set_footer(text="If you get caught, then don\'t say my name!!")
                    await message.channel.send(embed=embed)

                else:
                    await message.channel.send("You are not giving any name in the arguments, so let me think that you mean that I will hack you. Well! I don\' hack babies!!\n:smirk:   ")

      if message.content.startswith('Penis size of '):
                if message.content != 'Penis size of':
                    victim = message.content.replace('Penis size of',"").strip()
                    r=random.randint(0,15)
                    s='8'
                    for x in range(r):
                        s=s+'='
                    s=s+'>'
                    embed=discord.Embed(title="Penis size: "+s, description="", color=0x026424)
                    text=''
                    if r<=5:
                        text='no better than a kid!!'
                    if r>5 and r<10:
                        text='normal, and need to exersise a bit!!'
                    if r>=10:
                        text='epic!!'
                    
                    omg =(victim+" is "+text)
                    #embed.set_footer(text)
                    await message.channel.send(embed=embed)
                    await message.channel.send(omg)

                else:
                    await message.channel.send("You are not giving any name in the arguments, so let me think that you mean that I will measure your penis. Well! first grow that a little...it is not measurable!!\n:smirk:   ")

      if message.content.startswith('Gay rate of '):
                if message.content != 'Gay rate of':
                    victim = message.content.replace('Gay rate of',"").strip()
                    r=random.randint(0,100)
                    embed=discord.Embed(title="GAY-o-METER", description="\n"+victim+" is "+str(r)+"% Gay", color=0x026424)
                    await message.channel.send(embed=embed)

                else:
                    await message.channel.send("You are not giving any name in the arguments, so let me think that you mean to measure the gay rate of yourself. You are 100 % gay then!!\n:smirk:   ")

      if message.content=='Laugh at':
                await message.channel.send("You are not giving any name in the arguments, so let me think that you mean that I will laugh at you. Your face is so toxic that even I can\'t laugh at you.\n:smirk:   ")

      if message.content=='Hack':
                await message.channel.send("You are not giving any name in the arguments, so let me think that you mean that I will hack you. Well! I don\' hack babies!!\n:smirk:   ")

      if message.content=='Penis size of':
                await message.channel.send("You are not giving any name in the arguments, so let me think that you mean that I will measure your penis. Well! first grow that a little...it is not measurable!!\n:smirk:   ")  

      if message.content=='Gay rate of':
                await message.channel.send('You are not giving any name in the arguments, so let me think that you mean to measure the gay rate of yourself. You are 100 % gay then!!\n:smirk:   "')

      if message.content=='test':
                text =message.content
                await message.channel.send(text)

      if message.content.startswith('test'):
                text = message.content.replace('test', "")
                await message.channel.send(text)

      if message.content.startswith('Kill'):
                try:
                    if message.content != 'Kill':
                        victim = message.content.replace('Kill',"").strip()
                        killed=[
                            (victim+' died due to chocking condoms during swimming.'),
                            (victim+' died due to eating the death cap mushroom.'),
                            ('There was a big clash between two groups of people and innocent '+victim+' got killed.'),
                            (victim+' died due to drinking stagnant water gathered in an old pot.'),
                            (victim+' died just like that.'),
                            (victim+' died when he was in a party and drank a full butt of Aakonian Ale'),
                            ('I told '+victim+' not to go towards the Elephant Grave, but he did. Now he is no more...')
                        ]
                        omgkilled=random.choice(killed)
                        embed=discord.Embed(title=("RIP :sob: :sob: :sob: "), description=omgkilled, color=0x026424)
                        await message.channel.send(embed=embed)

                    else:
                        await message.channel.send("I think idiots like you don\'t know that they have to mention a user!!")
                except:
                    await message.channel.send("I think idiots like you don\'t know that they have to mention a user!!")

      if message.content.startswith('Educate '):
              victim = message.content.replace('Educate',"").strip()
              eduwords=[
                  'You know '+victim+' that 1+2 is equal to 3??',
                  'What '+victim+'? you don\'t know the alphabets?',
                  'Yes you are right, I have to educate '+victim+'.',
                  'come on '+victim+' You have to learn the alphabets.'
                ]
              embed=discord.Embed(title='Ah...Education!!', description=random.choice(eduwords),color=0x026424)
              await message.channel.send(embed=embed)

      if message.content=='Educate':
                await message.channel.send("You are not giving any name in the arguments, so let me think that you mean that I will Educate you. But how can I educate turtles?\n:smirk:   ")

      if message.content.startswith('Humour of '):
              victim = message.content.replace('Humour of',"").strip()
              r=random.randint(0,100)
              embed=discord.Embed(title=':thinking: :thinking: Are you humorous?:thinking: :thinking: ', description=victim+" is "+str(r)+"% humorous.",color=0x026424)
              await message.channel.send(embed=embed)

      if message.content=='Humour of':
                await message.channel.send("You are not giving any name in the arguments, so let me think that you mean that I will check humour of you. But first you have to be humorous. Then only I can check you!!\n:smirk:   ")

      if message.content.startswith('Horoscope of '):
              victim = message.content.replace('Horoscope of',"").strip()
              todo=[
                'Try to walk more on gutters',
                'Try to slap your loved ones',
                'Try to eat Death Cap mushroom',
                'Try to fast for a month',
                'Try to roast your teachers in front of public',
                'Try to spend the mont roaming around naked',
                'Try to curse every strangers you meet everyday'        
                ]
              nottodo=[
                'Try not to tlak with your life partner(if any)',
                'Try not to eat food for a month',
                'Do not masterbet for six year',
                'Try to avoid walking in roads',
                'Try not to use digital devices.'
              ]
              td = random.choice(todo)
              ntd = random.choice(nottodo)
              embed=discord.Embed(title="HORROR-SCOPE", description="\"That's how I see "+victim+"'s future...\"", color = 0x026424)
              embed.add_field(name="To do", value=td, inline=False)
              embed.add_field(name="Not to do", value=ntd, inline=False)
              embed.set_footer(text="T&C APPLY\nWhat I say may be or may not be true...")
              await message.channel.send(embed = embed)

      if message.content == "Horoscope of":
              await message.channel.send("I realy want to, but if you don\'t put any name, how can I IDIOT?")



            #FakeSlash commands
      if message.content == '/credits':
                embed=discord.Embed(title="Credits", description="All these peoples have helped in creation of the bot.", color=0x026424)
                embed.set_author(name="One Eye Bot", url="https://oneeyebot.blogspot.com/")
                embed.add_field(name="Creator", value="Captain Tiger", inline=False)
                embed.add_field(name="Helping websites", value="stackoverflow.com, codegrepper.com, pypi.org", inline=False)
                embed.add_field(name="Writen on", value="Python Language", inline=False)
                embed.add_field(name="Helpers", value="DAGGER", inline=False)
                embed.set_footer(text="This feature is still on beta")
                await message.channel.send(embed=embed)

      if message.content == '/version':
                await message.channel.send(botversion)

      if message.content == '/FakeSlash help':
                embed=discord.Embed(title="FakeSlash© Commands", description="This are not slash commands.", color=0x026424)
                embed.set_author(name="One Eye Bot", url="https://oneeyebot.blogspot.com/")
                embed.add_field(name="/FakeSlash help", value="Shows help box", inline=False)
                embed.add_field(name="/credits", value="Shows credits.", inline=False)
                embed.add_field(name="/version", value="Shows version of the bot.", inline=False)
                embed.add_field(name="/FakeSlash", value="Shows information about FakeSlash©.", inline=False)
                embed.add_field(name="/Python Version", value="Shows in which Python the bot is running.", inline=False)
                embed.add_field(name="/Tutorial", value="Shows tutorial for the bot.", inline=False)
                embed.add_field(name="/License", value="Shows license for the bot.", inline=False)
                embed.set_footer(text="This feature is still on beta")
                await message.channel.send(embed=embed)

      if message.content == '/FakeSlash':
                fakeslash="Welcome to FakeSlash© help center.\nFakeSlash© is a new feature (beta) for One Eye which enables users to read generic informations of the bot.\nIf you want to know more, type '/FakeSlash help'."
                embed=discord.Embed(title="FakeSlash©", description=fakeslash, color=0x026424)
                embed.set_footer(text="This feature is still on beta")
                await message.channel.send(embed=embed)

      if message.content == '/Python Version':
                version=str(sys.version)
                finver='One Eye Bot is created with Python '+version
                await message.channel.send(finver)

      if message.content == '/Tutorial':
                await message.channel.send(file=discord.File('/Tutorial.txt'))

      if message.content == '/License':
                await message.channel.send(file=discord.File('License.txt'))

            #Easter eggs
      if message.content == '//':
                await message.channel.send('There are no Easter eggs here.')

      if message.content == 'Tell me some true news':
                await message.channel.send('You can never find a Easter egg!!')


    except Exception as e: 
        print('An Error/Exception occurred when user typed '+ message.content)
        exceptionembed=discord.Embed(title="Woah:tired_face:  Somethinng bad happened!!", description="This ex-ception is more disturbing than my 7th ex-wife.\nTry again after this exception is fixed, else send screen shot of this to my email: ", color=0x026424)
        exceptionembed.add_field(name="One Eye HelpDesk", value="oneeyehelp@gmail.com", inline=False)
        await message.channel.send(embed=exceptionembed)
        print(e)
        #await message.channel.send(message.content)


keep_alive.keep_alive()
try:
  my_secret = os.environ['TOKEN']
  client.run(my_secret)
except Exception as e:
  print(e)
