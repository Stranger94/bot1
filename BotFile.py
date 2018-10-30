#Bot from Stranger

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import os
import random
import math
import logging

global a
global b
global x
global y




def stopwatch(seconds):
    start = time.time()
    time.clock()    
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        time.sleep(1)  

def cooldown(seconds):
    start = time.time()
    time.clock()    
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        time.sleep(1)  


bot = commands.Bot(command_prefix='~')

pfp_path = "C:\Users\Richard\Desktop\pfp.png"

fp = open(pfp_path, 'rb')
pfp = fp.read()

@bot.event
async def on_ready():
    print ("Ready")
    print ("Bot Name: " + bot.user.name)
    print ("Bot ID: " + bot.user.id)    
    bot.loop.create_task(status())
    await bot.edit_profile(password=None, avatar=pfp)


@commands.cooldown(1, 30, commands.BucketType.user)


@bot.command(pass_context = True)
async def ping(ctx):
       await bot.say("Pong") 

      

@bot.command(pass_context=True)
async def mute(ctx, user: discord.Member):
    if ctx.message.author.server_permissions.kick_members:
        role = discord.utils.get(user.server.roles, name='Muted(Meee)')
        embed = discord.Embed(title="{} has been muted!".format(user.name) , color=0x0072ff)
        embed.set_thumbnail(url=user.avatar_url)
        await bot.add_roles(user, role)
        await bot.say(embed=embed)
       
    else:
       embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff0000)
       await bot.say(embed=embed)

@bot.command(pass_context=True)
async def tempmute(ctx, user: discord.Member):
    #ctx.message.author.server_permissions.kick_members or 
       if not ("444444522450124817" in (role.id for role in ctx.message.author.roles)):
        if ("504819720197898252" in (role.id for role in ctx.message.author.roles)):

            role = discord.utils.get(user.server.roles, name='Muted(Meee)') 
            x = random.randint(1, 10)
            embed = discord.Embed(title="{} has been muted for ".format(user.name) + str(x) + " minutes", color=0x0072ff)

            embed.set_thumbnail(url=user.avatar_url)
            await bot.add_roles(user, role)
            await bot.say(embed=embed)
            rolex = discord.utils.get(user.server.roles, name='AngryMod') 
            await bot.remove_roles(ctx.message.author, rolex)
            x = x*60
            await asyncio.sleep(x)
            #stopwatch(x * 60)

            await bot.remove_roles(user, role)
            await asyncio.sleep(5)
            await bot.add_roles(user, rolex)
            embed = discord.Embed(title="{} recovered.".format(user.name) , color=0x0072ff)
            await bot.say(embed=embed)
          
        else:
            embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff0000)
            await bot.say(embed=embed)
            
@bot.command(pass_context=True)
async def guess(ctx, y: int):
    if ("504819720197898252" in (role.id for role in ctx.message.author.roles)):
        embed = discord.Embed(title="You cannot win something, you already have!", description="You have AngryMod role already!", color=0xff0000)
        await bot.say(embed=embed)
    else:
            a = random.randint(1, 100)
            await bot.say("Ok, lemme roll the dice")
            await asyncio.sleep(2)
            await bot.say("...")
            await asyncio.sleep(1)
            await bot.say("...")
            await asyncio.sleep(1)
            await bot.say("I rolled a " + str(a) + "!") 
            

            if y == a:
                 
                 rolex = discord.utils.get(ctx.message.server.roles, name='AngryMod')
                 await bot.add_roles(ctx.message.author, rolex)
                 embed = discord.Embed(title="Congratulations {}! You win the AngryMod role.".format(ctx.message.author.name) , color=0xff72ff)
                 await bot.say(embed=embed)
                  
            else:
                 embed = discord.Embed(title="{} guessed wrong HAHA".format(ctx.message.author.name) , color=0xf072ff)
                 await bot.say(embed=embed) 
                 
@commands.cooldown(1, 300, commands.BucketType.user)

@bot.command(pass_context=True)
async def nuke(ctx, user: discord.Member):
    
    role = discord.utils.get(user.server.roles, name='Muted(Meee)')
    x = random.randint(5, 30)
    embed = discord.Embed(title="{}, shut up for ".format(user.name) + str(x) + " seconds ploz.", color=0x0072ff)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.add_roles(user, role)
    await bot.say(embed=embed)
    await asyncio.sleep(x)
    await bot.remove_roles(user, role)
    await bot.say("{} is back".format(user.name))

@bot.command(pass_context=True, hidden=True)
async def status(ctx):
    while True:
        await bot.change_presence(game=discord.Game(name="Strangers Bot"), status=discord.Status("online"))
        await asyncio.sleep(20)
        await bot.change_presence(game=discord.Game(name="~nuke someone"), status=discord.Status("idle"))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name="~guess a number"), status=discord.Status("dnd"))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name="Bored, pls help!"), status=discord.Status("idle"))
        await asyncio.sleep(10)

bot.run(os.getenv('TOKEN'))

