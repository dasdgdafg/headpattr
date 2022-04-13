import asyncio
import websockets
import random
import re

def listenForEvents(twitchusername, callback):

    async def connect():
        print("connecting to twitch...")
        uri = "wss://irc-ws.chat.twitch.tv/"
        async with websockets.connect(uri,
                                      ping_interval=20,
                                      ping_timeout=5) as websocket:
            global ws
            ws = websocket
            await ws.send("NICK justinfan%s" % int(random.random()*100000000))
            await ws.send("JOIN #%s" % twitchusername)
            print("connected to twitch")
            async for message in ws:
                await handleMessage(message)
            print("disconnected from twitch")

    async def handleMessage(message):
        m = re.match("^:([^!]+)![^ ]+ PRIVMSG #[^ ]+ :(.*)$", message)
        if m:
            callback(m.group(1), m.group(2).strip())
    asyncio.get_event_loop().create_task(connect())

