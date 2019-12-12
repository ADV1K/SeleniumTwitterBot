from twitterbot import TwitterBot

USERNAME = "change_me"
PASSWORD = "change_me"

bot = TwitterBot(USERNAME, PASSWORD)
bot.tweet("Hello world from python and selenium")
bot.quit()
