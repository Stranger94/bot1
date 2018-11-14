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
import datetime
from discord.utils import get

client = discord.Client()
bot = commands.Bot(command_prefix=("~", "-"))

async def status():
    await bot.wait_until_ready()
    while not bot.is_closed:
        await bot.change_presence(game=discord.Game(name="Strangers Bot"), status=discord.Status("online"))
        await asyncio.sleep(20)
        await bot.change_presence(game=discord.Game(name="~nuke someone"), status=discord.Status("idle"))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name="~guess a number"), status=discord.Status("dnd"))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name="Bored, pls help!"), status=discord.Status("idle"))
        await asyncio.sleep(10)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.loop.create_task(status())

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(pass_context = True)
async def info(ctx):
       embed = discord.Embed(title= "Bot by Stranger#1405", description="Prefix: -/~\n**Latest updates:** Bot will reply sometimes on hi. You can run now, when battled with -battle, there will be added more options soon (**using badages for example**)." , color=0x80f43d)
       await bot.say(embed=embed)    


@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(pass_context = True)
async def ping(ctx):
       embed = discord.Embed(title= "Bot by Stranger#1405", description="Last update: 13.11.2018 21:49.\nFor latest updates: Type -info\n_____________<:stoneswordnoob:509197316930928650>_____________" , color=0x80f43d)
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

@commands.cooldown(1, 120, commands.BucketType.user)
@bot.command(pass_context=True)
async def tempmute(ctx, user: discord.Member):
    #ctx.message.author.server_permissions.kick_members or 
  
  if ("504819720197898252" in (role.id for role in ctx.message.author.roles)):

    if ("444444522450124817" in (role.id for role in user.roles)):
        
       await bot.say("{} is already muted.".format(user.name))

    else:
       if ("444444522450124817" in (role.id for role in ctx.message.author.roles)):

        await bot.say("Wait till you aren't muted anymore, {}.".format(ctx.message.author.name))

       else:

            role = discord.utils.get(user.server.roles, name='Muted(Meee)') 
            x = random.randint(5, 10)
            embed = discord.Embed(title="{} has been muted for ".format(user.name) + str(x) + " minutes", color=0x0072ff)

            embed.set_thumbnail(url=user.avatar_url)
            await bot.add_roles(user, role)
            await bot.say(embed=embed)
            rolex = discord.utils.get(user.server.roles, name='AngryMod') 
            await bot.remove_roles(ctx.message.author, rolex)
            x = x * 10
            i = 1
            while i <= x:
                await asyncio.sleep(6)
                await bot.add_roles(user, role)
                i = i+1
            #stopwatch(x * 60)

            await bot.remove_roles(user, role)
            await asyncio.sleep(5)
            embed = discord.Embed(title="{} is fully recovered.".format(user.name) , color=0x0072ff)
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
   
 
 if ("444444522450124817" in (role.id for role in ctx.message.author.roles)):
    await bot.say("You failed and nuked yourself, {}.".format(ctx.message.author.name))   

 else:
   if not ("444444522450124817" in (role.id for role in user.roles)):

    role = discord.utils.get(user.server.roles, name='Muted(Meee)')
    x = random.randint(1, 40)
    embed = discord.Embed(title="{}, shut up for ".format(user.name) + str(x) + " seconds ploz.", color=0x0072ff)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.add_roles(user, role)
    await bot.say(embed=embed)
    await asyncio.sleep(x)
    await bot.remove_roles(user, role)
    await bot.say("{} is back".format(user.name))



   else:
    if ("444444522450124817" in (role.id for role in user.roles)):
        await bot.say("{} is muted already.".format(user.name))

@commands.cooldown(1, 120, commands.BucketType.user)            
@bot.command(pass_context=True)
async def battle(ctx, user: discord.Member):
     band1 = random.randint(1, 5)
     band2 = random.randint(1, 5)
     Sce1 = "Forest"
     #Sce2 = "Winter"
     #Sce3 = "Ocean"

     #s = random.randint(1, 3)

     g = random.randint(1, 3)


     if g == 1:
      embed = discord.Embed(title = "Scenario: " + Sce1 , description="{} challenges {} to a battle in the ".format(ctx.message.author.name, user.name) + Sce1 + "!" , color=0xbc4403)
     if g == 2:
      embed = discord.Embed(title = "Scenario: " + Sce1 , description="{} attacks {} in the ".format(ctx.message.author.name, user.name) + Sce1 + "!" , color=0xbc4403)
     if g == 3:
      embed = discord.Embed(title = "Scenario: " + Sce1 , description="{} running into an ambush from {} in the ".format(user.name, ctx.message.author.name) + Sce1 + "!" , color=0xbc4403)

     await bot.say(embed=embed)

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
         MDefense = 27
     else:
         if ("507324354577825793" in (role.id for role in ctx.message.author.roles)):
             Defense = 6
             MDefense = 23
         else: 
             if ("507324314820018217" in (role.id for role in ctx.message.author.roles)):
                 Defense = 5
                 MDefense = 19
             else:
                 if ("507324278547677219" in (role.id for role in ctx.message.author.roles)):
                     Defense = 4
                     MDefense = 13
                 else: 
                     if ("507324244053590026" in (role.id for role in ctx.message.author.roles)):
                        Defense = 2
                        MDefense = 8
                     else: 
                         if ("507324191117148172" in (role.id for role in ctx.message.author.roles)):
                             Defense = 1
                             MDefense = 4
                         else: 
                               Defense = 0
                               MDefense = 0




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
         MDefense2 = 27
     else:
         if ("507324354577825793" in (role.id for role in user.roles)):
             Defense2 = 6
             MDefense2 = 23
         else: 
             if ("507324314820018217" in (role.id for role in user.roles)):
                 Defense2 = 5
                 MDefense2 = 19
             else:
                 if ("507324278547677219" in (role.id for role in user.roles)):
                     Defense2 = 4
                     MDefense2 = 13
                 else: 
                     if ("507324244053590026" in (role.id for role in user.roles)):
                        Defense2 = 2
                        MDefense2 = 8
                     else: 
                         if ("507324191117148172" in (role.id for role in user.roles)):
                             Defense2 = 1
                             MDefense2 = 4
                         else: 
                             Defense2 = 0
                             MDefense2 = 0
     
     newx1 = await bot.say("{}, type 'run' if you want to try to escape!".format(user.name))
     checkmsg1 = await bot.wait_for_message(timeout= 10.0, author= user, content="run", check= None)

     await asyncio.sleep(10)
     try:
                if checkmsg1.content == "run":
                                    await bot.delete_message(newx1)

                                    await bot.say("{} runs away.".format(user.name))
                                    return

     except:
                                    await bot.delete_message(newx1)
    
    
    
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

     await asyncio.sleep(2)

     w = 0

     WolfD = 40
     SpiderD = 30
     FoxD = 40
     BearD = 70
     PiranhaD = 40
     CrabD = 25
     NoobD = 19

     WolfD1 = WolfD - MDefense
     SpiderD1 = SpiderD - MDefense
     FoxD1 = FoxD - MDefense
     BearD1 = BearD - MDefense
     PiranhaD1 = PiranhaD - MDefense
     CrabD1 = CrabD - MDefense
     NoobD1 = NoobD - Defense

     WolfD2 = WolfD - MDefense2
     SpiderD2 = SpiderD - MDefense2
     FoxD2 = FoxD - MDefense2
     BearD2 = BearD - MDefense2
     PiranhaD2 = PiranhaD - MDefense2
     CrabD2 = CrabD - MDefense2
     NoobD2 = NoobD - Defense2

     
      
     while (HP1 > 0 and HP2 > 2):
            
            w += 1


            if (w > 20 and w < 22):
                await bot.say("Both players aggreed to a draw.")
            else:
                if w == 1:

                    msg = await bot.say("Round " + str(w))
                    msgx = await bot.say("{} HP:  200".format(ctx.message.author.name))
                    msgy = await bot.say("{} HP:  200".format(user.name))
                    await asyncio.sleep(2)
                    a1 = random.randint(1, 20)
                    a2 = random.randint(1, 20)
                    if a1 <= Chance:
                        HP2 = HP2 - Damage1
                        msg1 = await bot.say("{} does ".format(ctx.message.author.name) + str(Damage1) + " damage.")
                        await bot.edit_message(msgy, "{} HP: ".format(user.name) + str(HP2))
                    else: 
                        msg1 = await bot.say("{} misses.".format(ctx.message.author.name))

                    if a2 <= Chance2:
                        HP1 = HP1 - Damage2
                        msg2 = await bot.say("{} does ".format(user.name) + str(Damage2) + " damage.")
                        await bot.edit_message(msgx, "{} HP: ".format(ctx.message.author.name) + str(HP1))
                        await asyncio.sleep(2)
                    else:
                        msg2 = await bot.say("{} misses".format(user.name))
                        await asyncio.sleep(2)
                    msgz = await bot.say("Noobs are getting interested in the fight. Animals are getting in the way.")

                else:
                    if (w > 1 and w < 21):
                        await bot.edit_message(msg, "Round " + str(w))
                        a1 = random.randint(1, 20)
                        a2 = random.randint(1, 20)
                        e11 = random.randint(1, 20)     #wolf attack chance 15%
                        e21 = random.randint(1, 20)     #spider attack chance 10%
                        e31 = random.randint(1, 20)     #crab attack chance 10%
                        e41 = random.randint(1, 20)     #noob attack chance 10%
                        e12 = random.randint(1, 20)     #wolf attack chance 5%
                        e22 = random.randint(1, 20)     #spider attack chance 10%
                        e32 = random.randint(1, 20)     #crab attack chance 5%
                        e42 = random.randint(1, 20)     #noob attack chance 20%

                        if a1 <= Chance:
                            HP2 = HP2 - Damage1
                            q1 = "{} does ".format(ctx.message.author.name) + str(Damage1) + " damage."

                        else: 
                            q1 = "{} misses".format(ctx.message.author.name)

                        if a2 <= Chance2:
                            HP1 = HP1 - Damage2
                            q2 = "{} does ".format(user.name) + str(Damage2) + " damage."
                            await asyncio.sleep(2)
                        else:
                            q2 = "{} misses".format(user.name)
                            await asyncio.sleep(2)
                            
                        if (band2 == 4 or band2 == 9 or band2 == 14 or band2 == 19):

                                
                                newx2 = await bot.say("{}, use garlic for regeneration?(Type: 'yes' (**FAST**))".format(user.name))
                                checkmsg2 = await bot.wait_for_message(timeout= 3.0, author= user, content="yes", check= None)

                                await asyncio.sleep(3)
                                try:
                                    if checkmsg2.content == "yes":
                                        await bot.delete_message(newx2)

                                        mgg2 = await bot.say("{} recovers 20 HP.".format(user.name))
                                        
                                        if HP2 <= 180:
                                            HP2 = HP2 + 20
                                        else:
                                            HP2 = 200
                                        

                                except:
                                        mgg2 = await bot.say("{} recovers 10 HP.".format(user.name))                                        
                                        
                                        if HP2 <= 190:
                                            HP2 = HP2 + 10
                                        else:
                                            HP2 = 200


                                    


                        if (band1 == 4 or band1 == 9 or band1 == 14 or band1 == 19):
                                newx3 = await bot.say("{}, use garlic for regeneration?(Type: 'yes' (**FAST**))".format(ctx.message.author.name))
                                checkmsg3 = await bot.wait_for_message(timeout= 3.0, author= ctx.message.author, content="yes", check= None)

                                await asyncio.sleep(3)
                                try:
                                    if checkmsg3.content == "yes":
                                        await bot.delete_message(newx3)

                                        mgg3 = await bot.say("{} recovers 20 HP.".format(ctx.message.author.name))
                                        
                                        if HP1 <= 180:
                                            HP1 = HP1 + 20
                                        else:
                                            HP1 = 200
                                        

                                except:
                                        mgg3 = await bot.say("{} recovers 10 HP.".format(ctx.message.author.name))                                        
                                        
                                        if HP1 <= 190:
                                            HP1 = HP1 + 10
                                        else:
                                            HP1 = 200



                        band1 = band1 + 1
                        band2 = band2 + 1

                           

            MobDamage1 = 0
            MobDamage2 = 0
            w00 = ""
            w0 = ""
            if (w > 1 and w < 21):
                if e11 <= 3:
                    w1 = (" <:Dwolf:504455555255894056>")
                    MobDamage1 = MobDamage1 + WolfD1
                    w0 = "from"
                else:
                    w1 = ""
                if e21 <= 2:
                    w2 = " <:Dspider:504451731481034767>"
                    MobDamage1 = MobDamage1 + SpiderD1
                    w0 = "from"
                else:
                    w2 = ""
                if e31 <= 2:
                    w3 = " <:Dcrab:509197291890933760>"
                    MobDamage1 = MobDamage1 + CrabD1
                    w0 = "from"
                else:
                    w3 = ""
                if e41 <= 2:
                    w4 = " <:stoneswordnoob:509197316930928650>"
                    MobDamage1 = MobDamage1 + NoobD1
                    w0 = "from"
                else:
                    w4 = ""   
                if e12 <= 1:
                    w5 = (" <:Dwolf:504455555255894056>")
                    MobDamage2 = MobDamage2 + WolfD2
                    w00 = "from"
                else:
                    w5 = ""
                if e22 <= 2:
                    w6 = " <:Dspider:504451731481034767>"
                    MobDamage2 = MobDamage2 + SpiderD2
                    w00 = "from"
                else:
                    w6 = ""                
                if e32 <= 1:
                    w7 = " <:Dcrab:509197291890933760>"
                    MobDamage2 = MobDamage2 + CrabD2
                    w00 = "from"
                else:
                    w7 = ""
                if e42 <= 4:
                    w8 = " <:stoneswordnoob:509197316930928650>"
                    MobDamage2 = MobDamage2 + NoobD2
                    w00 = "from"
                else:
                    w8 = ""
                    
                
                HP1 = HP1 - MobDamage1
                HP2 = HP2 - MobDamage2
                q11 = "{} **HP: ".format(user.name) + str(HP2) + "**"
                q22 = "{} **HP: ".format(ctx.message.author.name) + str(HP1) + "**"

                await bot.edit_message(msg1, q1)
                await bot.edit_message(msg2, q2)
                await bot.edit_message(msgz, "{} takes ".format(ctx.message.author.name) + str(MobDamage1) + " damage " + w0 + w1 + w2 + w3 + w4 + ". {} takes ".format(user.name) + str(MobDamage2) + " damage " + w00 + w5 + w6 + w7 + w8 + ".")        
                await asyncio.sleep(2)
                
                try:
                    await bot.delete_message(mgg2)
                    await bot.delete_message(mgg3)
                except: 
                    True
                await bot.edit_message(msgy, q11)
                await bot.edit_message(msgx, q22)
                await asyncio.sleep(3)






     if (HP1 > 0):
        await bot.delete_message(msg1)
        await bot.delete_message(msg2)
        await bot.delete_message(msgz)
        await bot.delete_message(msgx)
        await bot.delete_message(msgy)
        embed = discord.Embed(title = "Result", description="{} wins. ".format(ctx.message.author.name) + "{} loses and is dead.".format(user.name), color=0x03bc4d)
        await bot.say(embed=embed)
        role = discord.utils.get(user.server.roles, name='Muted(Meee)')
        x = random.randint(10, 60)
        embed = discord.Embed(title="{} gets muted for ".format(user.name) + str(x) + " seconds. Hope he can recover in that time.", color=0x0072ff)
        embed.set_thumbnail(url=user.avatar_url)
        await bot.add_roles(user, role)
        await bot.say(embed=embed)
        await asyncio.sleep(x)
        await bot.remove_roles(user, role)
        await bot.say("{} is back".format(user.name))

     if (HP2 > 0):
         await bot.delete_message(msg1)
         await bot.delete_message(msg2)
         await bot.delete_message(msgz)
         await bot.delete_message(msgx)
         await bot.delete_message(msgy)
         embed = discord.Embed(title = "Result", description="{} wins. ".format(user.name) + "{} loses and is dead.".format(ctx.message.author.name), color=0x03bc4d)
         await bot.say(embed=embed)
         role = discord.utils.get(user.server.roles, name='Muted(Meee)')
         x = random.randint(60, 120)
         embed = discord.Embed(title="{} gets muted for".format(ctx.message.author.name) + str(x) + " seconds. Hope he can recover in that time.", color=0x0072ff)
         embed.set_thumbnail(url=ctx.message.author.avatar_url)
         await bot.add_roles(ctx.message.author, role)
         await bot.say(embed=embed)
         await asyncio.sleep(x)
         await bot.remove_roles(ctx.message.author, role)
         await bot.say("{} is back".format(ctx.message.author.name))
     
     if (HP2 < 0 and HP1 < 0):
        await bot.delete_message(msg1)
        await bot.delete_message(msg2)
        await bot.delete_message(msgz)
        await bot.delete_message(msgx)
        await bot.delete_message(msgy)
        await bot.say("Both players died!")
        x = random.randint(10, 60)
        y = random.randint(10, 60)
        yneu = y + 40
        role = discord.utils.get(user.server.roles, name='Muted(Meee)')
        embed = discord.Embed(description="{} gets muted for ".format(user.name) + str(x) + " seconds. {} gets muted for ".format(ctx.message.author.name) + str(yneu) + " seconds.", color=0x0072ff)
        await bot.say(embed=embed)
        if (yneu >= x):
            await bot.add_roles(user, role)
            await bot.add_roles(ctx.message.author, role)
            await asyncio.sleep(x)
            await bot.remove_roles(user, role)
            await bot.say("{} is back".format(user.name))
            yneu = yneu - x
            await asyncio.sleep(yneu)
            await bot.remove_roles(ctx.message.author, role)
            await bot.say("{} is back".format(ctx.message.author.name))
        else:
            await bot.add_roles(user, role)
            await bot.add_roles(ctx.message.author, role)
            await asyncio.sleep(yneu)
            await bot.remove_roles(ctx.message.author, role)
            await bot.say("{} is back".format(ctx.message.author.name))
            x = x - yneu
            await asyncio.sleep(x)
            await bot.remove_roles(user, role)
            await bot.say("{} is back".format(user.name))

@bot.event
async def on_message(message):

  if message.content.startswith('Hi') or message.content.startswith('hi') or message.content.startswith('hey') or message.content.startswith('Hey'):


      delta1 = datetime.timedelta(minutes = 15)  
      now = datetime.datetime.now()

      then = now - delta1
      counter = 0

     #so far its fine

      async for message in bot.logs_from(message.channel, limit=2, after = then): #not counting...
            counter += 1
      if counter == 1:
        if message.content.startswith('Hi') or message.content.startswith('hi') or message.content.startswith('hey') or message.content.startswith('Hey'):
            
            embed = discord.Embed(title="Hi", description="Have a great day!", color=0x1eff38)
            embed.set_author(name="LETS'S GOOOO", url = "https://images-ext-2.discordapp.net/external/sshKs1hxko3YR-vILfivBNCMlQ33YN8uE0zdJhiw8JY/%3Fsize%3D256/https/cdn.discordapp.com/avatars/506186624032571412/7193d48d0f345f633b2959f26b4512b2.png", icon_url="https://vignette.wikia.nocookie.net/yoshi/images/8/8d/Yoshi_SSBU.png/revision/latest?cb=20180628045711")
            embed1 = await bot.send_message(message.channel, embed = embed)            
            await asyncio.sleep(1)

            x1 = await bot.send_message(message.channel, "──────────────████──████────────────\n────────────██░░▒▒██░░▒▒██──────────\n──────────██░░────────▒▒▓▓██────────\n──────────██──██──██────▓▓████████──\n")
            x2 = await bot.send_message(message.channel, "──────────██──██──██──────██░░░░▒▒██\n──────██████──────────────████▒▒▓▓██\n────██░░░░░░██──▓▓──────▓▓░░░░██████\n──██░░────░░░░▓▓░░▓▓▓▓▓▓░░──░░▒▒██░░\n")
            x3 = await bot.send_message(message.channel, "──████──██░░░░░░▒▒░░──────░░░░▒▒██▒▒\n██░░░░░░░░░░░░░░▒▒▒▒────────▒▒▓▓██▓▓\n██░░░░░░░░░░░░▒▒▒▒▓▓────────▒▒▓▓████\n██▒▒░░░░░░▒▒▒▒▒▒▓▓██░░────░░▓▓▓▓████\n")
            x4 = await bot.send_message(message.channel, "██▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓████░░░░▓▓▓▓██▒▒██\n──██▒▒▒▒▒▒▓▓▓▓▓▓▓▓██──░░▓▓▓▓██████──\n────████▓▓▓▓▓▓▓▓██──░░▒▒▒▒▓▓██▒▒██──\n────────████████████▒▒▒▒▒▒▒▒▓▓██────\n")
            x5 = await bot.send_message(message.channel, "────────██▒▒──▒▒██░░░░▒▒──────██────\n────████▒▒▒▒▒▒████░░░░██──────██────\n██████──██████──██░░░░████────██────\n██░░▒▒██──────████░░░░░░████──██────\n")
            x6 = await bot.send_message(message.channel, "██████──██████──██░░░░████────██────\n██░░▒▒██──────████░░░░░░████──██────\n██──▓▓▒▒████████▒▒░░░░██░░████──────\n██────▓▓▒▒░░░░██▒▒░░────░░██████────\n")
            x7 = await bot.send_message(message.channel, "──██░░────▒▒▒▒██▓▓▒▒░░░░░░██████────\n──██░░░░──────░░██▓▓▒▒░░████░░██────\n────████████████░░██████▒▒████──────\n────██▓▓▒▒░░░░██▒▒▒▒██████──────────\n")
            x8 = await bot.send_message(message.channel, "────██▓▓▒▒░░░░██████░░██████────────\n──██▓▓▓▓▓▓▒▒──░░██▓▓▒▒░░░░──██──────\n──██▓▓▓▓▒▒░░░░░░██▓▓▓▓▒▒▒▒░░██──────\n──████████████████████████████──────\n")
            
            
            await asyncio.sleep(2)

            await bot.delete_message(x8)
            await bot.delete_message(x7)
            await bot.delete_message(x6)
            await bot.delete_message(x5)
            await bot.delete_message(x4)
            await bot.delete_message(x3)
            await bot.delete_message(x2)
            await bot.delete_message(x1)

            embed2 = discord.Embed(title = "I don't reply to everyone :D" , description="<:gofight:509374882346434560>")
            xxx= await bot.edit_message(embed1, embed = embed2)
            
            emoji = get(bot.get_all_emojis(), name='plz')
            await bot.add_reaction(message= xxx, emoji = emoji)
            await bot.process_commands(message)
  else:
        True
        await bot.process_commands(message)
@commands.cooldown(1, 60, commands.BucketType.user)            
@bot.command(pass_context=True)
async def noob(ctx, message_id):
    msg = await bot.get_message(ctx.message.channel, message_id)
    emoji = get(bot.get_all_emojis(), name='Dame_Wall')
    emoji2 = get(bot.get_all_emojis(), name='Ddia_Wall')
    emoji3 = get(bot.get_all_emojis(), name='Dgold_Wall')
    emoji4 = get(bot.get_all_emojis(), name='Dstone_Wall')
    emoji5 = get(bot.get_all_emojis(), name='Dwood_Wall')
    emoji9 = get(bot.get_all_emojis(), name='haha')
    emoji10 = get(bot.get_all_emojis(), name='Dame_spike')
    emoji11 = get(bot.get_all_emojis(), name='Ddia_spike')
    emoji12 = get(bot.get_all_emojis(), name='Dgold_spike')
    emoji13 = get(bot.get_all_emojis(), name='Dstone_spike')
    emoji14 = get(bot.get_all_emojis(), name='Dwood_spike')
    emoji15 = get(bot.get_all_emojis(), name='evil')



    await bot.add_reaction(message= msg, emoji = emoji)
    await bot.add_reaction(message= msg, emoji = emoji2)
    await bot.add_reaction(message= msg, emoji = emoji3)
    await bot.add_reaction(message= msg, emoji = emoji4)
    await bot.add_reaction(message= msg, emoji = emoji5)
    await bot.add_reaction(message= msg, emoji = '🇳')
    await bot.add_reaction(message= msg, emoji = '🇺')
    await bot.add_reaction(message= msg, emoji = '🇧')
    await bot.add_reaction(message= msg, emoji = emoji9)
    await bot.add_reaction(message= msg, emoji = emoji10)
    await bot.add_reaction(message= msg, emoji = emoji11)
    await bot.add_reaction(message= msg, emoji = emoji12)
    await bot.add_reaction(message= msg, emoji = emoji13)
    await bot.add_reaction(message= msg, emoji = emoji14)
    await bot.add_reaction(message= msg, emoji = emoji15)

@commands.cooldown(1, 60, commands.BucketType.user)            
@bot.command(pass_context=True)
async def quote(ctx, msg_id):
    msg = await bot.get_message(ctx.message.channel, msg_id)
    await bot.say('{0.timestamp} - {0.content}'.format(msg))

@commands.cooldown(1, 60, commands.BucketType.user)            
@bot.command(pass_context=True)
async def bust(ctx, user: discord.Member):
    
    delta1 = datetime.timedelta(hours = 0, minutes = 30)  
    now = datetime.datetime.now()

    then = now - delta1
    counter = 0

    async for message in bot.logs_from(ctx.message.channel, limit=5, after = then):
   
       
       message = discord.utils.get(bot.messages, author = user)
       if message == None:
           async for message in bot.logs_from(ctx.message.channel, limit=10, after = then):
                message = discord.utils.get(bot.messages, author = user)
                emoji1 = get(bot.get_all_emojis(), name='stoneswordnoob')
                emoji2 = get(bot.get_all_emojis(), name='Wierdcat')
                await bot.add_reaction(message= message, emoji = '🇪')        
                await bot.add_reaction(message= message, emoji = '🇵')        
                await bot.add_reaction(message= message, emoji = '🇮')
                await bot.add_reaction(message= message, emoji = '🇨')

                await bot.add_reaction(message= message, emoji = emoji1)


                await bot.add_reaction(message= message, emoji = '🇳')
                await bot.add_reaction(message= message, emoji = '🇺')
                await bot.add_reaction(message= message, emoji = '🇧')
                await bot.add_reaction(message= message, emoji = emoji2)

       else:
        emoji1 = get(bot.get_all_emojis(), name='stoneswordnoob')
        emoji2 = get(bot.get_all_emojis(), name='Wierdcat')
        await bot.add_reaction(message= message, emoji = '🇪')        
        await bot.add_reaction(message= message, emoji = '🇵')        
        await bot.add_reaction(message= message, emoji = '🇮')
        await bot.add_reaction(message= message, emoji = '🇨')

        await bot.add_reaction(message= message, emoji = emoji1)


        await bot.add_reaction(message= message, emoji = '🇳')
        await bot.add_reaction(message= message, emoji = '🇺')
        await bot.add_reaction(message= message, emoji = '🇧')
        await bot.add_reaction(message= message, emoji = emoji2)            
bot.run(os.getenv('TOKEN'))

