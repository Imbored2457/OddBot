import discord
from discord.ext import commands
from datetime import datetime
today = datetime.today()

class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
       
    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        embed = discord.Embed(title="Member Succsessfully Banned.", color=discord.Color.green())
        embed.add_field(name="Member Username", value=f"{member.mention}", inline=False)
        embed.add_field(name="Reason", value=f"{reason}", inline=False)
        embed.add_field(name="Date", value=f"{today}", inline=False)
        await ctx.send(embed=embed)
        memberEmbed = discord.Embed(title="You Have Been Banned.", color=discord.Color.red())
        memberEmbed.add_field(name="Staff Member Username", value=f"{ctx.author.mention}", inline=False)
        memberEmbed.add_field(name="Reason", value=f"{reason}", inline=False)
        memberEmbed.add_field(name="Date", value=f"{today}", inline=False)
        try:
            await member.send(embed=memberEmbed)
            await member.ban(reason=reason)
        except:
            await ctx.send("The user has there dms set to private. They have not been told that they have been banned.")
            await member.ban(reason=reason)

def setup(bot):
    bot.add_cog(ban(bot))