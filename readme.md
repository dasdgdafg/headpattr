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

Once you have it set up, modify the `commands.py` file to add custom actions. The example actions press buttons and play sounds, but it's just python code so you can do anything you want if you write the code for it. Maybe you want to write to a file, maybe you want to send a network request, etc. There's lots of python tutorials out there that you can copy/paste from.

To run the program, open a command prompt/terminal in the same directory as the program, and run either `python3 headpattr.py` or `python headpattr.py` or `py headpattr.py`. Which one of those commands works may depend on how you installed python and what OS you are using. On Windows, double clicking the `headpattr.bat` file may work.

In case you're wondering, it's called headpattr because the original idea was to press a hotkey to do a headpat action when someone donated.
