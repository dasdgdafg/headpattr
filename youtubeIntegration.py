from pytchat import LiveChatAsync
import pytchat
import asyncio
import re
import httpx

## The pytchat library requires an old version of the httpx library
## If you get weird errors, make sure version 0.18.2 of httpx is installed (pip install httpx==0.18.2)

def listenForEvents(youtubeusername, callback):
    async def connect():
        print("connecting to youtube...")
        async with httpx.AsyncClient() as client:
            r = await client.get("https://www.youtube.com/c/%s/live" % youtubeusername)
        m = re.findall('rel="canonical" href="https://www\\.youtube\\.com/watch\\?v=([^"]+)"', r.text)

        if len(m) > 0:
            print("found youtube video: https://www.youtube.com/watch?v=%s" % m[0])
        else:
            print("no livestream found for https://www.youtube.com/c/%s/" % youtubeusername)
            return

        # the `interruptable` parameter seems to do the reverse of what it says
        # when true it catches SIGINT and keeps going,
        # but when false SIGINT will actually stop the program
        livechat = LiveChatAsync(m[0], interruptable = False, callback = func)
        print("connected to youtube")
        while livechat.is_alive():
            await asyncio.sleep(1)

        print("disconnected from youtube")

    async def func(chatdata):
        for c in chatdata.items:
            callback(c.author.name, c.message.strip())
            await chatdata.tick_async()

    asyncio.get_event_loop().create_task(connect())

