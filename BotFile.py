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

client = discord.Client()
bot = commands.Bot(command_prefix='~')


@bot.event
async def on_ready():
        print ("Ready")
        print ("Bot Name: " + bot.user.name)
        print ("Bot ID: " + bot.user.id)    
        
@client.event
async def on_ready():
    client.loop.create_task(status())


    
    
@commands.cooldown(1, 10, commands.BucketType.user)


@bot.command(pass_context = True)
async def ping(ctx):
       embed = discord.Embed(title= "Bot by Stranger#1405", description="Last update: 02.11.2018 10:30. Bug fixes." , color=0x80f43d)
       await bot.say(embed=embed)
      
@commands.cooldown(1, 30, commands.BucketType.user)

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
@commands.cooldown(1, 30, commands.BucketType.user)

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
@commands.cooldown(2, 120, commands.BucketType.user)            
@bot.command(pass_context=True)
async def guess(ctx, y: int):
    if ("504819720197898252" in (role.id for role in ctx.message.author.roles)):
        embed = discord.Embed(title="You cannot win something, you already have!", description="You have AngryMod role already!", color=0xfcf7f8)
        await bot.say(embed=embed)
    else:

        if (y > 30 or y < 1):
            embed = discord.Embed(title="Unknown constructions? Dick stuck in sink.", description="Guess from 1 to 30, and nothing weird!", color=0x660e1b)
            await bot.say(embed=embed)
        else:
            a = random.randint(1, 30)
            await bot.say("Ok, lemme roll the dice")
            await asyncio.sleep(3)
            await bot.say("...")
            await asyncio.sleep(3)
            await bot.say("...")
            await asyncio.sleep(1)
            await bot.say("I rolled a " + str(a) + "!") 
            
            if y == a:
                 
                 rolex = discord.utils.get(ctx.message.server.roles, name='AngryMod')
                 await bot.add_roles(ctx.message.author, rolex)
                 embed = discord.Embed(title="Congratulations {}! You win the AngryMod role.".format(ctx.message.author.name) , color=0x7cff30)
                 await bot.say(embed=embed)
            else:

                if ((y + 2) == a or (y + 1) == a or (y - 1) == a or (y - 2) == a):
                 
                        embed = discord.Embed(title= "Very scarce oO", description="{} almost guessed right. Dammit.".format(ctx.message.author.name) , color=0xc99206)
                        await bot.say(embed=embed)
                        await bot.say("Ok...Rerolling.")
                        a = random.randint(1, 30)
                        await asyncio.sleep(3)
                        await bot.say("...")
                        await asyncio.sleep(3)
                        await bot.say("...")
                        await asyncio.sleep(3)
                        await bot.say("I rolled a " + str(a) + "!") 
                
                        if y == a:
                 
                            await bot.add_roles(ctx.message.author, rolex)
                            embed = discord.Embed(title="Congratulations {}! You win the AngryMod role.".format(ctx.message.author.name) , color=0x7cff30)
                            await bot.say(embed=embed)
                  
                        else:
                            embed = discord.Embed(title="{} guessed wrong and I won't reroll!".format(ctx.message.author.name) , color=0xdb0020)
                            await bot.say(embed=embed) 
                else:
                        embed = discord.Embed(title="{} can't defeat me!".format(ctx.message.author.name) , color=0xdb0020)
                        await bot.say(embed=embed) 
                 
                 
@commands.cooldown(2, 300, commands.BucketType.user)

@bot.command(pass_context=True)
async def nuke(ctx, user: discord.Member):
    
    role = discord.utils.get(user.server.roles, name='Muted(Meee)')
    x = random.randint(1, 50)
    embed = discord.Embed(title="{}, shut up for ".format(user.name) + str(x) + " seconds ploz.", color=0x0072ff)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.add_roles(user, role)
    await bot.say(embed=embed)
    await asyncio.sleep(x)
    await bot.remove_roles(user, role)
    await bot.say("{} is back".format(user.name))

@bot.command(pass_context=True)
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
@bot.command(pass_context=True)
async def botguess(ctx):
  while True:

    await asyncio.sleep(2000)
    if False:
        y = random.randint(1, 30)
        await bot.say("~guess " + str(y))
        
    else:
        
        if False:
            embed = discord.Embed(title="Unknown constructions? Dick stuck in sink.", description="Guess from 1 to 30, and nothing weird!", color=0x660e1b)
            await bot.say(embed=embed)
        else:
            y = random.randint(1, 30)
            await bot.say("~guess " + str(y))
            a = random.randint(1, 30)
            await bot.say("Rolling...")
            await asyncio.sleep(3)
            await bot.say("...")
            await asyncio.sleep(3)
            await bot.say("...")
            await asyncio.sleep(3)
            await bot.say("I rolled a " + str(a) + "!") 
            
            if y == a:
                 
                
                 embed = discord.Embed(title="I win, yay." , color=0x7cff30)
                 await bot.say(embed=embed)
            else:

                if ((y + 2) == a or (y + 1) == a or (y - 1) == a or (y - 2) == a):
                 
                        embed = discord.Embed(title= "Very scarce oO", description="Dammit.", color=0xc99206)
                        await bot.say(embed=embed)
                        await bot.say("Ok...Rerolling.")
                        a = random.randint(1, 30)
                        await asyncio.sleep(3)
                        await bot.say("...")
                        await asyncio.sleep(3)
                        await bot.say("...")
                        await asyncio.sleep(3)
                        await bot.say("I rolled a " + str(a) + "!") 
                
                        if y == a:
                 
  
                            embed = discord.Embed(title="Congratulations to me, I win!" , color=0x7cff30)
                            await bot.say(embed=embed)
                  
                        else:
                            embed = discord.Embed(title="Nvm, fail!".format(ctx.message.author.name) , color=0xdb0020)
                            await bot.say(embed=embed) 
                else:
                        embed = discord.Embed(title="Aw, no luck!", color=0xdb0020)
                        await bot.say(embed=embed) 

@bot.event
async def on_ready():
        client.loop.create_task(botguess())
    
    
@commands.cooldown(1, 500, commands.BucketType.user)            
@bot.command(pass_context=True)
async def battle(ctx, user: discord.Member):

     embed = discord.Embed(title = "A random day", description="{} challenges {} to a battle!".format(ctx.message.author.name, user.name) , color=0xbc4403)
     await bot.say(embed=embed)
     await asyncio.sleep(5)



     if ("507312880211984384" in (role.id for role in ctx.message.author.roles)):
         Attack = 30
         str1 = "pulls out his Dragon sword"
     else:
         if ("507312873337389057" in (role.id for role in ctx.message.author.roles)):
             Attack = 27
             str1 = "pulls out his Ameythst sword"
         else: 
             if ("497058717305667586" in (role.id for role in ctx.message.author.roles)):
                 Attack = 24
                 str1 = "pulls out his Diamond sword"
             else:
                 if ("497058660535762946" in (role.id for role in ctx.message.author.roles)):
                     Attack = 22
                     str1 = "pulls out his Gold sword"
                 else: 
                     if ("497058624934379522" in (role.id for role in ctx.message.author.roles)):
                        Attack = 19
                        str1 = "pulls out his Stone sword"
                     else: 
                         if ("497058550192013312" in (role.id for role in ctx.message.author.roles)):
                             Attack = 12
                             str1 = "pulls out his Wood sword"
                         else:  
                                Attack = 5
                                str1 = "charges with bare hands"

     if ("507324396252299268" in (role.id for role in ctx.message.author.roles)):
         Defense = 8
     else:
         if ("507324354577825793" in (role.id for role in ctx.message.author.roles)):
             Defense = 6
         else: 
             if ("507324314820018217" in (role.id for role in ctx.message.author.roles)):
                 Defense = 5
             else:
                 if ("507324278547677219" in (role.id for role in ctx.message.author.roles)):
                     Defense = 4
                 else: 
                     if ("507324244053590026" in (role.id for role in ctx.message.author.roles)):
                        Defense = 2
                     else: 
                         if ("507324191117148172" in (role.id for role in ctx.message.author.roles)):
                             Defense = 1
                         else: Defense = 0




     if ("507312880211984384" in (role.id for role in user.roles)):
         Attack2 = 30
     else:
         if ("507312873337389057" in (role.id for role in user.roles)):
             Attack2 = 27
         else: 
             if ("497058717305667586" in (role.id for role in user.roles)):
                 Attack2 = 24
             else:
                 if ("497058660535762946" in (role.id for role in user.roles)):
                     Attack2 = 22
                 else: 
                     if ("497058624934379522" in (role.id for role in user.roles)):
                        Attack2 = 19
                     else: 
                         if ("497058550192013312" in (role.id for role in user.roles)):
                             Attack2 = 12
                         else:  
                                Attack2 = 5

     if ("507324396252299268" in (role.id for role in user.roles)):
         Defense2 = 8
     else:
         if ("507324354577825793" in (role.id for role in user.roles)):
             Defense2 = 6
         else: 
             if ("507324314820018217" in (role.id for role in user.roles)):
                 Defense2 = 5
             else:
                 if ("507324278547677219" in (role.id for role in user.roles)):
                     Defense2 = 4
                 else: 
                     if ("507324244053590026" in (role.id for role in user.roles)):
                        Defense2 = 2
                     else: 
                         if ("507324191117148172" in (role.id for role in user.roles)):
                             Defense2 = 1
                         else: Defense2 = 0
     
     embed = discord.Embed(title = "Battle begins", description="{} ".format(ctx.message.author.name) + str1 + " to attack {}".format(user.name), color=0x03bc4d)
     await bot.say(embed=embed)

     Damage1 = Attack - Defense2
     Damage2 = Attack2 - Defense
     HP1 = 200
     HP2 = 200

     if ("497072853326495755" in (role.id for role in ctx.message.author.roles)):
         Chance = 17
     else:
         if ("444427406225309696" in (role.id for role in ctx.message.author.roles)):
             Chance = 16
         else: 
             if ("504819720197898252" in (role.id for role in ctx.message.author.roles)):
                 Chance = 15
             else:
                 if ("444844581062836244" in (role.id for role in ctx.message.author.roles)):
                     Chance = 14
                 else: 
                     if ("502174923557699584" in (role.id for role in ctx.message.author.roles)):
                        Chance = 13
                     else: 
                         if ("444448025482493955" in (role.id for role in ctx.message.author.roles)):
                             Chance = 12
                         else: 
                            if ("500092762226556939" in (role.id for role in ctx.message.author.roles)):
                                Chance = 11
                            else: 
                                if ("444426912845266944" in (role.id for role in ctx.message.author.roles)):
                                    Chance = 10
                                else:  
                                    if ("497051370386489344" in (role.id for role in ctx.message.author.roles)):
                                       Chance = 9
                                    else:
                                          Chance = 8

     if ("497072853326495755" in (role.id for role in user.roles)):
            Chance2 = 17
     else:
         if ("444427406225309696" in (role.id for role in user.roles)):
             Chance2 = 16
         else: 
             if ("504819720197898252" in (role.id for role in user.roles)):
                 Chance2 = 15
             else:
                 if ("444844581062836244" in (role.id for role in user.roles)):
                     Chance2 = 14
                 else: 
                     if ("502174923557699584" in (role.id for role in user.roles)):
                        Chance2 = 13
                     else: 
                         if ("444448025482493955" in (role.id for role in user.roles)):
                             Chance2 = 12
                         else: 
                            if ("500092762226556939" in (role.id for role in user.roles)):
                                Chance2 = 11
                            else: 
                                if ("444426912845266944" in (role.id for role in user.roles)):
                                    Chance2 = 10
                                else:  
                                    if ("497051370386489344" in (role.id for role in user.roles)):
                                       Chance2 = 9
                                    else:
                                          Chance2 = 8

#Battle

     await asyncio.sleep(2)

     w = 0
      
     while (HP1 > 0 and HP2 > 2):
            await asyncio.sleep(2)
            w += 1
            
            


            if (w > 20 and w < 22):
                await bot.say("Both players aggreed to a draw.")
            else:


                await bot.say("Round " + str(w))
                a1 = random.randint(1, 20)
                a2 = random.randint(1, 20)
                if a1 <= Chance:
                    HP2 = HP2 - Damage1
                    await bot.say("{} does ".format(ctx.message.author.name) + str(Damage1) + "damage. {} has ".format(user.name) + str(HP2) + " HP left.")
                else: 
                    await bot.say("{} misses".format(ctx.message.author.name) + "{} has ".format(user.name) + str(HP2) + " HP left.")

                if a2 <= Chance2:
                    HP1 = HP1 - Damage2
                    await bot.say("{} does ".format(user.name) + str(Damage2) + "damage. {} has ".format(ctx.message.author.name) + str(HP1) + " HP left.")
                else:
                    await bot.say("{} misses".format(user.name) + "{} has ".format(ctx.message.author.name) + str(HP1) + " HP left.")
     

     if (HP1 > 0):
        embed = discord.Embed(title = "Result", description="{} wins. ".format(ctx.message.author.name) + "{} cannot defend and is dead.".format(user.name), color=0x03bc4d)
        await bot.say(embed=embed)

        role = discord.utils.get(user.server.roles, name='Muted(Meee)')
        x = random.randint(10, 100)
        embed = discord.Embed(title="{} gets muted for".format(user.name) + str(x) + " seconds. Hope he can recover in that time.", color=0x0072ff)
        embed.set_thumbnail(url=user.avatar_url)
        await bot.add_roles(user, role)
        await bot.say(embed=embed)
        await asyncio.sleep(x)
        await bot.remove_roles(user, role)
        await bot.say("{} recovered his HP.".format(user.name))

     if (HP2 > 0):
         embed = discord.Embed(title = "Result", description="{} wins. ".format(user.name) + "{} attacked and died lmao. You savage got your payoff.".format(ctx.message.author.name), color=0x03bc4d)
         await bot.say(embed=embed)
         role = discord.utils.get(user.server.roles, name='Muted(Meee)')
         x = random.randint(50, 300)
         embed = discord.Embed(title="{} gets muted for".format(ctx.message.author.name) + str(x) + " seconds. Hope he can recover in that time.", color=0x0072ff)
         embed.set_thumbnail(url=ctx.message.author.avatar_url)
         await bot.add_roles(ctx.message.author, role)
         await bot.say(embed=embed)
         await asyncio.sleep(x)
         await bot.remove_roles(ctx.message.author, role)
         await bot.say("{} recovered his HP.".format(ctx.message.author.name))
            
bot.run(os.getenv('TOKEN'))

