import asyncio
import websockets
import logging
import json

EVENT_START = "42[\"event\","
AUTHENTICATED_START = "42[\"authenticated\","
MESSAGE_END = "]"

ws = None

def listenForEvents(jwtToken, callback):

    async def connect():
        print("connecting to streamelements...")
        uri = "wss://realtime.streamelements.com/socket.io/?cluster=main&EIO=3&transport=websocket"
        async with websockets.connect(uri,
                                      origin="https://streamelements.com",
                                      ping_interval=20,
                                      ping_timeout=5) as websocket:
            global ws
            ws = websocket
            await ws.send("420[\"overlay:ping\",{\"source\":\"other\"}]")
            await ws.send("42[\"authenticate\", {\"method\":\"jwt\",\"token\":\"%s\"}]" % jwtToken)
            async for message in ws:
                await handleMessage(message)

    async def handleMessage(message):
        #print(message)
        if message.startswith(AUTHENTICATED_START):
            msg = json.loads(message[len(AUTHENTICATED_START):-len(MESSAGE_END)])
            await ws.send("421[\"subscribe\",{\"room\":\"kvstore::%s\",\"reconnect\":false}]" % msg["channelId"])
            print("connected to streamelements")
        if message.startswith(EVENT_START):
            event = json.loads(message[len(EVENT_START):-len(MESSAGE_END)])
            if event["type"] == "tip":
                callback(event)

    async def sendPings():
        while True:
            await asyncio.sleep(20)
            await ws.send("2")
            
    #logger = logging.getLogger('websockets')
    #logger.setLevel(logging.DEBUG)
    #logger.addHandler(logging.StreamHandler())

    asyncio.get_event_loop().create_task(sendPings())
    asyncio.get_event_loop().create_task(connect())

