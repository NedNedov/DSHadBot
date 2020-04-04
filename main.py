import os
import discord
from discord import utils
from discord.ext import commands
import random
import requests
import bs4
import COVID19Py
# импорт библиотек

def up_cr(self):
	self.ncov19 = COVID19Py.COVID()
	
	self.latest = self.ncov19.getLatest()
	self.location = self.ncov19.getLocationByCountryCode()
	
	self.final_confirmed = f"Заболевших: {location[0]['latest']['confirmed']}"
	self.final_deaths = f"Смертей: {location[0]['latest']['deaths']}"

# client

client = commands.Bot(command_prefix='.')

# команда для очистки чата

@client.command()
async def clear(ctx, num=5):
    await ctx.channel.purge(limit=num)

# coronainfo

@client.command()
async def corona(ctx, *, args):	
	if args == 'азер':
		up_cr.self.location = self.ncov19.getLocationByCountryCode(str(args))
		await ctx.send(up_cr.self.final_confirmed + "\n" + up_cr.self.final_deaths)
		

# авто-роль

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, id=int("689396798879563843"))
    await member.add_roles(role)

# прощание

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(
        member.guild.channels, id=int("582894293551677451"))
    await channel.send(f"{member} 𝙡𝙚𝙛𝙩 𝙪𝙨! 𝘽𝙮𝙚 𝘽𝙮𝙚...")

# орел/решка игра

@client.command()
async def coin(ctx, args):
    variants = ['Орёл', 'Решка']
    if args == 'орел' or 'орёл':
        await ctx.send('Правильный ответ: ' + random.choice(variants))
    elif args == 'решка':
        await ctx.send('Правильный ответ: ' + random.choice(variants))

# представление

@client.command()
async def who(ctx):
    await ctx.send("Я Rudolf Hadler, помощник и бот на этом сервере.Всем хорошего дня и побед в играх!")

# помощь

@client.command()
async def helping(ctx, args):

    if args == 'server':
        await ctx.send("Для информации насчет ботов перейдите в Help. Для получения информации о каком-то канале,после комнады напиши назвние канала.")
    elif args == 'chat':
        await ctx.send("Этот канал для общения и разговоров")
    elif args == 'news':
        await ctx.send("Тут переодически появляются новости сервера")
    elif args == 'cheats':
        await ctx.send("Тут обмен читов для CS:GO")
    elif args == 'disscusion-cheats':
        await ctx.send("Тут обсуждение читов для CS:GO")
    elif args == 'help':
        await ctx.send("Это канал для получения информации о сервере")
    elif args == 'musicselect':
        await ctx.send("Канал для выбора песни для MusicRoom1")


# информация

@client.command()
async def info(ctx):
    await ctx.send("На этом дискорд сервере ты встретишь дружелюбных и адекватных людей,хорошую администрацию,Музыкального Бота и другое(над сервером ведётся работа,если есть идеи пишите а ЛС в Discord 𝓝𝓮𝓭_𝓝𝓮𝓭𝓸𝓿#2686)")

# да/нет игра

@client.command()
async def askg(ctx, *,args):
	answers = ['Да','Возможно','Нет','Вероятнее всего','Может быть','Определённо нет','Определённо да']
	await ctx.send("Твой вопрос: " + args + "\nОтвет: " + random.choice(answers))


# RUN
token = os.environ.get('BOT_TOKEN')
client.run(str(token))
