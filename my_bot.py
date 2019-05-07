import discord
import os
 
client = discord.Client()
 
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_member_join(member):
        role = ""
        for i in message.server.roles:
            if i.name == "트수단!":
                role = i
                break
        await client.add_roles(member, role)

 
@client.event
async def on_message(message):
    if message.content.startswith('!테스트'):
        await client.send_message(message.channel, '삐빕-봇 테스트 중입니다.(inpo:온라인 여부 확인중:ONLINE 체팅 확인:N/A 체팅 확인:ONLINE 즐거운 하루 보내십시오)')
    if message.content.startswith('!H.E.V작동 여부'):
        await client.send_message(message.channel, 'H.E.V:H.E.V 마크 4 보호복을 이용해 주셔서 감사합니다 온라인 작동 여부 확인중 입니다......AUTO madi madicool systeam:online voice systeam:online HUD screen system:online screen systeam:online 온라인 여부 확인:온라인 안전하고 즐거운 하루 보내십시오')
    if message.content.startswith('!타입'):
        await client.send_message(message.channel, '1.평화 2.펑!')
    if message.content.startswith('헐 진짜요?'):
        await client.send_message(message.channel, '나 부름??')
    if message.content.startswith('!빠루맨'):
        await client.send_message(message.channel, '나임 고든 프리맨')
    if message.content.startswith('!고든'):
        await client.send_message(message.channel, '프리맨')
    if message.content.startswith('!낚시'):
        await client.send_message(message.channel, '아호호아 삐------치이이이이이 콤바인 이즈 데드 3.2.1 콤바인 이즈 데드')

    if message.content.starswith("!역할설정"):
        role = ""
        rolename = message.content.split(" ")
        member = discord.utils.get(client.get_all_members(), id=rolenmae[1])
        for i in message.server.roles:
            if i.name == rolename[2]:
                role = i
                break
        await client.add_roles(member, role)


access_token = os.en/iron["BOT_TOTKEN"]
client.run('eccess_tocen')
