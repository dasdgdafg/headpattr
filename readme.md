Install python if you don't already have it: https://www.python.org/downloads/

Install the `twitchAPI` package for python by running `pip install twitchAPI` or `py -m pip install twitchAPI` or `python -m pip install twitchAPI` in a command prompt/powershell/terminal. Which one of those commands works may depend on how you installed python and what OS you are using.  
Do the same thing for the packages `keyboard` and `winsound`. (`winsound` is only on windows, use something else instead on linux, such as `playsound`.)

Create a file called `apikeys.txt`, that looks like this
```
twitchusername:
accesstoken:
refreshtoken:
clientid:
streamelementsjwt:
streamlabssocket:
```
Get Twitch API tokens from https://twitchtokengenerator.com/  
(you can generate the tokens directly through Twitch if you prefer, but I find it much easier to use a 3rd party site)  
Select bits:read, channel:read:subscriptions, and channel:read:redemptions  
This will allow the program to see when people donate via bits/subs, and when they redeem channel points  
Click 'Generate Token!', it will take you to twitch where you can click 'authorize', then copy the 3 tokens into the `apikeys.txt` file, after the `:` on the appropriate line.  
Also add your twitch username in that file.  
For streamelements, get your jwt token from https://streamelements.com/dashboard/account/channels, visible after toggling the 'Show secrets' button  
For streamlabs, get your socket token from https://streamlabs.com/dashboard#/settings/api-settings, click "API Tokens" then "Click To Show Socket Token"  
The `apikeys.txt` file should end up looking something like this (these are example values, not real ones):
```
twitchusername:SomeUsername69
accesstoken:lb890awnr340ifgmiaf89409jkadfs
refreshtoken:ibdnyu56sdnbv65yfrsbc5nbuymgy65sd5sew98dg2n65nvs56
clientid:werg18hmg65df98wrgth65fhgj5u59
streamelementsjwt:sdgthFGulijghws68548qw4ht9DBytj49rtq.948eweDFG4wert48y4tuy84er98wASDFrqw489th4djhuyDFSGy545j9sdjm0a90-o3ejoigj09wh82iTRYJrojgwioert8092jr899UIOrfFGHBNks20TY489hgdsf98XCVBAghfdlgkjaSBNVjhdflkddfahsgjaCVBho4879dfbgjhkfdhasdfgsbDFGH0hjf6h98idsjkdhfghjsdf5dfgsqwre6eytr5ytuiofghj6vdhfiug93ZXVCiundfg97hasdfgSDFG4hd9fgh9h.9fgd78ySDHSDFGg4oidsj-sdfgoijas89DHFGgdoiss
streamlabssocket:eyJ0adsfgi4351QasdfgbGciOiJIasdfgiJ9.eyJ0b2asdfI6IkI3Ras768Q2NTE4NSDGIFOUJKBDIiwicmVh345vbsdfhsdofgVlLCJwSID435FIUOJhc3RlciI6dHJ1hsgf783ddHViZV9pZCIAOFSJIUDuND378WZuSGhPsdfhgWZ1523LQSJ9.d453INFJF1jf354-jgs453DIFasdfGdBb12-Vszsd46
```

To run the program, open a command prompt in the same directory as the program, and run either `python3 headpattr.py` or `python headpattr.py` or `py headpattr.py`. Which one of those commands works may depend on how you installed python and what OS you are using. On Windows, double clicking the `headpattr.bat` file may work.

Once you have it set up, modify the `commands.py` file to add custom actions. The example actions press buttons and play sounds, but it's just python code so you can do anything you want if you write the code for it. Maybe you want to write to a file, maybe you want to send a network request, etc. There's lots of python tutorials out there that you can copy/paste from.

In case you're wondering, it's called headpattr because the original idea was to press a hotkey to do a headpat action when someone donated.
