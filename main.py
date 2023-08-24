import discord, wikipedia, os, random, time
from discord import Option
from discord.ui import Select, View
from discord.ext import commands
from discord.ext.commands import MissingPermissions
from dotenv import load_dotenv
from datetime import datetime

from scripts.embed2 import Embed2
from scripts.sysLog import sys_LOG

print("""
The Måtta (Legacy) Discord Bot

GitHub:
- LEGACY: https://github.com/luqmanity/matta-legacy
- NEW: https://github.com/luqmanity/matta
      
Join The Discord Server for support, updates, etc:
- https://discord.gg/7w8b6MMXBy\n""")

if not os.path.exists(".env"):
    print("""
Missing .env file, which must contain
TOKEN = <your bot token> in order to operate
          
Refer to the README.md on the GitHub repo for more info.""")
    
else:

    load_dotenv()

    if __name__ == "__main__":
        #ENV token
        TOKEN = str(os.getenv("token"))

        bot = discord.Bot(intents= discord.Intents.all())

        #STARTUP
        startup_time = time.time()
        
        @bot.event
        async def on_ready():
            await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.playing, name= "Hej då! /help"))
            sys_LOG(f"{bot.user} is online, took {round(time.time() - startup_time, 4)}s", "status")

        #COGS - Refer scripts folder 
        bot.load_extension("scripts.modules.help")
        bot.load_extension("scripts.modules.moderation")
        bot.load_extension("scripts.modules.messaging")
        bot.load_extension("scripts.modules.tools")

        #COOLDOWN MANAGEMENT
        @bot.event
        async def on_application_command_error(ctx, error):
            if isinstance(error, commands.CommandOnCooldown):
                await ctx.send(error)
            else:
                raise error

        bot.run(TOKEN)