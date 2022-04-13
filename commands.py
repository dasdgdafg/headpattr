import keyboard
from uuid import UUID
import asyncio
import time

try: #these 2 only work on windows
    import other_keyboard
    import winsound
except:
    pass

actionQueue = asyncio.Queue()
def q(action):
    actionQueue.put_nowait(action)

def sound(filename):
    winsound.PlaySound(filename, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)

userTimes = {}
globalTime = 0
def messageCallback(user: str, message: str) -> None:
    global userTimes
    global globalTime
    t = time.time()

    # shared cooldown, only do 1 command every this many seconds, change to 0 to disable
    if t - globalTime < 5: 
        return

    # per user cooldown, change to 0 to disable
    if user in userTimes and t - userTimes[user] < 60: 
        return

    # Add more commands here
    # copy the `globalTime = t` and `userTimes[user] = t` lines if you want the cooldown to work
    # queue up your custom actions in these callbacks with the q function, like q(myAction)
    # for actions that take arguments, do it like q(lambda: myAction(arg))
    if message == "!headpat":
        globalTime = t
        userTimes[user] = t
        q(shortHeadpat)
    elif message == "!headpat-twice":
        globalTime = t
        userTimes[user] = t
        q(shortHeadpat)
        q(shortHeadpat)
    elif message == "!headpaaat":
        globalTime = t
        userTimes[user] = t
        q(longHeadpat)

# define your custom actions here
# return the number of seconds to wait after the action before the next action can happen
# only .wav files are supported for sounds

def shortHeadpat():
    sound("short sound.wav")
    keyboard.press_and_release('shift+a')
    return 1

def longHeadpat():
    sound("long sound.wav")
    other_keyboard.PressAndRelease('f12')
    return 5

