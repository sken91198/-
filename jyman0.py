import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("�α��� ��...")
    print(client.user.name)
    print(client.user.id)
    print("================")
    

@client.event
async def on_message(message):
    if message.content.startswith("!�ȳ�"):
        await message.channel.send("�ȳ�! �� �ؿ����̾�!")
        await message.channel.send("�ʿ��Ѱ� �ִٸ� !�� ������ �Է�����!")      
    if message.content.startswith("!����"):
        await message.channel.send("���� ��������!")
        await message.channel.send("�����!!!!!!!!!!")
        await message.channel.send("����� �����ڴ� jyman0�Դϴ�.")                                                                  
    if message.content.startswith("!�ٺ�"):
        await message.channel.send("��!")                                  
    if message.content.startswith("!�̽��Ϳ���"):
        await message.channel.send("��...���� ����.")
        await message.channel.send("������ �����ڴ� ������?")                                
    if message.content.startswith("!��û��"):
        await message.channel.send("��!")
    if message.content.startswith("!����"):
        await message.channel.send("����? ���̰� ����? �Դ°ǰ�?")
        await message.channel.send("������: 12���Դϴ�.")
        await message.channel.send("����!")
    if message.content.startswith("!������"):
        await message.channel.send("jyman0 �Դϴ�.")
    if message.content.startswith("!����"):
        await message.channel.send("�׷��� �� �߿���!")
    if message.content.startswith("!�޷�"):
        await message.channel.send("��!")
    if message.content.startswith("!��"):
        await message.channel.send("��! ����! ���Ƿ罺!")
        await message.channel.send("��~ ������� �ƽô±���~")
        await message.channel.send("����� ��.��.��.��.��.��.��.")
        await message.channel.send(".. ��� �ϳ׿�")
    if message.content.startswith("!����"):
        await message.channel.send("����~")
    if message.content.startswith("!�Ǹ�"):
        await message.channel.send("�װ� �ٷ� &*^*^*&*&(�Ը���)")
    if message.content.startswith("!jyman0"):
        await message.channel.send("jyman0: �� �ҷ����?")
    if message.content.startswith("!���"):
        await message.channel.send("��������! ���� ����̴� (���)")
    if message.content.startswith("!��Ʋ�׶���"):
        await message.channel.send("��������! ���� ����̴� (���)")
    if message.content.startswith("!���κ���Ľ�"):
        await message.channel.send("�װ� ����?")
    if message.content.startswith("!����"):
        await message.channel.send("�װ� ����?")
    if message.content.startswith("!����"):
        await message.channel.send("����--!!!")
    if message.content.startswith("!�ܺ�ĭ�ø���"):
        await message.channel.send("a���� ���ϱ� b������ c���� ��Ÿ���..")
    if message.content.startswith("?")
        await message.channel.send("����....")
    if message.content.startswith("!���")
        await message.channel.send("������! �̻���� ���� ���������� ������ ������ �Ƽ���!")
    if message.content.startswith("!�Ұ�")
        await message.channel.send("��..�����Դϴ�")


        
access_token = os.environ["BOT_TOKEN"]    
client.run(access_token)