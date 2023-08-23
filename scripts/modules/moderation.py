import discord
from discord.ext import commands
from discord.commands import Option
from discord.ui import Select, View
from discord.ext.commands import MissingPermissions
from scripts.embed2 import Embed2
from scripts.sysLog import sys_LOG

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #BAN COMMAND
    @discord.slash_command(name= "ban", description= "Bans a member of the server")
    @commands.has_permissions(ban_members = True, administrator = True)
    async def ban(self, ctx, member: Option(discord.Member, description= "Who to ban?"), reason: Option(str, description= "Reason for ban?", required= False)):
        if member.id == ctx.author.id:
            await ctx.respond("You can't ban **yourself** lol")
        elif member.guild_permissions.administrator:
            await ctx.respond("LMAO why would you kick another admin...")
        else:
            if reason == None:
                reason = "None provided"
            await member.ban(reason= reason)
            await ctx.respond(f"<@{ctx.author.id}> has been banned <@{member.id}> for the following reason: \n {reason}")
            sys_LOG(f"""COMMAND: ban
        Server name: {ctx.guild.name}, ID: {ctx.guild.id}
        Channel name: {ctx.channel.name}, ID: {ctx.channel.id}
        Banned user: {member.name}, ID: {member.id}
        Sender: {ctx.author}""")
    @ban.error
    async def banerror(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.respond("Requires certain permissions.")
        else:
            await ctx.respond("Something went wrong")

    #KICK COMMAND
    @discord.slash_command(name = "kick", description= "Kicks a member of the server")
    @commands.has_permissions(kick_members= True, administrator= True)
    async def kick(self, ctx, member: Option(discord.Member, description= "Who to kick?"), reason: Option(str, description= "Reason for kick?", required= False)):
        if member.id == ctx.author.id:
            await ctx.respond("You can't kick **yourself** lol")
        elif member.guild_permissions.administrator:
            await ctx.respond("LMAO why would you ban another admin...")
        else:
            if reason == None:
                reason = "None provided"
            await member.kick(reason= reason)
            await ctx.respond(f"<@{ctx.author.id}> has been kicked <@{member.id}> for the following reason: \n {reason}")
            sys_LOG(f"""COMMAND: kick
        Server name: {ctx.guild.name}, ID: {ctx.guild.id}
        Channel name: {ctx.channel.name}, ID: {ctx.channel.id}
        Kicked user: {member.name}, ID: {member.id}
        Sender: {ctx.author}""")
    @kick.error
    async def kickerror(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.respond("Requires certain permissions.")
        else:
            await ctx.respond("Something went wrong")

def setup(bot):
    bot.add_cog(Moderation(bot))