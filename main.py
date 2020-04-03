import discord
from discord import utils
from discord.ext import commands
import os
import random
# импорт библиотек

client = commands.Bot(command_prefix = '.')

# команда для очистки чата
@client.command()
async def clear(ctx, num = 5):
	await ctx.channel.purge(limit = num)
	
# авто-роль
@client.event
async def on_member_join(member):
	role = discord.utils.get(member.guild.roles, id = int("689396798879563843"))
	await member.add_roles(role)
	
# прощание
@client.event
async def on_member_remove(member):
	channel = discord.utils.get(member.guild.channels, id=int("582894293551677451"))
	await channel.send(f"{member} 𝙡𝙚𝙛𝙩 𝙪𝙨! 𝘽𝙮𝙚 𝘽𝙮𝙚...")

@client.command()
async def coin(ctx, args):
	variants = ['орел','решка']
	if args == 'орел':
		await ctx.send('Правильный ответ: ' + random.choice(variants))
	elif args == 'решка':
		await ctx.send('Правильный ответ: ' + random.choice(variants))

@client.command()
async def helping(ctx, args):
	if args == '':
		await ctx.send("Для информации насчет ботов перейдите в #Information.Для получения информации о каком-то канале,после комнады напиши назвние канала.")
	elif args == '📃𝓒𝓗𝓐𝓣📃':
		await ctx.send("Этот канал для общения и разговоров")
	elif args == '📣𝕹𝖊𝖜𝖘📢':
		await ctx.send("Тут переодически появляются новости сервера")
	elif args == '💻👨🏽🅲🅷🅴🅰🆃🆂👨🏽💻':
		await ctx.send("Тут обмен читов для CS:GO")
	elif args == '🗣ᴅɪsᴄᴜssɪᴏɴ-ᴄʜᴇᴀᴛs🗣':
		await ctx.send("Тут обсуждение читов для CS:GO")
	elif args == '𝕀𝕟𝕗𝕠𝕣𝕞𝕒𝕥𝕚𝕠𝕟💭':
		await ctx.send("Это канал для получения информации о сервере")
	elif args == 'musicselect':
		await ctx.send("Канал для выбора песни для MusicRoom1")	
	
# информация
@client.command()
async def info(ctx):
	await ctx.send("На этом дискорд сервере ты встретишь дружелюбных и адекватных людей,хорошую администрацию,Музыкального Бота и другое(над сервером ведётся работа,если есть идеи пишите а ЛС в Discord 𝓝𝓮𝓭_𝓝𝓮𝓭𝓸𝓿#2686)")
	
# RUN
token = os.environ.get('BOT_TOKEN')
client.run(str(token))
