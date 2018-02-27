import discord
import asyncio

client = discord.Client()


@client.event
async def on_ready():
    print('Login to ' + client.user.name)
    print('User_ID ' + client.user.id)
    print('Hello_Discord!')

@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("Hello"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # Write↓
            m = "Hellooow" + message.author.name
            # Send to
            await client.send_message(message.channel, m)
            

client.run("Your_Token")
