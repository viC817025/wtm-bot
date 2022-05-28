import discord
from discord.ext import commands
import json
import random





from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('G:\\user\\Documents\\GitHub\\wtm-bot\\serviceAccount.json')
firebase_admin.initialize_app(cred)
# 初始化firestore

doc = {
  'name': "帽子哥",
  'email': "abc@gmail.com"
}

db = firestore.client()

doc_ref = db.collection("user")

doc_ref.add(doc)

with open ('setting.json',mode = 'r',encoding='utF8') as jFile:
    jdata = json.load(jFile)

intents = discord.Intents.all()




bot = commands.Bot(command_prefix= '!',intents = intents) #建置BOT prefix命令字首





@bot.event
async def on_ready():
    print("BOT is online <<")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['MAIN_CHANNEL']))
    await channel.send(F'{member} 加入了肥宅群!!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['MAIN_CHANNEL']))
    await channel.send(F'{member} 離開了...')


@bot.command()
async def 安尼亞(ctx):
    random_pic = random.choice(jdata['anya'])
    pic = discord.File(random_pic)
    await ctx.send(file = pic)

@bot.command()
async def 救救我(ctx):
    await ctx.send('指令專區:\n延遲 : 查看目前延遲\n安尼亞 : 傳送安尼亞圖片')

@bot.command()
async def 低能(ctx):
    await ctx.send('你才低能 7414')

bot.run(jdata['TOKEN'])
