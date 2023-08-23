import discord, random
from discord.ext import commands
from discord.commands import Option
from scripts.embed2 import Embed2
from scripts.sysLog import sys_LOG

autoresponses = {}

class AutoResponder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #MESSAGE RESPONDER
    @discord.Cog.listener()
    async def on_message(self, message):
        messageUF = message.content
        #A couple of changes so it's readable
        unwanted_chars = ["'", "!", ",", "?", " "]
        message.content = "".join([char for char in message.content if char not in unwanted_chars])
        message.content = message.content.lower()

        if not message.author == self.bot.user:

            #AUTOMATED MESSAGE RESPONDER
            for guild in autoresponses:
                for responder in autoresponses[guild]:
                    if autoresponses[guild][responder]["enabled"] == True:
                        if message.content in autoresponses[guild][responder]["triggers"]:
                                if len(autoresponses[guild][responder]["responses"]) > 1:
                                    await message.channel.send(random.choice(autoresponses[guild][responder]["responses"]))
                                else:
                                    await message.channel.send(autoresponses[guild][responder]["responses"][0])
    
    #AUTORESPONDER ADD
    @discord.slash_command(name= "autoresponder_add", description= "Create a new autoresponder")
    @commands.has_permissions(administrator= True)
    async def autoresponder_add(self, ctx,
        respondername: Option(str, description= "Enter name for this autoresponder (must be unique)"),
        triggers: Option(str, description= "Enter all trigger words, split with comma (,). The bot ignores case-sensitivity, special characters."),
        responses: Option(str, description= "What message to respond with. If multiple, responses will be random.")):
            #Converting inputs into a list
            triggersList = triggers.split(",")
            responseList = responses.split(",")
            triggersList = [word.strip() for word in triggersList]
            responseList = [word.strip() for word in responseList]
            autoresponses[ctx.guild.id] = {respondername: {"enabled": True, "triggers": triggersList, "responses": responseList}}
    
            embed = Embed2(ctx= ctx,
                 title= "Autoresponder Module", description= f"New autoresponder **{respondername}** successfully created.")
            embed.add_field(title= "Triggers:", content= autoresponses[ctx.guild.id][respondername]["triggers"])
            embed.add_field(title= "Responses:", content= autoresponses[ctx.guild.id][respondername]["responses"])

            await ctx.respond(embed= embed.Embed)
            
    #AUTORESPONDER TOGGLE
    @discord.slash_command(name= "autoresponder_toggle", description= "Enable/Disable autoresponders")
    @commands.has_permissions(administrator= True)
    async def autoresponder_toggle(self, ctx, respondername: Option(str, description= "Enter name of autoresponder")):
        if autoresponses[ctx.guild.id][respondername]["enabled"] == False:
            autoresponses[ctx.guild.id][respondername]["enabled"] = True

            embed = Embed2(ctx= ctx,
                title= "Autoresponder Module", description= f"**{respondername}** now enabled.")

            await ctx.respond(embed= embed.Embed)
        else:
            autoresponses[ctx.guild.id][respondername]["enabled"] = False

            embed = Embed2(ctx= ctx,
                title= "Autoresponder Module", description= f"**{respondername}** now disabled.")

            await ctx.respond(embed= embed.Embed)  
        
    #AUTORESPONDER EDIT
    @discord.slash_command(name= "autoresponder_edit", description= "Edit an existing autoresponder. Any edits overwrites the previous ones.")
    @commands.has_permissions(administrator= True)
    async def autoresponder_edit(self, ctx,
        respondername: Option(str, description= "Name of the autoresponder"),
        triggers: Option(str, description= "Enter all trigger words, split with comma (,). The bot ignores case-sensitivity, special characters.", required= False),
        responses: Option(str, description= "What message to respond with. If multiple, responses will be random.", required= False)):

            #Checking things
            if not triggers == None:
                #Converting inputs into a list
                triggersList = triggers.split(",")
                triggersList = [word.strip() for word in triggersList]

                autoresponses[ctx.guild.id][respondername]["triggers"] = triggersList
        
            if not responses == None:
                #Converting inputs into a list
                responseList = responses.split(",")
                responseList = [word.strip() for word in responseList]

                autoresponses[ctx.guild.id][respondername]["responses"] = responseList
            
            embed = Embed2(ctx= ctx,
                 title= "Autoresponder Module", description= f"Changes made to the **{respondername}** autoresponder:")
            embed.add_field(title= "Triggers:", content= autoresponses[ctx.guild.id][respondername]["triggers"])
            embed.add_field(title= "Responses:", content= autoresponses[ctx.guild.id][respondername]["responses"])

            await ctx.respond(embed= embed.Embed)

    #AUTORESPONDER DEL
    @discord.slash_command(name= "autoresponder_delete", description= "Delete an autoresponder.")
    @commands.has_permissions(administrator= True)
    async def autoresponder_del(self, ctx,
        respondername: Option(str, description= "Name of the autoresponder")):
            del autoresponses[ctx.guild.id][respondername]

            embed = Embed2(ctx= ctx,
                 title= "Autoresponder Module",
                 description= f"Successfully deleted the autoresponder **{respondername}**.")
            
            await ctx.respond(embed= embed.Embed)

#COGS SETUP FOR BOT
def setup(bot):
    bot.add_cog(AutoResponder(bot))