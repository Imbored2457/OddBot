import discord
from discord.ext import commands
import config
import os
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Bot online!")


@bot.command()
async def load(ctx, extension):
    if ctx.author.id == '866285734808780812':
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f"Loaded Cog: {extension}")
    else:
        await ctx.send('Only the owner of the bot can run this command.')

@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == '866285734808780812':
        bot.unload_extension(f'cogs.extension')
        await ctx.send(f'Unloaded Cog: {extension}')
    else:
        await ctx.send('Only the owner of the bot can run this command.')

@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == '866285734808780812':
        bot.reload_extension(f'cogs.{extension}')
        await ctx.send(f'Reloaded Cog: {extension}')
    else:
        await ctx.send('Only the owner of the bot can run this command.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print("Loaded Cogs.")
    else:
        print("Failed to load __pycache__")

bot.run(config.token)