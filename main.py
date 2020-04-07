import os
import random
import discord
import dictionary
from discord import utils
from discord.ext import commands
# импорт библиотек

# client
client = commands.Bot(command_prefix='.')

# auto-role
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, id = int("689396798879563843"))
    await member.add_roles(role)

# goodbye
@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, id = int("582894293551677451"))
    await channel.send(f"{member} 𝐥𝐞𝐟𝐭 𝐮𝐬 𝐟𝐨𝐫 𝐚𝐧 𝐮𝐧𝐤𝐧𝐨𝐰𝐧 𝐫𝐞𝐚𝐬𝐨𝐧 :(")

# clearing
@client.command()
async def cl(ctx, n = 3):
    if n > 100:
        await ctx.send('Слишком большое число')
    else:
        await ctx.channel.purge(limit = n)

# o/r game
@client.command()
async def c(ctx, *, args):
    if args == random.choice(coin_vars := ['орел','решка']):
        await ctx.send('Да! Правильный ответ: ' + args)
    elif args not in coin_vars:
        await ctx.send('Напиши нормальный вариант')
    else:
        await ctx.send('Неа...Подкинь еще раз')

# ask game
@client.command()
async def ag(ctx, *, args):
    if (ecx := len(list(args))) < 3:
        await ctx.send("Напиши нормальный вопрос")
    else:
        await ctx.send('Твой вопрос: ' + args + '\nОтвет: ' + random.choice(dictionary.answers))

# help
@client.command()
async def h(ctx):
    await ctx.send(dictionary.helping)

# information
@client.command()
async def i(ctx):
    await ctx.send(dictionary.info)

# whois
@client.command()
async def w(ctx):
    await ctx.send(dictionary.who_am_i)

# RUN
token = os.environ.get('BOT_TOKEN')
client.run(str(token))
