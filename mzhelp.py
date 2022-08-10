helpcmdz = {
    'meme': "Generates a random meme from reddit.",
    'donate': "Donate me pls",
    'nitro': "Generates a random nitro code.",
    'dice': "Rolls random dice.",
    'credits': "Shows credits.",
    'ticket': "Opens a ticket.",
    ('delete', 'tclose', 'tdelete'): "Deletes the current channel. This command was originally intended for deleting a ticket.",
    'afk': "AFK command. Upon activation, whenever someone pings you, they will be notified that you are AFK.",
    ('about', 'info'): "Shows information about the bot.",
    'ping': "Shows the network latency.",
    'updates': "Shows the latest update logs.",
    'dmnitro': "DMs you any amount of nitro codes.",
    ('membercount', 'mc'): "Shows the member count of the server.",
    ('snipe', 'sniper'): "Snipes a recently deleted message.",
    ('editsnipe', 'esnipe'): "Edit snipes a recently edited message.",
    ('dw'): "{For giveaways only} how a drop works. **Requires Permission(s): Manage Server**",
    'mute': "Mutes a member. **Requires Permission(s): Manage Server**",
    'unmute': "Unmutes a member. **Requires Permission(s): Manage Server**",
    'nuke': "Nukes the channel and creates a clone of it. **Requires Permission(s): Administrator**",
    'kick': "Kicks a member. **Requires Permission(s): Kick Members**",
    'ban': "Bans a member. **Requires Permission(s): Ban Members**",
    'unban': "Unbans a member. **Requires Permission(s): Ban Members**",
    'gg': "{For giveaways only} GG, stay in that server. **Requires Permission(s): Manage Server**",
    'tips': "{For giveaways only} Tips to win giveaways! **Requires Permission(s): Manage Server**",
    'claimed': "Logs a member's claim in claim logs. **Requires Permission(s): Administrator**",
    'setclaimschannel': "Sets claim channel for this server. **Requires Permission(s): Administrator**",
    'won': "{For giveaways only} Shows who won last giveaway. **Requires Permission(s): Manage Server**",
    'setproofschannel': "Set proof channel for won command. **Requires Permission(s): Administrator**",
    'spam': "'Spams' a certain amount of the same message in the current channel. **Requires Permission(s): Administrator**",
    'dmspam': "Spams a certain amount of the same message... But in someone's DMs. You can opt out of this by using '.optout_spam'. **Requires Permission(s): Administrator**",
    'dmspam_force': "FORCE DM spams someone regardless of whether they opted out! **Requires Permission(s): Administrator**",
    'lockall': "MASS LOCKDOWNS all the channels. Use with caution! **Requires Permission(s): Manage Channels**",
    'slowmode': "Sets the slowmode. **Requires Permission(s): Manage Channels**",
    'purge': "Purges messages. Avoids pinned messages. **Requires Permission(s): Manage Messages**",
    ('timer', 'countdown'): "Sets a countdown timer. **Requires Permission(s): Administrator**",
    ('whois', 'memberinfo'): "Checks a member's info such as role, avatar, permissions, and join date.",
    ('type', 'typing'): "Get the bot to type for a certain amount of time, or infinitely.",
    ('stoptype', 'stoptyping'): "Get the bot to stop typing. Due to API limitations, this command will not be activated instantly.",
    ('music', 'play', 'song'): "Plays a certain song. The bot will automatically join the voice channel you're in.",
    ('leave', 'disconnect'): "Leaves the voice channel that the bot is currently in.",
    ('continue', 'resume'): "Resumes playing music.",
    'pause': "Pauses the music that is currently playing.",
    ('skip', 'stop'): "Skips the music that is currently playing.",
    ('serverinfo', 'whereami'): "Gets information about the current server.",
    ('ruser', 'robloxaccount', 'robloxacc', 'racc', 'getruser', 'getrobloxuser', 'getrobloxacc', 'robloxuser'): "Gets information about a Roblox user.",
    'gstart': "Starts a giveaway.",
    'greroll': "Rerolls a giveaway.",
    'gend': "Ends a giveaway.",
    ('grerollc', 'rerollc', 'reroll_c'): "Rerolls a giveaway in compatible mode with other bots.",
    ('lastmention', 'recentmention', 'mentionmsg', 'msgmention'): "Fetches the most recent mention of you."
}

helpusage = {
    'meme': "`.meme`",
    'donate': "`.donate`",
    'nitro': "`.nitro`",
    'dice': "`.dice <amount> <number of sides>`",
    'credits': "`.credits`",
    'ticket': "`.ticket`",
    ('delete', 'tclose', 'tdelete'): "`.delete|tclose|tdelete`",
    'afk': "`.afk [reason='AFK']`",
    ('about', 'info'): "`.about|info`",
    'ping': "`.ping`",
    ('updates', 'update'): "`.updates|update`",
    'dmnitro': "`.dmnitro <amount>`",
    ('membercount', 'mc'): "`.membercount|mc`",
    ('snipe', 'sniper'): "`.snipe [index]`",
    ('editsnipe', 'esnipe'): "`.editsnipe|esnipe [index]`",
    ('dw'): "`.dw`",
    'mute': "`.mute <discord.Member>`",
    'unmute': "`.unmute <discord.Member>`",
    'nuke': "`.nuke`",
    'kick': "`.kick <discord.Member> [reason=None]`",
    'ban': "`.ban <discord.Member> [reason=None]`",
    'unban': "`.unban <User's Name + Discrim>`",
    'gg':"`.gg <server name>`",
    'tips': "`.tips`",
    'claimed': "`.claimed <discord.Member> <name>`",
    'setclaimschannel': "`.setclaimschannel <mention channel|channel ID>`",
    'won': "`.won <discord.Member> <name>`",
    'setproofschannel': "`.setproofschannel <mention channel|channel ID>`",
    'spam': "`.spam <number of times> <message>`",
    'dmspam': "`.dmspam <number of times> <discord.Member> <message>`",
    'dmspam_force': "`.dmspam_force <number of times> <discord.Member> <message>`",
    'lockall': "`.lockall`",
    'slowmode': "`.slowmode <seconds>`",
    'purge': "`.purge <limit>`",
    ('timer', 'countdown'): "`.timer|countdown <duration> [name=None]`",
    ('whois', 'memberinfo'): "`.whois|memberinfo <discord.Member>`",
    ('type', 'typing'): "`.type|typing [duration=None]`",
    ('stoptype', 'stoptyping'): "`.stoptype|stoptyping`",
    ('music', 'play', 'song'): "`.music|play|song <YouTube URL|Song Name>`",
    ('leave', 'disconnect'): "`.leave|disconnect`",
    ('continue', 'resume'): "`.continue|resume`",
    'pause': "`.pause`",
    ('skip', 'stop'): "`.skip|stop`",
    ('serverinfo', 'whereami'): "`.serverinfo|whereami`",
    ('ruser', 'robloxaccount', 'robloxacc', 'racc', 'getruser', 'getrobloxuser', 'getrobloxacc', 'robloxuser'): ""
                                                                                                                "`.robloxuser|ruser|robloxacc|... <Roblox user ID>`",
    'gstart': "`.gstart <duration> <number of winners> [prize='<undefined>']`",
    'greroll': "`.greroll <message ID>`",
    'gend': "`.gend <message ID>`",
    ('grerollc', 'rerollc', 'reroll_c'): "`.grerollc|rerollc|reroll_c <message ID>`",
    ('lastmention', 'recentmention', 'mentionmsg', 'msgmention'): "`.lastmention|recentmention|... [limit=10000]`"
}

