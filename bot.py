import discord
import asyncio
import os
import sys

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("しね"):
        # 送り主がBotだった場合反応したくないので
      for var in range(0, 10):
        if client.user != message.author:
            # メッセージを書きます
            m = "FuckYou!!!" + message.author.name
            n = "FuckYou!!!" + message.author.name
            o = "FuckYou!!!" + message.author.name
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await client.send_message(message.channel, m)
            await client.send_message(message.channel, n)
            await client.send_message(message.channel, o)

@client.event
async def on_message(message):
    if message.content.startswith("こまんどいち"):
        await client.send_message(message.channel, 'Say hello')
        msg = await client.wait_for_message(author=message.author, content='hello')
        await client.send_message(message.channel, 'Hello.')


@client.event
async def on_message(message):
   
    if message.content.startswith("cmd2"):
        # 送り主がBotだった場合反応したくないので
      
        if client.user != message.author:
            await client.kick(member)



client.run("Your_Token")