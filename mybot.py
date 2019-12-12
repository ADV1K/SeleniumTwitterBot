# Import the TwitterBot class
from twitterbot import TwitterBot

# create a new bot
bot = TwitterBot("my_username", "my_secret_password")

# tweet
bot.tweet("Hello world from python and selenium")

# quit the bot and close the chrome window
bot.quit()
