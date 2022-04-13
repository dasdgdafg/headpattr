# based on the example code from https://buttplug-py.docs.buttplug.io/
from buttplug.client import (ButtplugClientWebsocketConnector, ButtplugClient,
                             ButtplugClientDevice, ButtplugClientConnectorError)
import asyncio

client = None

def device_added(emitter, dev: ButtplugClientDevice):
    print("Device found: ", dev)

def device_removed(emitter, dev: ButtplugClientDevice):
    print("Device removed: ", dev)

async def connect():
    global client
    print("connecting to intiface...")

    # First, we'll need to set up a client object. This is our conduit to the
    # server.
    # We create a Client object, passing it the name we want for the client.
    # Names are shown in things like the Intiface Desktop Server GUI.
    client = ButtplugClient("headpattr")
    connector = ButtplugClientWebsocketConnector("ws://127.0.0.1:12345")

    # This connector will connect to Intiface Desktop on the local machine,
    # using the default port for insecure websockets.
    # There's one more step before we connect to a client, and that's
    # setting up an event handler.
    client.device_added_handler += device_added
    client.device_removed_handler += device_removed

    # Whenever we connect to a client, we'll instantly get a list of devices
    # already connected (yes, this sometimes happens, mostly due to windows
    # weirdness). We'll want to make sure we know about those.
    # Finally, we connect.
    try:
        await client.connect(connector)
    except ButtplugClientConnectorError as e:
        print("Could not connect to intiface server, is it running? {}".format(e.message))
        client = None
        return

    # Now we move on to looking for devices.
    # This will tell the server to start scanning for devices, and returns
    # while it's scanning. If we get any new devices, the device_added_task
    # function that we assigned as an event handler earlier will be called.
    await client.start_scanning()

async def vibrate(intensity):
    global client
    if client == None:
        await connect()
    if client != None:
        if len(client.devices) == 0:
            print("Warning: attempting to vibrate, but no devices found")
        for d in client.devices.values():
            if "VibrateCmd" in d.allowed_messages.keys():
                d.send_vibrate_cmd(intensity)
            else:
                print("Warning: attempting to vibrate, but device does not support vibration", d)

