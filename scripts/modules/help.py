import discord
from discord.ext import commands
from discord.ui import Select
from scripts.embed2 import Embed2

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #/HELP COMMAND
    @discord.slash_command(name= "help", description= f"Get help from Måtta")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help(self,ctx):
        embed = Embed2(ctx=ctx,
            title = f"**{self.bot.user.name}** | Help",
            description=f"""
    **HOME**
    Regal is all you need to start, manage and grow your servers,
    whilst equipped with a wide arsenal of tools and features.

    Join our Discord Server:
    > https://discord.gg/7w8b6MMXBy

    View features and it's commands, usages using the menus below!""", 
            color=discord.Color.from_rgb(204,204,255))
        embed.add_field(
            title= "🤔 How to change settings for individuals?",
            content= "This feature is coming soon.")
        select = Select(
            placeholder= "Select a category...",
            options=[ #Menu options
            discord.SelectOption(label= "Home", emoji= "🏠"),
            discord.SelectOption(label= "Moderation", emoji= "⚒️"),
            discord.SelectOption(label= "Auto-responders", emoji= "🤖"),
            discord.SelectOption(label= "Tools", emoji= "🔨"),
            discord.SelectOption(label= "General Settings", emoji= "⚙️")
        ])
        embed.set_footer("NY")

        class View(discord.ui.View):
            async def on_timeout(self):
                self.disable_all_items()

        view = View(timeout=10)

        async def response(interaction):
            #HOME
            if select.values[0] == "Home":
                embed = Embed2(ctx=ctx,
            title = f"**{self.bot.user.name}** | Help",
            description=f"""
**HOME**
Måtta (Swedish for "Moderation") is all you need to start, manage and grow your servers,
whilst equipped with a wide arsenal of tools and features.

Join our Discord Server for support, updates, and everything else:
> https://discord.gg/7w8b6MMXBy

    View features and it's commands, usages using the menu below!""",
    color=discord.Color.from_rgb(204,204,255))
                embed.add_field(
                    title= "🤔 How to change settings for individuals?",
                    content= "This feature is coming soon.")
                embed.set_footer(text= "NY")
                await interaction.response.edit_message(embed=embed.Embed)

            #MODERATION
            if select.values[0] == "Moderation":
                embed = Embed2(ctx= ctx,
                    title= f"**{self.bot.user.name}** | Help",
                    description= """
    **MODERATION**
    Tools and commands that helps with server management and control!""",
    color= discord.Color.from_rgb(204,204,255))
                embed.add_field(title= "/kick", content= "Kicks a user in this server")
                embed.add_field(title= "/ban", content= "Bans a user in this server")

                embed.set_footer(text= "NY")
                await interaction.response.edit_message(embed=embed.Embed)
                
            #AUTO-RESPONDERS
            if select.values[0] == "Auto-responders":
                embed = Embed2(ctx= ctx,
                    title= f"**{self.bot.user.name}** | Help",
                    description= """
    **AUTO-RESPONDERS**
    Messages that the bot will send after a trigger message is sent.""",
    color= discord.Color.from_rgb(204,204,255))
                embed.add_field(
                    title= "/autoresponder_add",  content="""
                    Create a new autoresponder, simply add triggers and responders.""")
                embed.add_field(
                    title= "/autoresponder_toggle", content="""
                    Toggles an existing autoresponder.""")
                embed.add_field(
                    title= "/autoresponder_edit", content="""
                    Overwrites existing settings of an autoresponder""")
                embed.add_field(
                    title= "/autoresponder_delete", content= """
                    Deletes an existing autoresponder. **CANNOT** be undone.""")
                
                embed.set_footer(text= "NY")
                await interaction.response.edit_message(embed= embed.Embed)
            
            if select.values[0] == "Tools":
                embed = Embed2(ctx= ctx,
                    title= f"**{self.bot.user.name}** | Help",
                    description= """
    **TOOLS**
    Somewhat useful tools for the server I guess""")
                embed.add_field(title= "/membercount", content= """
Gets the membercount of the server.""")
                embed.add_field(title= "/server_info", content= """
General info about the server.""")
                embed.add_field(title= "/user_info", content= """
General info of a user.""")
                
                embed.set_footer(text= "NY")
                await interaction.response.edit_message(embed=embed.Embed)
            else:
                pass

        select.callback = response
        view.add_item(select)
        await ctx.respond(embed=embed.Embed, view=view)

def setup(bot):
    bot.add_cog(Help(bot))