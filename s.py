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

    game = discord.Game("아무것도 안")

    await client.change_presence(status=discord.Status.online, activity=game)



@client.event

async def on_message(message):
    if message.content == ("/scommand"):
        embed = discord.Embed(title="오늘급식", description="녹두밥\n한방닭곰탕5.6.13.15.\n언양식치즈떡갈비2.5.6.10.13.\n브로콜리숙회5.6.\n섞박지9.\n마카롱1.2.6.", color=0x00ff00)
        await message.channel.send(embed=embed)

client.run('Nzg4Nzk3ODI5NTc3MTc5MTY5.X9ovOQ.-tFEqzs3j4QQhRRT8sCd46Z4188')
