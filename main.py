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
	role = discord.utild.get(member.guild.roles, name = "Новобранец")
	await member.add_roles(role)
# RUN
token = os.environ.get('BOT_TOKEN')

client.run(str(token))
# в config.py нужен по сути только TOKEN,но на всякий случай,пусть все остается,как есть
