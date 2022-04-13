import keyboard
from uuid import UUID
import asyncio
import time
import re

try: #these 2 only work on windows
    import other_keyboard
    import winsound
except:
    pass

try:
    import buttplugIntegration
except:
    pass

actionQueue = asyncio.Queue()
def q(action):
    actionQueue.put_nowait(action)

def sound(filename):
    winsound.PlaySound(filename, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)

def vibrate(intensity):
    asyncio.run(buttplugIntegration.vibrate(intensity))

def sleep(duration):
    asyncio.run(asyncio.sleep(duration))

userTimes = {}
globalTime = 0
def messageCallback(user: str, message: str) -> None:
    global userTimes
    global globalTime
    t = time.time()

    # shared cooldown, only do 1 command every this many seconds, change to 0 to disable
    if t - globalTime < 0: 
        return

    # per user cooldown, change to 0 to disable
    if user in userTimes and t - userTimes[user] < 0: 
        return

    # Add your commands here
    # copy the `globalTime = t` and `userTimes[user] = t` lines if you want the cooldown to work
    # queue up your custom actions in these callbacks with the q function, like q(myAction)
    # for actions that take arguments, do it like q(lambda: myAction(arg))
    if message == "!headpat":
        globalTime = t
        userTimes[user] = t
        q(headpat)
    elif message == "!headpat-twice":
        globalTime = t
        userTimes[user] = t
        # do the headpat action twice
        q(headpat)
        q(headpat)
    elif message == "!bellypat":
        globalTime = t
        userTimes[user] = t
        q(bellyrub)
    elif message == "!cunnypat":
        globalTime = t
        userTimes[user] = t
        q(lambda: vibrateTemp(0.75, 5)) # vibrate with 75% intensity for 5 seconds
    elif re.match("^!vibrate ([0-9]+)$", message):
        # vibrates at the specified intensity
        # "!vibrate 50" would be 50% intensity for example
        globalTime = t
        userTimes[user] = t
        intensity = re.match("^!vibrate ([0-9]+)$", message).group(1)
        intensity = min(max(number, 0), 100) # min allowed is 0% and max is 100%
        intensity /= 100 # convert from 0-100 to 0.0-1.0
        q(lambda: vibrateConstant(intensity))

# define your custom actions here
# return the number of seconds to wait after the action before the next action can happen
# only .wav files are supported for sounds
# if keyboard.press_and_release doesn't work, try other_keyboard.PressAndRelease instead

def headpat():
    # play a sound and press a button
    sound("short sound.wav")
    keyboard.press_and_release('shift+a')
    return 1

def bellyrub():
    # play a sound and press a button
    sound("other sound.wav")
    # other_keyboard only supports pressing 1 key at a time
    other_keyboard.PressAndRelease('f12')
    return 2

def vibrateConstant(intensity):
    # set the vibration intensity (and leave it on)
    vibrate(intensity)
    return 3

def vibrateTemp(intensity, duration):
    # set the intensity, wait a bit, then turn it off
    vibrate(intensity)
    sleep(duration)
    vibrate(0)
    return 0
