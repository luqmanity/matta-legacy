import discord
from scripts.sysLog import sys_LOG

class Embed2():
    def __init__(self, ctx, title, description=None, color=None, log=None):
        self.Embed = discord.Embed(
            title="Default title",
            description="Default description",
            color=discord.Color.from_rgb(255, 255, 255)
        )
        self.Embed.clear_fields()  # Clear existing fields

        self.Embed.title = title
        if description is not None:
            self.Embed.description = description
        if color is not None:
            self.Embed.color = color

        if log:
            sys_LOG(f"""
        Server name: {str(ctx.guild.name)}, ID: {ctx.guild.id}
        Channel name: {str(ctx.channel.name)}, ID: {ctx.channel.id}
        Sender: {str(ctx.author)}""", type=title)

    def add_field(self, title, content=None, inline=None):
        if inline is None:
            inline = False
        if content is None:
            content = "No contents specified."
        self.Embed.add_field(name=title, value=content, inline=False)
    
    def set_footer(self, text):
        if text == "NY":
            text = "Regal Discord Bot - Developed by Nytra-Designed."
        self.Embed.set_footer(text= text)

    def set_image(self, url):
        self.Embed.set_image(url= url)