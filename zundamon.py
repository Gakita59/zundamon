import discord
from discord.ext import tasks
import magical

TOKEN = 'OTkxNjAwODE4MzI1Mjk1MTE0.GsAN-7.gieyVasoMQSaHLTdy3EFwtsvrujcVWA1srh0RM'
client = discord.Client()
channel = None
previous_elms = [['a','a']]


async def init_embed():
    embed = discord.Embed(
        title = 'しんちゃくチケットなのだ！',
        color=0x00ff00,
        url = "https://cloak.pia.jp/resale/item/list?areaCd=&prefectureCd=&hideprefectures=01&perfFromDate=&perfToDate=&numSht=&priceFrom=&priceTo=&eventCd=2209305%2C2209306%2C2209307&perfCd=&rlsCd=&lotRlsCd=&eventPerfCdList=&stkStkndCd=&stkCliCd=&invalidCondition=&preAreaCd=&prePrefectureCd=&totalCount=40&beforeSearchCondition=%7B%22event_cd%22%3A%222209305%2C2209306%2C2209307%22%2C%22sort_condition%22%3A%22perf_date_time%2Casc%22%2C%22page%22%3A1%7D&ma_token=96r4j5mxIQ6JnHd&sortCondition=entry_date_time%2Cdesc"
    )
    embed.add_field(name='',value='')
    return embed


async def send_embed(embed,elm):
    embed.set_field_at(0,name=elm[0],value=elm[1])
    await channel.send(embed=embed)

async def catch_new_ticket(elms):
    if elms[0] == previous_elms[0]:
        return False
    elif len(previous_elms) > 1 and elms[0] == previous_elms[1]:
        return False
    else:
        return True


@tasks.loop(seconds=1)
async def task(embed):

    elms = magical.get_elems()

    try:
        print(elms[0])
        if await catch_new_ticket(elms):
            await send_embed(embed,elms[0])
            print('embed sended!!')
            if '札幌' in elms[0][0]:
                await send_message('@everyone さっぽろのチケットなのだ！はやくとるのだ！！')
        global previous_elms
        previous_elms = elms

    except IndexError:
        pass
    

async def send_message(message):
    await channel.send(message)

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content == 'ずんだもん':
        await message.channel.send('はいなのだ！')

    if message.content == 'おはよう':
        await message.channel.send(message.author.display_name + 'さん！おはようなのだ！')
    
    if message.content == '\start':
        await message.channel.send('しんちゃくチケットがあったらここにおくるのだ')
        global channel
        channel = message.channel
        embed = await init_embed()
        task.start(embed)

    if message.content == '\stop':
        task.cancel()
        await message.channel.send('やめるのだ')

    if message.content == '\prev':
        await message.channel.send('previous_elmsの値は')
        await message.channel.send(previous_elms)
        await message.channel.send('なのだ')


client.run(TOKEN)