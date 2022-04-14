import asyncio
import websockets
import json
import random

def listenForEvents(pomfusername, callback):

    async def connect():
        print("connecting to pomf...")
        uri = "wss://pomf.tv/websocket/"
        async with websockets.connect(uri,
                                      origin="https://pomf.tv",
                                      ping_interval=20,
                                      ping_timeout=5) as websocket:
            await websocket.send("{\"roomId\":\"%s\",\"userName\":\"Guest_%s\",\"apikey\":\"Guest\",\"action\":\"connect\"}" % (pomfusername, int(random.random()*100000000)))
            print("connected to pomf")
            async for message in websocket:
                await handleMessage(message)
            print("disconnected from pomf")

    async def handleMessage(message):
        event = json.loads(message)
        if "type" in event and event["type"] == "message":
            callback(event["from"]["name"], event["message"].strip())

    asyncio.get_event_loop().create_task(connect())

