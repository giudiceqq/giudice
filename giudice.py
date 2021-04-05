import discord 
from discord.ext import commands
import os
client = commands.Bot( command_prefix = ".")

@client.event
async def on_ready():
    print ("Bot connected")
#sostav
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def sostav(ctx):
	emb = discord.Embed(title = "**Актуальный состав семьи Giudice**", description = "Noah Giudice - Основатель Империи (1)\nJake Giudice - Лидер Империи (2)\nAberforth Giudice - Заместитель Империи (3)\nPhilipp Giudice - Заместитель Империи (4)\nJames Giudice - Империанец (5)\nWilliam Giudice - Империанец (6)\nLelouch Giudice - Империанец (7)\nCarlos Giudice - Империанец (8)\nAberforth Giudice - Империанец (9)\nGabriel Giudice - Империанец (10)\nMilton Giudice - Империанец (11)\nSanate Giudice - Империанец (12)\nLautaro Giudice - Империанец (13)\nTakeda Giudice -  Империанец (14)\nBulat Giudice - Империанец (15)\nAngel Giudice -  Империанец (16)\nPitty Giudice -  Империанец (17)\nRalph Giudice - Империанец (18)\nJordan Giudice - Империанец(19)", color = discord.Color.blue())
	await ctx.send(embed = emb)
#sostav2
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def sostav2(ctx):
	emb = discord.Embed(title="**Империанцы которые успешно отстояли посты лидера**", description = "Noah Giudice - Шеф СФПД [09.04.2020] - [09.05.2020] | Успешно\nJake Giudice - Шеф СФПД [28.05.2020] - [28.06.2020]  | Успешно\nLuke Giudice - Шериф РКШД [14.06.2020] - [15.07.2020] | Успешно\nJulia Giudice - Глав.Врач ЛВМЦ [19.06.2020] - [19.07.2020] | Успешно\nJames Giudice - Шеф СФПД [28.06.2020] - [18.07.2020] | ПСЖ\nLautaro Giudice - Упр. Изд. СФ СМИ [14.03.2021] - [Стоит]\nJake Giudice - Адмирал Армии СФ [21.03.2021] - [Стоит]",color = discord.Color.blue())
	await ctx.send(embed = emb)
#sostav3
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def sostav3(ctx):
	emb = discord.Embed(title = "**Должностные лица империи**", description = "📷Lautaro Giudice - СМИ Сан-Фиерро | 10 |\n⚔️Jake Giudice - Армия Сан-Фиерро | 10 |\n📷Aberforth Giudice - СМИ Сан-Фиерро| 9 |\n⚔️James Giudice - Тюрьма Стр. Реж| 8 |\n🔱William Giudice - Фед. Бюр. Расл. | 6 |\n⚔️Gabriel Giudice - Фед. Бюр. Расл. | 4 |\n📷Lelouch Giudice - СМИ СФ | 4 | \n⚔️Noah Giudice - Армия Сан-Фиерро | 3 |\n📷Angel Giudice - CМИ СФ| 3 |\n⚔️Philipp Giudice - Полиция Лас-Вент. | 2 |\n🚫Ralph Giudice  - None | 0 |\n🚫Milton Giudice - None | 0 |\n🚫Pitty Giudice - None | 0 |\n🚫Bulat Giudice- None | 0 |\n🚫Takeda Giudice - None | 0 |\n🚫Sanate Giudice - None | 0 |\n🚫Carlos Giudice - None | 0 |\n🚫Jordan Giudice - None | 0 |",color = discord.Color.blue())
	await ctx.send(embed = emb)
#infouser
@client.command(pass_context = True)
async def info(ctx,member:discord.Member):
	emb = discord.Embed(title = 'Информация о пользователи', description = 'Тут вы можете узнать информацию о пользователи', color = discord.Color.blue())
	emb.add_field(name = 'Дата присоединения к серверу:', value = member.joined_at,inline = False)
	emb.add_field(name = 'Имя пользователя:', value = member.display_name,inline = False)
	emb.add_field(name = 'Дата создания аккаунта Discord:', value = member.created_at.strftime("%a,%d %B %Y, %I:%M %p UTC"))

	await ctx.send(embed = emb)	
#ping
@client.command(pass_context = True)
async def ping(ctx):
	author = ctx.message.author
	emb = discord.Embed(title = "Ping", description = "Проверка бота", color = discord.Color.blue())
	emb.add_field(name = 'Pong', value = f"{author.mention}",inline = False)
	emb.set_author(name = client.user.name, icon_url = client.user.avatar_url)
	await ctx.send(embed = emb)
#clear
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def clear(ctx, amount : int):
	emb = discord.Embed(title = "Отчистка чата", color = 0xff0000)
	deleted = await ctx.message.channel.purge(limit=amount + 1)
	emb.add_field(name = f"Было удалено {amount} сообщений :bucket: ", value = "Отчистка прошла успешно!")
	await ctx.send(embed = emb)
#info bot
@client.command(pass_context = True)
async def infobot(ctx):
	emb = discord.Embed(title = "Информация о боте", description = "Тут вы можете узнать информацию о боте", color = discord.Color.blue())
	emb.add_field(name = 'Дата создания бота:', value = '05/04/2021', inline = False)
	emb.add_field(name = 'Автор бота:', value = 'Giudice#5102', inline = False)
	emb.set_author( name = client.user.name, icon_url = client.user.avatar_url)
	await ctx.send(embed = emb)
#connect 
token = os.environ.get("BOT_TOKEN")

client.run(token)