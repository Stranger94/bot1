#Bot from Stranger

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import os








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

@bot.event
async def on_ready():
    print ("Ready")
    print ("Bot Name: " + bot.user.name)
    print ("Bot ID: " + bot.user.id)    
 


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

    if ("504819720197898252" in (role.id for role in ctx.message.author.roles)):
            role = discord.utils.get(user.server.roles, name='Muted(Meee)') 
            embed = discord.Embed(title="{} has been muted for 5 minute".format(user.name), color=0x0072ff)
            embed.set_thumbnail(url=user.avatar_url)
            await bot.add_roles(user, role)
            await bot.say(embed=embed)
            rolex = discord.utils.get(user.server.roles, "504819720197898252" in (role.id for role in ctx.message.author.roles)) 
            await bot.remove_roles(ctx.message.author, "504819720197898252" in role.id)

            await asyncio.sleep(300)
            #stopwatch(10)

            role2 = discord.utils.get(user.server.roles, name='Muted(Meee)')
            embed = discord.Embed(title="{} unmuted.".format(user.name) , color=0x0072ff)
            await bot.remove_roles(user, role2)
            await bot.say(embed=embed)
          
    else:
            embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff0000)
            await bot.say(embed=embed)


bot.run(os.getenv('TOKEN'))


