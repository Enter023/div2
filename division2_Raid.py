import discord
import pytz
import datetime
import time
from time import time

client = discord.Client()
TOKEN='Njc3NDk0Nzk4MjIyODg0ODc0.XlEpdw.JXVWCqWXMP2Ud988qjrxI6dgQfg'
CANNEL_ID=677489467409563661


@client.event
async def on_ready():
    print('ログインしました')
    print('division2_Raid')
    print('-----------------')
    channel = client.get_channel(CANNEL_ID)
    while 1:
        timedate = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
        now = timedate.strftime('%H:%M:%S')
        daydate = datetime.date.today().weekday()
        print(now)
        if daydate==5:
         if now == '21:00:00':
                msg = await channel.send('定期レイド　日曜日\n朝の部　9：00（◀) 夜の部　20:00(▶)\nリアクションにて返事お願いします')
                await msg.add_reaction( '◀')
                await msg.add_reaction( '▶')  
        if daydate==6:
            if now == '09:00:00':
                msg = await channel.send('定期レイド　朝の部を始めます\n参加者はレイドVCまで')
    
            if now == '21:00:00':
                msg = await channel.send('定期レイド　夜の部を始めます\n参加者はレイドVCまで')
        
client.run(TOKEN)