import keyboard
import other_keyboard
from uuid import UUID
import asyncio
import winsound

actionQueue = asyncio.Queue()
def q(action):
    actionQueue.put_nowait(action)

def sound(filename):
    winsound.PlaySound(filename, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)

# queue up your custom actions in these callbacks with the q function, like q(myAction)
# refer to the Twitch/Streamelements documentation for more details on the available data in each callback

def streamelementsTipCallback(event: dict) -> None:
    data = event["data"]
    print("%s tipped %.2f %s" % (data["username"], data["amount"], data["currency"]))
    q(mediumHeadpat)

def streamlabsTipCallback(event: dict) -> None:
    data = event["message"][0]
    print("%s tipped %s" % (data["from"], data["formatted_amount"]))
    q(mediumHeadpat)

def bitCallback(uuid: UUID, response: dict) -> None:
    data = response["data"]
    print("got %d bits from %s" % (data["bits_used"], data["user_name"]))
    if data["bits_used"] >= 1000:
        q(longHeadpat)
    elif data["bits_used"] >= 200:
        q(mediumHeadpat)
    else:
        q(shortHeadpat)

def subCallback(uuid: UUID, response: dict) -> None:
    data = response["data"]
    if "display_name" in data["message"]:
        print("sub from %s" % (data["message"]["display_name"]))
    else:
        print("unknown sub")
    q(mediumHeadpat)

def pointCallback(uuid: UUID, response: dict) -> None:
    data = response["data"]
    print("%s redeemed %s" % (data["redemption"]["user"]["display_name"], data["redemption"]["reward"]["title"]))
    # adjust the title here to match the one set in twitch
    if data["redemption"]["reward"]["title"] == "Headpat":
        q(mediumHeadpat)


# define your custom actions here
# return the number of seconds to wait after the action before the next action can happen
# only .wav files are supported for sounds

def shortHeadpat():
    sound("short sound.wav")
    keyboard.press_and_release('ctrl+a')
    return 1

def mediumHeadpat():
    sound("medium sound.wav")
    other_keyboard.PressAndRelease('b')
    return 2

def longHeadpat():
    sound("long sound.wav")
    other_keyboard.PressAndRelease('f12')
    return 5

