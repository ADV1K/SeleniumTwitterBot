# A simple script that automatically posts tweets of links of latest articles in Fedora Magazine along with their titles.
import feedparser
import pickle

from twitterbot import TwitterBot

USERNAME = "FedoraMagazine"  # enter your username instead
PASSWORD = "my_secret_password"  # enter your password instead


def main():
	feed = feedparser.parse('https://fedoramagazine.org/feed/')  # read the feed
	try:
		links = pickle.load(open('tweeted_links', 'rb'))  # load posted links
	except FileNotFoundError:
		links = set()  # no link is posted yet

	try:
		bot = TwitterBot(USERNAME, PASSWORD)
		for entry in feed.entries[::-1]:
			link = entry.link
			title = entry.title
			print(title, link)
			if link not in links:
				bot.tweet(title + '\n' + link)
				links.add(link)
		bot.quit()  # quits and clears the chromedriver from memory
	finally:
		pickle.dump(links, open('tweeted_links', 'wb'))  # add the posted links to the file


if __name__ == '__main__':
	main()
