import discord
from discord.ext import commands
from discord.commands import Option
from scripts.embed2 import Embed2

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #GREET
    @discord.slash_command(name="greet", description= "Greet someone!")
    async def greet(self,ctx, name: Option(str, "What sentence bruh")):
        await ctx.respond(f"ok this is a test {name}")
    
    #MEMBERCOUNT
    @discord.slash_command(name= "membercount", description= "Tells you how many members does this server has")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def membercount(self, ctx):
        MemberCountEmbed = Embed2(ctx=ctx, title= "Membercount", description= f"Members: {ctx.guild.member_count}", log=True)
        await ctx.respond(embed=MemberCountEmbed.Embed)
    @membercount.error
    async def membercounterror(self, ctx, error):
        await ctx.respond(error)

    #USER DETAILS
    @discord.slash_command(name= "user_info", description= "Gets the info of a user in the server")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def userinfo(self, ctx, user: Option(discord.Member, "Username to get info of")):
        embed = Embed2(ctx= ctx,
            title= f"{user.name}'s info",
            description= f"Well we fetched some stuff we know about the mentioned user and here it is!")
        embed.add_field(title= "Username:", content= f"{user.name}")
        embed.add_field(title= "Display name:", content= f"{user.display_name}")
        embed.add_field(title= "Nickname:", content= f"{user.nick}")
        embed.add_field(title= "ID: ", content= f"{user.id}")
        embed.add_field(title= "User created on: ", content= f"{user.created_at}")

        await ctx.respond(embed=embed.Embed)
        print(dir(ctx.user))

    #SERVER DETAILS
    @discord.slash_command(name= "server_info", description= "Fetch the info of this server")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def serverinfo(self, ctx):
        embed = Embed2(ctx= ctx,
            title= f"Server info",
            description= f"""Server info for {ctx.guild.name}. We know it aint much lol""")
        embed.add_field(title= "Name:", content= f"{ctx.guild.name}")
        embed.add_field(title= "Server ID:", content= f"{ctx.guild.id}")
        embed.add_field(title= "Owner:", content= f"{ctx.guild.owner}")
        embed.add_field(title= "Membercount:", content= f"{ctx.guild.member_count}")
        embed.add_field(title= "Created on:", content= f"""{ctx.guild.created_at.strftime("%Y-%m-%d %H:%M:%S")}""")

        await ctx.respond(embed=embed.Embed)
        print(ctx.guild.channels)
    
    #PING BOT
    @discord.slash_command(name= "ping", description= "Ping the bot to check the latency")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def ping(self, ctx):
        embed = Embed2(ctx= ctx, title= "Ping Bot", description= f"Latency: {round(self.bot.latency * 1000)}ms")

        await ctx.respond(embed=embed.Embed)

    #CHANNELS
    @discord.slash_command(name= "channels", description= "Output all the channels in this server")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def channels(self, ctx, channel: Option(discord.TextChannel, description= "Select a specific channel", required= False)):
        await ctx.respond("This command is being tested.")
        print(channel)

def setup(bot):
    bot.add_cog(Greetings(bot))