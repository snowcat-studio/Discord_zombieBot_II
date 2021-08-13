import discord
from discord.ext import commands
 
token = "token here"
app = commands.Bot(command_prefix='!')

@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=discord.Game("반갑습니다 :D")) # dnd: 다른 용무중, idle: 자리비움

@app.command(name='날씨')
async def 날씨(message):
    await message.send("오늘 날씨는 화창합니다.🌞")

@app.command(name= "마감")
async def 마감독촉(message):
    await message.send("마감하십쇼 --")

@app.command(name='인사해봐')
async def 인사(message):
    embed = discord.Embed(title='안녕하세요. 좀비봇II입니다.',description='저는 좀비가 만든 디스코드 봇 2세입니다.\n아래에서 제 명령어를 확인할 수 있습니다.',
    color = 0x00ff00)
    #Embed 기본틀 (메인 제목, 설명, 컬러)
    embed.add_field(name="`!날씨`",value='날씨 정보를 알려드립니다.', inline=False)
    embed.add_field(name='`!인사해봐`',value='인사와 함께 기본적인 명령어를 알려드립니다.', inline=False)
    embed.add_field(name='`!마감`',value='마감하십쇼', inline=False)
    embed.set_footer(text='2021.08.13')
    await message.send(embed = embed)
     
app.run(token)