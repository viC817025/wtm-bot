import discord
from discord.ext import commands

intents = discord.Intents.all()




bot = commands.Bot(command_prefix= '[',intents = intents) #建置BOT prefix命令字首



token = 'OTgwMDUzMTM1NjMwNDMwMjE4.G9Ty_t.YS0BugK6wxjlq13ACYnIPd2FrVm-I1MBwV4lkQ'

@bot.event
async def on_ready():
    print("BOT is online <<")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(726636844913262675)
    await channel.send(F'{member} 加入了肥宅群!!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(726636844913262675)
    await channel.send(F'{member} 離開了...')


bot.run(token)
