Install python if you don't already have it: https://www.python.org/downloads/

Install the dependencies. Depending on your operating system and how you installed python, the command for this will be something like `pip install -r requirements.txt` or `py -m pip install -r requirements.txt` or `python -m pip install -r requirements.txt`. Most of the dependencies are only needed for certain integrations, so you could just manually install the ones you want if you prefer.  
Do the same thing for the packages `keyboard` and `winsound`. (`winsound` is only on windows, use something else instead on linux, such as `playsound`.)

Create a file called `apikeys.txt`, that looks like this
```
twitchusername:
youtubeusername:
pomfusername:
```
Fill out your username for the chats that you want to connect to. Leave it blank for ones you don't use.  
For Twitch, use the name found in the url for your channel page, like https://www.twitch.tv/yourname. This is not necessairly the same as your display name which shows up in other places.  
For Youtube, use the name found in the url for your channel page, like https://www.youtube.com/c/yourname. This is not necessairly the same as your display name which shows up in other places.  
For Pomf, use the name found in the url for your channel page, like https://pomf.tv/stream/yourname.  
If you want to connect to all three, it would end up looking something like this:
```
twitchusername:yourtwitchusername
youtubeusername:YourYoutubeUsername
pomfusername:YourPomfUsername
```
If you want to just want to connect to Twitch, it would end up looking something like this:
```
twitchusername:yourtwitchusername
youtubeusername:
pomfusername:
```

Once you have that set up, modify the `commands.py` file to add custom actions. The example actions are at the bottom of the file. The action should return the number of seconds to wait before another action can happen. If there is no need to wait, `return 0`. If the action is doing something like playing a sound or triggering an animation, you may want to set a delay so the next action can't happen until the sound/animation is over. If the sound was 2 seconds long for example, you could `return 2` at the end of the action.  
The `sound` function will play a sound. It only works with .wav files, and only on windows. If you use linux, you probably know enough coding to modify it yourself to work on linux. Put the .wav files in the same directory as the commands.py file.  
The `keyboard.press_and_release` function allows pressing a key or combination of keys. This is useful if you have a program that will change your model or play animations in response to keypresses. There is also a `other_keyboard.PressAndRelease` function that presses a key, but is implemented differently. other_keyboard only supports pressing 1 key at a time. Depending on how the program is listening for keypresses, you may need to use `other_keyboard` if `keyboard` isn't working. In particular, VTubeStudio doesn't seem to work with the regular `keyboard` library.  
The `vibrate` function allows controlling toys that are connected via [Intiface](https://intiface.com/desktop/). You will need to have Intiface installed and the server running for this to work.  
The actions are just python code so you can do anything you want if you write the code for it. Maybe you want to write to a file, maybe you want to send a network request, etc. There's lots of python tutorials out there that you can copy/paste from.  

After writing the actions that you want to do, the next part of the set up is to decide what chat commands you want to trigger those actions.  Above the sample actions, you can find the sample command code. The simplest way to do this is to check if the message exactly matches a command. The example commands all start with `!`, but this is not required; they can be whatever you want. If you would like to use regular expressions, you can do something like `elif re.match("my regex", message):` instead of `elif message == "my command":`. Info about how to use regular expressions can be found [here](https://docs.python.org/3/howto/regex.html).  

Above the commands, you can also change the lines `if t - globalTime < 0:` and `if user in userTimes and t - userTimes[user] < 60:` if you would like to adjust the cooldown. By default, the same user can only give a command once every 60 seconds.

To run the program, open a command prompt/terminal in the same directory as the program, and run either `python3 headpattr.py` or `python headpattr.py` or `py headpattr.py`. Which one of those commands works may depend on how you installed python and what OS you are using. On Windows, double clicking the `headpattr.bat` file may work.

In case you're wondering, it's called headpattr because the original idea was to press a hotkey to do a headpat action when someone donated. An older version of this program would do things in response to Twitch subs/bits, but it didn't always work and there was no way to test it, so I decided to just integrate with chat instead.
