import discord
from discord.ext import commands
from datetime import datetime
today = datetime.today()

class kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        embed = discord.Embed(title="Member Kicked Successfully!", color=discord.Color.green())
        embed.add_field(name="Member Username", value=f"{member.mention}", inline=False)
        embed.add_field(name="Reason", value=f"{reason}", inline=False)
        embed.add_field(name="Date", value=f"{today}", inline=False)
        await ctx.send(embed=embed)
        memberEmbed = discord.Embed(title="You have been kicked!", description=f"Guild: {ctx.guild.name}", color=discord.Color.red())
        memberEmbed.add_field(name="Staff Member Username", value=f"{ctx.author.mention}", inline=False)
        memberEmbed.add_field(name="Reason", value=f"{reason}", inline=False)
        memberEmbed.add_field(name="Date", value=f"{today}", inline=False)
        try:
            await member.send(embed=memberEmbed)
            await member.kick()
        except commands.NoPrivateMessage:
            await ctx.send("This user has there dms on private. They have not been told that they have been kicked.")
            await member.kick()

def setup(bot):
    bot.add_cog(kick(bot))