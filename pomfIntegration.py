import asyncio
import websockets
import json
import random

ws = None

def listenForEvents(pomfusername, callback):

    async def connect():
        print("connecting to pomf...")
        uri = "wss://pomf.tv/websocket/"
        async with websockets.connect(uri,
                                      origin="https://pomf.tv",
                                      ping_interval=20,
                                      ping_timeout=5) as websocket:
            global ws
            ws = websocket
            await ws.send("{\"roomId\":\"%s\",\"userName\":\"Guest_%s\",\"apikey\":\"Guest\",\"action\":\"connect\"}" % (pomfusername, int(random.random()*100000000)))
            print("connected to pomf")
            async for message in ws:
                await handleMessage(message)

    async def handleMessage(message):
        event = json.loads(message)
        if event["type"] == "message":
            callback(event["from"]["name"], event["message"].strip())

    asyncio.get_event_loop().create_task(connect())

