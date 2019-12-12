# SeleniumTwitterBot
A simple python script that automatically posts tweets of links of latest articles in Fedora Magazine along with their titles

just simply edit make your username and password in the mybot.py and run the script. 

## creating a simple bot
```python
# Import the TwitterBot class
from twitterbot import TwitterBot

# create a new bot
bot = TwitterBot("my_username", "my_secret_password")

# tweet
bot.tweet("Hello world from python and selenium")

# quit the bot and close the chrome window
bot.quit()
```

if you don't want to see that unnecessary chrome pop-up then use
```python
bot = TwitterBot("my_username", "my_secret_password", headless=True)
```

## Missing a feature
if you feel like you're missing a feature or if you have found a bug then feel free to open a pull request.
