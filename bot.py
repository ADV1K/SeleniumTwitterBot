from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TwitterBot:
	def __init__(self, username, password, headless=False):
		self.username = username
		self.password = password
		self.headless = headless
		options = Options()
		options.headless = headless
		self.driver = webdriver.Chrome(options=options)
		self.login()

	def login(self):
		self.driver.get("https://twitter.com/login")
		usernameBox = self.driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
		passwordBox = self.driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
		submitBtn = self.driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
		usernameBox.send_keys(self.username)
		passwordBox.send_keys(self.password)
		submitBtn.click()
		if f"https://twitter.com/login/error?username_or_email={self.username}" == self.driver.current_url:
			self.driver.quit()  # quit the driver and raise the error
			raise ValueError("Incorrect username or password!")

	def tweet(self, text):
		if not 0 < len(text) < 280:  # check if tweet has a valid length
			return False

		self.driver.get("https://twitter.com/compose/tweet")
		textArea = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div')))
		tweetBtn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div/span/span')
		# textArea.click()
		textArea.send_keys(text)
		tweetBtn.click()

	def quit(self):
		self.driver.quit()


def test():
	USERNAME = "FedoraMagazine"  # change me
	PASSWORD = "password789798"  # change me
	# raise Exception("Why are you so lazy! Change the login details with your username and password and comment this line!")

	bot = TwitterBot(USERNAME, PASSWORD)
	bot.tweet('hello world from python and selenium')
	bot.quit()


if __name__ == '__main__':
	test()
