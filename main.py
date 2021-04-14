VERSION = 1.0
AUTHORS = ['xq#1001']

## Disclaimer ##
# please do not copy off of this, if you do atleast give me credit and/or ask me on discord at xq#1001, if thats invalid check my github bio || thanks and enjoy the project

import discord
import json
import ctypes
import requests
import pyfiglet
import webbrowser

from discord.ext import commands
from discord import client
from discord.errors import LoginFailure
from colored import fg

ctypes.windll.kernel32.SetConsoleTitleW(f'Author xq#1001 | Version {VERSION} | XERL SELFBOT')

with open('config.json') as Data:
    config = json.load(Data)

token = config.get("token")
prefix = config.get("prefix")

client = commands.Bot(description="XERL SELFBOT", command_prefix=prefix,self_bot=True)
client.remove_command('help')
user = discord.Client()

red = fg('1')
blue = fg('51')
white = fg('15')

Err = f'{white}[{red}ERR{white}]'
Xerl = f'{white}[{blue}X{white}ER{red}L{white}]'

print(f'''
        {blue}                     █████ █████    ██████████    ███████████      █████      
                            ░░███ ░░███    ░░███░░░░░█   ░░███░░░░░███    ░░███       
                             ░░███ ███      ░███  █ ░     ░███    ░███     ░███       
        {white}                      ░░█████       ░██████       ░██████████      ░███       
                               ███░███      ░███░░█       ░███░░░░░███     ░███       
        {red}                      ███ ░░███     ░███ ░   █    ░███    ░███     ░███      █
                             █████ █████    ██████████    █████   █████    ███████████
                            ░░░░░ ░░░░░    ░░░░░░░░░░    ░░░░░   ░░░░░    ░░░░░░░░░░░ 
''')

@client.event
async def on_ready():
    print(f'                                                {white}User: {blue}{client.user.name}{white}#{red}{client.user.discriminator}')
    print(f'                                                {white}ID: {red}{client.user.id}')

@client.command()
async def ascii(ctx):
    await ctx.message.delete()

    args = input(f'     {Xerl} Text To Render In Ascii > ')
    result = pyfiglet.figlet_format(args)

    await ctx.send(f'```{result}```')

@client.command()
async def anime(ctx):
    await ctx.message.delete()
    webbrowser.open("https://www.nekos.fun/apidoc.html")
    print(f'   {Xerl} Opened Up The Link In Your Browser, Scroll Down For Tags.')
    
    raw = input(f'   {Xerl} Tag > ').lower()
    tag = raw.lower()

    url = requests.get(f'http://api.nekos.fun:8080/api/{tag}')
    data = url.json()

    image = data['image']

    if tag == "kiss":
        user = int(input(f'   {Xerl} ID Of The User You Want To Kiss > '))
        print("\n")
        name = await client.fetch_user(user)
        emb = discord.Embed(title=f'{client.user.name}#{client.user.discriminator} Kissed {name}')
        emb.set_image(url=image)
        emb.set_footer(text="https://www.nekos.fun/apidoc.html")

    elif tag == "lick":
        user = int(input(f'   {Xerl} ID Of The User You Want To Lick > '))
        print("\n")
        name = await client.fetch_user(user)
        emb = discord.Embed(title=f'{client.user.name}#{client.user.discriminator} Licked {name}')
        emb.set_image(url=image)
        emb.set_footer(text="https://www.nekos.fun/apidoc.html")

    elif tag == "hug":
        user = int(input(f'   {Xerl} ID Of The User You Want To Hug > '))
        print("\n")
        name = await client.fetch_user(user)
        emb = discord.Embed(title=f'{client.user.name}#{client.user.discriminator} Hugged {name}')
        emb.set_image(url=image)
        emb.set_footer(text="https://www.nekos.fun/apidoc.html")

    elif tag == "slap":
        user = int(input(f'   {Xerl} ID Of The User You Want To Slap > '))
        print("\n")
        name = await client.fetch_user(user)
        emb = discord.Embed(title=f'{client.user.name}#{client.user.discriminator} Slapped {name}')
        emb.set_image(url=image)
        emb.set_footer(text="https://www.nekos.fun/apidoc.html")

    elif tag == "slap":
        user = int(input(f'   {Xerl} ID Of The User You Want To Slap > '))
        print("\n")
        name = await client.fetch_user(user)
        emb = discord.Embed(title=f'{client.user.name}#{client.user.discriminator} Slapped {name}')
        emb.set_image(url=image)
        emb.set_footer(text="https://www.nekos.fun/apidoc.html")

    elif tag == "pat":
        user = int(input(f'   {Xerl} ID Of The User You Want To Pat > '))
        print("\n")
        name = await client.fetch_user(user)
        emb = discord.Embed(title=f'{client.user.name}#{client.user.discriminator} Gave {name} A Pat')
        emb.set_image(url=image)
        emb.set_footer(text="https://www.nekos.fun/apidoc.html")

    elif tag == "feed":
        user = int(input(f'   {Xerl} ID Of The User You Want To Feed > '))
        print("\n")
        name = await client.fetch_user(user)
        emb = discord.Embed(title=f'{client.user.name}#{client.user.discriminator} Fed {name}')
        emb.set_image(url=image)
        emb.set_footer(text="https://www.nekos.fun/apidoc.html")

    elif tag == "cuddle":
        user = int(input(f'   {Xerl} ID Of The User You Want To Cuddle > '))
        print("\n")
        name = await client.fetch_user(user)
        emb = discord.Embed(title=f'{client.user.name}#{client.user.discriminator} Cuddled With {name}')
        emb.set_image(url=image)
        emb.set_footer(text="https://www.nekos.fun/apidoc.html")

    else:
        emb = discord.Embed(title=f'{client.user.name} Used {tag}')
        emb.set_image(url=image)
        emb.set_footer(text="https://www.nekos.fun/apidoc.html")
    
    await ctx.send(embed=emb)

@client.command()
async def av(ctx):
    await ctx.message.delete()
    
    userid = int(input(f'   {Xerl} ID Of The User > '))
    print('\n')
    user = await client.fetch_user(userid)
    avatar = user.avatar_url

    if userid == client.user.id:
        embed = discord.Embed(title=f'Your Avatar:')
        embed.set_image(url=avatar)

    else:
        embed = discord.Embed(title=f'{user}\'s Avatar')
        embed.set_image(url=avatar)

    await ctx.send(embed=embed)

@client.command()
async def ban(ctx):
    await ctx.message.delete()

    try:
        user = int(input(f'{Xerl} User ID You Want To Ban > '))
        if user == client.user.id:
            print(f'    {Err} You Can\'t Ban Yourself.')
    except Exception as ValueError:
        print(f'    {Err} {ValueError}')

    reason = input(f'{Xerl} Ban Reason > ')
    
    await user.ban(reason=reason)
    print(f'{Xerl} <@!{user}> Successfully Banned For: {reason}')

@client.command()
async def calc(ctx):
    await ctx.message.delete()

    try:
        print(f'   {Xerl} Operators: (Subtract: - , Add: +, Multiply: *, Divide: /)')
        Num1 = float(input(f'   {Xerl} Number 1 > '))
        Num2 = float(input(f'   {Xerl} Number 2 > '))
        operator = input(f'   {Xerl} Math Operator > ')

        if operator == "-":
            ans = Num1 - Num2
            await ctx.send(f'{Num1} {operator} {Num2} Is: {ans}')
        elif operator == "+":
            ans = Num1 + Num2
            await ctx.send(f'{Num1} {operator} {Num2} Is: {ans}')
        elif operator == "*":
            ans = Num1 * Num2
            await ctx.send(f'{Num1} {operator} {Num2} Is: {ans}')
        elif operator == "/":
            ans = Num1 / Num2
            await ctx.send(f'{Num1} {operator} {Num2} Is: {ans}')
        else:
            print(f'   {Err} Invalid Operator. Ex: (- , +, *, /)')

    except Exception as ValError:
        print(f'    {Err} {ValError}')

@client.command()
async def friends(ctx):
    await ctx.message.delete()

    flist = open('friends.txt','r+',encoding='utf-8')

    print(f'    {Xerl} Wrote All Friends To {flist.name}')
    for user in client.user.friends:
        friends = user.name+'#'+user.discriminator
        flist.write(str(friends)+"\n")

try:
    client.run(token, bot=False, reconnect=True)

except LoginFailure:
    print(f'    {Err} Improper Token Has Been Passed.')
    input("    press 'ENTER' to exit.")