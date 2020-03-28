import discord
from discord import utils
from discord.ext import commands
import os

import config # импорт библиотек


client = commands.Bot(command_prefix = '.')

# @client.event
# async def on_ready():
# 	print('Im ready') не обязательно

# команда для очистки чата
@client.command()
async def clear(ctx, num = 5):
	await ctx.channel.purge(limit = num)

# авто-роль
@client.event
async def on_member_join(member):
	role = 689396798879563843
	await member.add_roles(role)

# # no more 1 role
# @client.event
# async def on_member_update(before, after):

# 	if (len(after.roles)) > 1:
# 		member = discord.utils.get(after.guild.members)
# 		await member.remove_roles()

# RUN

Привет, WRIV!

token = os.environ.get('BOT_TOKEN')

# в config.py нужен по сути только TOKEN,но на всякий случай,пусть все остается,как есть
