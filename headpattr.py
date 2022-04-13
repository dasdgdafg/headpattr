from pprint import pprint
from uuid import UUID
import asyncio

import pomfIntegration
##import twitchIntegration
import commands

#read config
twitchusername = ""
pomfusername = ""
with open("apikeys.txt") as f:
    content = f.readlines()
for line in content:
    line = line.strip()
    if line.startswith("twitchusername"):
        twitchusername = line[len("twitchusername:"):]
    elif line.startswith("pomfusername"):
        pomfusername = line[len("pomfusername:"):]

if twitchusername:
    twitchIntegration.listenForEvents(twitchusername, commands.messageCallback)
else:
    print("skipping twitch, twitchusername was blank")

if pomfusername:
    pomfIntegration.listenForEvents(pomfusername, commands.messageCallback)
else:
    print("skipping pomf, pomfusername was blank")

# read actions from the queue, then wait for them to finish
async def doActions():
    while True:
        action = await commands.actionQueue.get()
        wait = action()
        if wait:
            await asyncio.sleep(wait)
asyncio.get_event_loop().create_task(doActions())

asyncio.get_event_loop().run_forever()


