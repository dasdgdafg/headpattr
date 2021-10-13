from twitchAPI.pubsub import PubSub
from twitchAPI.twitch import Twitch
from twitchAPI.types import AuthScope
from pprint import pprint
from uuid import UUID
import asyncio

import streamelementsIntegration
import streamlabsIntegration
import pomfIntegration
import commands

#read config
twitchusername = ""
accesstoken = ""
refreshtoken = ""
clientid = ""
streamelementsjwt = ""
streamlabssocket = ""
pomfusername = ""
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
    elif line.startswith("streamlabssocket"):
        streamlabssocket = line[len("streamlabssocket:"):]
    elif line.startswith("pomfusername"):
        pomfusername = line[len("pomfusername:"):]

# setting up Authentication and getting your user id
if twitchusername and accesstoken and refreshtoken and clientid:
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
else:
    print("skipping twitch, at least one of [twitchusername accesstoken refreshtoken clientid] was blank")

if streamelementsjwt:
    streamelementsIntegration.listenForEvents(streamelementsjwt, commands.streamelementsTipCallback)
else:
    print("skipping streamelements, streamelementsjwt was blank")

if streamlabssocket:
    streamlabsIntegration.listenForEvents(streamlabssocket, commands.streamlabsTipCallback)
else:
    print("skipping streamlabs, streamlabssocket was blank")

if pomfusername:
    pomfIntegration.listenForEvents(pomfusername, commands.pomfCallback)
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

#pubsub.unlisten(uuid)
pubsub.stop()

