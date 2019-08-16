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
        await mesaage.channel.send("xnbox 스튜디오에 있는 프로젝트를 알려드립니다.")
    if message.content.startswith("!스토어"):
        await message.channel.send("xnbox 웹페이지 스토어입니다")

    

 

client.run("NTg4NjI4NjQzMzA4MjQwODk2.XRSILA.TKUKZ2CIhDObw0BFaGS-l9hevo8")
