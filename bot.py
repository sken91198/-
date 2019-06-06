import discord
import asyncio
import random


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
    if message.content.startswith('!소개'):
        await client.send_message(message.channel, '코리아 리얼리티서버의 방패가 되겠습니다')
        await client.send_message(message.channel, '에드온 문의는 서버 총관리자님에게 문의 바랍니다')
    if message.content.startswith('!도움'):
        await client.send_message(message.channel, '모든 명령어는!로 시작해야 합니다')
        await client.send_message(message.channel, '현제 명령어 작업중입니다')
    if message.content.startswith('!명령어 목록'):
        await client.send_message(message.channel, '()!소개 #이 명령어를 쓰면 이 봇이 어떤 봇인지 말해줍니다')
        await client.send_message(message.channel, '()!모두 #이 명령어를 쓰면 전체를 호출합니다')
    if message.content.startswith('ㅎㅇ'):
        await client.send_message(message.channel, ':regional_indicator_h: :regional_indicator_i:')
    if message.content.startswith('!모두'):
    	roll = '@everyone {0.author.mention}님이 여러분을 부릅니다'.format(message)
    	await client.send_message(message.channel, roll)
    if message.content.startswith('!스켄도움말'):
        await client.send_message(message.channel, '????????????????????????unknown??????????????????????????????????????????????????????unknown?????????????????????????????????????unknown???????????????????????unknown')
    if message.content.startswith('!안티버스 프로그램'):
        await client.send_message(message.channel, '온라인 여부 확인중:온라인')
        await client.send_message(message.channel, '중립화 여부 확인중:온라인')
        await client.send_message(message.channel, '안랩,ip접속 받아오기:확인')
        await client.send_message(message.channel, '서버 통신:좋음')
        await client.send_message(message.channel, '인터넷 여부 확인중:온라인')
        await client.send_message(message.channel, '안티버스 프로그램:오프라인')
        await client.send_message(message.channel, 'ip받아오는중.................:192.168.0.7')
        await client.send_message(message.channel, '동적 IP:122.255.123.236')
        await client.send_message(message.channel, '안티버스 프로그램 가동:온라인 안전하고 즐거운 하루 보내십시오')

 

client.run("NTY1NDE0MjMwMDIzNjAyMTc2.XPiOXg.mAiijvjTijKDubuEKY3_8ybungo")
