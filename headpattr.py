from twitchAPI.pubsub import PubSub
from twitchAPI.twitch import Twitch
from twitchAPI.types import AuthScope
from pprint import pprint
from uuid import UUID
import asyncio

import streamelementsIntegration
import commands

#read config
twitchusername = ""
accesstoken = ""
refreshtoken = ""
clientid = ""
streamelementsjwt = ""
with open("apikeys.txt") as f:
    content = f.readlines()
for line in content:
    line = line.strip()
    if line.startswith("twitchusername"):
        twitchusername = line[len("twitchusername:"):]
    elif line.startswith("accesstoken"):
        accesstoken = line[len("accesstoken:"):]
    elif line.startswith("refreshtoken"):
        refreshtoken = line[len("refreshtoken:"):]
    elif line.startswith("clientid"):
        clientid = line[len("clientid:"):]
    elif line.startswith("streamelementsjwt"):
        streamelementsjwt = line[len("streamelementsjwt:"):]

# setting up Authentication and getting your user id
print("connecting to twitch...")
twitch = Twitch(clientid, authenticate_app=False)
twitch.set_user_authentication(accesstoken, [AuthScope.BITS_READ, AuthScope.CHANNEL_READ_SUBSCRIPTIONS, AuthScope.CHANNEL_READ_REDEMPTIONS], refreshtoken)
user_id = twitch.get_users(logins=[twitchusername])['data'][0]['id']

# starting up PubSub
pubsub = PubSub(twitch)
pubsub.start()
pubsub.listen_channel_points(user_id, commands.pointCallback)
pubsub.listen_channel_subscriptions(user_id, commands.subCallback)
pubsub.listen_bits(user_id, commands.bitCallback)
print("connected to twitch")

streamelementsIntegration.listenForEvents(streamelementsjwt, commands.streamelementsTipCallback)

# read actions from the queue, then wait for them to finish
async def doActions():
    while True:
        action = await commands.actionQueue.get()
        wait = action()
        if wait:
            await asyncio.sleep(wait)
asyncio.get_event_loop().create_task(doActions())

asyncio.get_event_loop().run_forever()

#pubsub.unlisten(uuid)
pubsub.stop()

