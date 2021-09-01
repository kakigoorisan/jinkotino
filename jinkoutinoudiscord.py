from discord import channel, client
import pya3rt
import discord
import requests
import botcommands

TOKEN = "Please Write Your TOKEN Here"
setchannelid = 0

diclient = discord.Client() 

jinkou = 0

def send_message(message):
    apikey = ""
    client = pya3rt.TalkClient(apikey)
    reply_message = client.talk(message)
    return reply_message["results"][0]["reply"]

@diclient.event
async def on_ready():
    print ("起動しました")
    message = "こんにちは"
    reply = send_message(message)
    print(reply)

@diclient.event
async def on_message(dimessage):
    global setchannelid
    if dimessage.channel.id != setchannelid and setchannelid != 0:
        return
    
    global jinkou

    print (jinkou)

    if dimessage.author.bot:
        return
    
    if dimessage.content == ".setchannelid":
        setchannelid = dimessage.channel.id
        
    if jinkou == 0 and dimessage.content == ".talks":
        print(dimessage.content)

        jinkou = 1

        print(jinkou)
        await dimessage.channel.send("会話を開始します")
        
    if dimessage.content == (".help"):
        await dimessage.channel.send(".talks :会話を開始 \n .talke :会話を終了 \n .help :これを表示.")

    if jinkou == 1 and dimessage.content != ".talks" and dimessage.content != ".talke" and dimessage.content != ".help":    
        message = dimessage.content
        reply = send_message(message)
        await dimessage.channel.send(f"{dimessage.author.mention}" + reply)

    if jinkou == 1 and dimessage.content == ".talke":
        await dimessage.channel.send("会話を停止します")

        jinkou = 0

    


diclient.run(TOKEN)
