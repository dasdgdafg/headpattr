import asyncio
import websockets
import logging
import json

EVENT_START = "42[\"event\","
MESSAGE_END = "]"

ws = None

def listenForEvents(streamlabssocket, callback):

    async def connect():
        print("connecting to streamlabs...")
        uri = "wss://sockets.streamlabs.com/socket.io/?cluster=main&EIO=3&transport=websocket&token=" + streamlabssocket
        async with websockets.connect(uri,
                                      origin="https://streamlabs.com",
                                      ping_interval=20,
                                      ping_timeout=5) as websocket:
            global ws
            ws = websocket
            anyResponse = False
            async for message in ws:
                await handleMessage(message)
                if not anyResponse:
                    anyResponse = True
                    print("connected to streamlabs")

    async def handleMessage(message):
        #print(message)
        if message.startswith(EVENT_START):
            event = json.loads(message[len(EVENT_START):-len(MESSAGE_END)])
            if event["type"] == "donation":
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

