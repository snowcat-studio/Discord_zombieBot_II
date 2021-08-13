import discord
from discord.ext import commands
 
app = commands.Bot(command_prefix='!')
 
@app.command(name='오늘날씨')
async def 따라하기(ctx):
    await ctx.send("오늘 날씨는 화창합니다.🌞")

@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=None)     
     
app.run('token here')