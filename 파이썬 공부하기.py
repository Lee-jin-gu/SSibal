import discord

import os

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

    game = discord.Game("GitHub_Lee-jin-gu")

    await client.change_presence(status=discord.Status.online, activity=game)

@client.event

async def on_message(message):
    if message.content.startswith("/급식"):

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

        site1 = site1.replace('[', '')

        site1 = site1.replace(']', '')

        site1 = site1.replace('<br/>', '\n')

        site1 = site1.replace('<td class="textC last">', '')

        site1 = site1.replace('<td class="textC">', '')

        site1 = site1.replace('</td>', '')

        site1 = site1.replace('amp;', '')

        print(site1)

        print('site2')

        embed = discord.Embed(title="급식", description="", color=0x00ff00)

        embed.add_field(name="오늘급식", value=f"{site1}", inline=True)

        await message.channel.send(embed=embed)
        
access_token = os.environ["BOT_TOKEN"]
client.run('access_token')
