# ConnectBot
## Exploits and Utilities for the WA educational website: _connect.det.wa.edu.au_
Written by Mitch. N., year 11 student from Butler College

### Information
To install ConnectBot, ensuere that you're using MacOS, as this is what it is programmed to run on. Place the entire repository inside a folder somewhere, and install the following modules via PIP
- requests
- pyinstaller


Once these modules have been installed, open a terminal instance, and navigate to the folder that 
contains the repository. Run the command `pyinstaller --onefile main.py` and wait for it to build. Once the terminal prompts for another commant to be entered, and there have been no error outputs, look inside the `dist` folder, here you should  see an executable named `main` which you can run.


*Note: For ConnectBot to work correctly, install a folder named `ConnectBot` to /Users/yourusername, containing the `main` executable. After this, open it and break loose!*

### Commands:
*Locking Connect Account Commands*
- Locking Bulk accounts constantly for a set amount of time:
  - `lock_account --bulk filename.txt --loop 9999`
    - This will constantly lock all Connect accounts contained in the list until the specified loop time has been reached, in this case: 9999 seconds.


- Locking a single account constantly for a set amount of time:
  - `lock_account username --loop 9999`
    - This command will constantly lock the specified Connect account until the timer is reached, or the application is closed.


- Locking Bulk accounts once:
  - `lock_account --bulk filename.txt`
    - This command will lock the specified Connect accounts a single time, then continue.


- Locking a single account once:
  - `lock_account username`
    - This command will lock the specified Connect account a single time, then continue.




*Notice Feed Commands*

- List a certain amount of posts from your notice feed.
  - `FeedUtil --get_feed 10`
    - This will retrieve the 10 latest posts on your Connect feed, and wil give you a `title`, the `class` that the notice is from, as well as the `ItemEvent` which is used for later applications, such as artificially boosting the views of a notice.


*View Boosting Commands*

- Bost a Connect notice's view counter
  - `BotUtil --bot_notice --views 10000 --threads 100 --item_event ItemEvent:3850171426`
    - This example command would spawn `100 threads`, each viewing the post `10` times to reach the target amount of views, `1000`. Additionally, the `--item_event` to specify what notice the views are going to.


### About Me
G'day, my name's Mitch Naake!

As of writing this, I'm a year 11 ATAR Computer Science student at Butler College. My joy in technology spurts from liking to find loopholes, and ways around things. Hence this neat project ;)

I've been programming in Python since roughly year 9, where I first tried to tackle this problem using selenium. God that was slow :D

I've progressed incredibly in my knowhow of the Python language, and have started some major projects, most notable https://docs.sayetta.com/stream/. Stream is a Anti-DDoS network for Minecraft servers. In short, it's a globally-distributed network of reverse-proxies that prevents players from getting the backend address of the Minecraft server that they're connected to, as well as drop packets from IPs that are in a public blacklist, and on top of all of this, filtering all traffic via Corero hardware! 


If you want to have a chat, feel free. You can find my discord server attached the Stream link above!

Cheers,

Mitch :)
