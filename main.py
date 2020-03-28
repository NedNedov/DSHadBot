import discord
from discord import utils
from discord.ext import commands
import os
# импорт библиотек


client = commands.Bot(command_prefix = '.')

# команда для очистки чата
@client.command()
async def clear(ctx, num = 5):
	await ctx.channel.purge(limit = num)

# авто-роль
@client.event
async def on_member_join(member):
	role = discord.utils.get(member.guild.roles, id=int("689396798879563843"))
	await member.add_roles(role)

# прощание
@client.event
async def on_member_remove(member):
	channel = discord.utils.get(member.guild.channels, id=int("582894293551677451"))
	await channel.send(f"{member} left us.Goodbye")
	
# RUN
token = os.environ.get('BOT_TOKEN')

client.run(str(token))
# в config.py нужен по сути только TOKEN,но на всякий случай,пусть все остается,как есть
