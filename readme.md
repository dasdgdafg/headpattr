Install python if you don't already have it: https://www.python.org/downloads/

Install the twitchAPI package for python by running "pip install twitchAPI" or "py -m pip install twitchAPI" or "python -m pip install twitchAPI" in a command prompt
Do the same thing for the packages keyboard and winsound. winsound is only on windows, use something else instead on linux, such as playsound.

Get Twitch API tokens from https://twitchtokengenerator.com/
(you can generate the tokens directly through Twitch if you prefer, but I find it much easier to use a 3rd party site)
Select bits:read, channel:read:subscriptions, and channel:read:redemptions
This will allow the program to see when people donate via bits/subs, and when they redeem channel points
Click 'Generate Token!', it will take you to twitch where you can click 'authorize', then copy the 3 tokens into the apikeys.txt file
Also update the twitch username in that file

To run the program, open a command prompt in the same directory as the program, and run either "python3 headpattr.py" or "python headpattr.py" or "py headpattr.py". Which one of those works may depend on how you installed python and what OS you are using. On Windows, double clicking the headpattr.bat file may work.

