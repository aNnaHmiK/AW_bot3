import discord
from discord.embeds import Embed
import random
import datetime


client = discord.Client()

token = "ODY0NTI1NzQyNzI1NzkxODQ0.YO2uVw.qhBnglQ6zT2HlZqrwu3jJUbXk4A"



# 정상작동 확인멘트 & 상태명 
@client.event
async def on_ready():

    print(client.user.name)
    print('애옹봇 노동해..')

    game = discord.Game('애옹 일')
    await client.change_presence(status=discord.Status.online, activity=game)


# 정보 확인
# @client.event
# async def on_message(message):
#     if message.content == "내정보":
#         user = message.author
#         date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
#         print(date)



# 지정 명령어 
@client.event
async def on_message(message):
    if message.content == "핑":
        await message.channel.send("팽~ 퐁!")

    if message.content == "애옹":
        await message.channel.send("집사가 함부로 이름을 부르다니 건방지다옹!")

    if message.content == "안녕!":
        await message.channel.send("어서와라옹")
    
    if message.content == "애옹님":
        await message.channel.send("왜 부르냐옹")

    if message.content == "주인님":
        await message.channel.send("집사야 불렀느냐옹")

# 정보 확인
    if message.content == "내정보":
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(date)


# 임베드 
    if message.content == "#명령어":
        embed = discord.Embed(title="명령어를 알려주겠다옹", description="#큐알 \n#냥이", color=0x00ff00)
        embed.add_field(name="#큐알", value ="입실과 퇴실은 필수다!", inline=True)
        embed.add_field(name="#냥이 ", value ="귀여웅 냥이", inline=False)
        embed.add_field(name="#뽑기", value ="무엇이 나올까나 ~ ", inline=True)
        embed.set_footer(text="애옹이는 놀고싶어")
        await message.channel.send(embed=embed)



# 임베드 이미지 삽입
    if message.content == "#큐알":  # 슬랙 막혀있어 이미지불러오기 실패, 디스코드 채팅채널에 선발송후 링크로 이미지 불러오기 완료
        embed = discord.Embed(title = "입실,퇴실을 꼭 확인 해주세요", description = "9시전 입실 필수", color = 0x00ff00)
        embed.set_image(url = "https://cdn.discordapp.com/attachments/864761529155977258/864761564158492682/image.png")
        await message.channel.send(embed = embed)

    if message.content == "#냥이":
        embed = discord.Embed(title = "공개된 이미지 테스트중", description = "고양이", color = 0x00ff00)
        embed.set_image(url = "https://cdn.imweb.me/upload/S201807025b39d1981b0b0/16b98d3e3d30e.jpg")
        await message.channel.send(embed = embed)






# 랜덤 대답 적용
    if message.content == "#냥이야":
        ran = random.randint(0,3)
        if ran == 0:
            d = "어디서 반말이냥"
        if ran == 1:
            d = "간식이냥?"
        if ran == 2:
            d = "귀찮다옹"
        if ran == 3:
            d = "에베베베~ 안들린다옹~"
       
        await message.channel.send(d)



















# 경고 및 벤
    # if message.content == "*경고":



# # 사진 보내기 
    # if message.content == "/사진":
    #     photo = message.content.split(" ")[1]
    #     await message.channel.send(file=discord.File(photo))

    



client.run(token)