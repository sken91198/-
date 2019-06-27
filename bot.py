import discord

client = discord.Client()

@client.event
async def on_ready():
    print('접속 중입니다')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
    await client.change_presence(game=discord.Game(name="서버 지키미v 1.0", type=1))    




@client.event
async def on_message(message):
    

 

client.run("NTg4NjI4NjQzMzA4MjQwODk2.XRSILA.TKUKZ2CIhDObw0BFaGS-l9hevo8")
