import discord

import asyncio

import datetime

import calendar

import requests

from bs4 import BeautifulSoup

client = discord.Client()

@client.event

async def on_ready():

    print(client.user.id)

    print("ready")

    game = discord.Game("/명령어")

    await client.change_presence(status=discord.Status.online, activity=game)



@client.event

async def on_message(message):
    if message.content == ("/명령어"):
        embed = discord.Embed(title="명령어 목록", description="/급식\n/내일급식\n/모래급식", color=0x00ff00)
        await message.channel.send(embed=embed)


    if message.content==("/급식"):

        a = message.content[4:]

        def get_html(url):

            _html = ""

            resp = requests.get(url)

            if resp.status_code == 200:

                _html = resp.text

            return _html

        today = datetime.datetime.today()

        sibal = str(today.strftime("%Y.%m.%d"))

        local_weekday = today.weekday() + 1

        html = get_html(f'https://stu.sen.go.kr/sts_sci_md01_001.do?schulCode=B100000659&schulCrseScCode=4&schulKndScCode=04&schYmd={sibal}')

        soup = BeautifulSoup(html, 'html.parser')

        site = soup.find_all("tr")

        site = site[2].find_all("td")

        site1 = site[local_weekday]

        site1 = str(site1)

        site1 = site1.replace('<br/>', '\n').replace('<td class="textC">', '').replace('</td>', '').replace('<td class="textC last">', '')

        print(site1)

        embed = discord.Embed(title="오늘 급식", description="급식이 없습니다!" if site1 == " " else "", color=0x00ff00)

        if site1 != " ":
            embed.add_field(name="급식", value=f"{site1}", inline=True)

        await message.channel.send(embed=embed)

    if message.content==("/내일급식"):
        
        a = message.content[4:]

        def get_html(url):

            _html = ""

            resp = requests.get(url)

            if resp.status_code == 200:

                _html = resp.text

            return _html

        today = datetime.datetime.today()

        sibal = str(today.strftime("%Y.%m.%d"))

        local_weekday = today.weekday() + 2

        html = get_html(f'https://stu.sen.go.kr/sts_sci_md01_001.do?schulCode=B100000659&schulCrseScCode=4&schulKndScCode=04&schYmd={sibal}')

        soup = BeautifulSoup(html, 'html.parser')

        site = soup.find_all("tr")

        site = site[2].find_all("td")

        site1 = site[local_weekday]

        site1 = str(site1)

        site1 = site1.replace('<br/>', '\n').replace('<td class="textC">', '').replace('</td>', '').replace('<td class="textC last">', '')

        print(site1)

        embed = discord.Embed(title="내일급식", description="급식이 없습니다!" if site1 == " " else "", color=0x00ff00)

        if site1 != " ":
            embed.add_field(name="내일급식", value=f"{site1}", inline=True)

        await message.channel.send(embed=embed)

    if message.content==("/모래급식"):
        
        a = message.content[4:]

        def get_html(url):

            _html = ""

            resp = requests.get(url)

            if resp.status_code == 200:

                _html = resp.text

            return _html

        today = datetime.datetime.today()

        sibal = str(today.strftime("%Y.%m.%d"))

        local_weekday = today.weekday() + 3

        html = get_html(f'https://stu.sen.go.kr/sts_sci_md01_001.do?schulCode=B100000659&schulCrseScCode=4&schulKndScCode=04&schYmd={sibal}')

        soup = BeautifulSoup(html, 'html.parser')

        site = soup.find_all("tr")

        site = site[2].find_all("td")

        site1 = site[local_weekday]

        site1 = str(site1)

        site1 = site1.replace('<br/>', '\n').replace('<td class="textC">', ' ').replace('</td>', '').replace('<td class="textC last">', '')

        print(site1)

        embed = discord.Embed(title="모래급식", description="급식이 없습니다!" if site1 == " " else "", color=0x00ff00)

        if site1 != " ":
            embed.add_field(name="모래급식", value=f"{site1}", inline=True)

        await message.channel.send(embed=embed)





    if message.content.startswith("!추천인 @민구"):
        await message.channel.send("추천인해주셔서 감사합니다")





    if message.content.startswith("!채팅청소"):
        if message.author.guild_permissions.manage_messages:
            try:
                amount = message.content[6:]
                await message.channel.purge(limit=int(amount))
                await message.channel.send(f"**{amount}**개의 메시지를 지웠습니다.")
            except ValueError:
                await message.channel.send("청소하실 메시지의 **수**를 입력해 주세요.")
        else:
            await message.channel.send("권한이 없습니다.")

client.run('token')
