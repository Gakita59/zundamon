import discord
import magical
import schedule
from time import sleep
import threading

TOKEN = 'OTkxNjAwODE4MzI1Mjk1MTE0.G3dK14.kbMLS7elZG5Xc18MMqP2HompML_eBb1SdkBJJE'
client = discord.Client()
channel = None


async def send_message(message):
    await channel.send(message)

@client.event
async def on_ready():
    print('ログインしました')
    schedule.every(10).seconds.do(task)
    while True:
        schedule.run_pending()
        sleep(1)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content == 'ずんだもん':
        await message.channel.send('やめるのだ')
    
    if message.content == '\here':
        await message.channel.send('ここに送るのだ')
        global channel
        channel = message.channel

    if message.content == 'ずんずん':
        await send_message('なのだ')

async def task():
    elms = magical.get_elems()
    await send_message(format(elms[0]))




client.run(TOKEN)