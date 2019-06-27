import discord

client = discord.Client()

@client.event
async def on_ready():
    print('접속 중입니다')
    print(client.user.name)
    print(client.user.id)




@client.event
async def on_message(message):
    if message.content.startswith("!소개"):
        await mesaage.channel.send("windows 디팬더에 있는 기능들입니다.
    

    

 

client.run("NTg4NjI4NjQzMzA4MjQwODk2.XRSILA.TKUKZ2CIhDObw0BFaGS-l9hevo8")
