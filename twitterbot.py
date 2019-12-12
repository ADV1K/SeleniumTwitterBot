from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TwitterBot:
	def __init__(self, username, password, headless=False, take_screenshots=True):
		self.username = username
		self.password = password
		self.take_screenshots = take_screenshots
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
		if self.take_screenshots:  # take screenshot
			self.driver.save_screenshot("img/login.png")
		submitBtn.click()  # submit the form
		if f"https://twitter.com/login/error?username_or_email={self.username}" == self.driver.current_url:
			self.driver.quit()  # quit the driver and raise the error
			raise ValueError("Incorrect username or password!")

	def tweet(self, text):
		if not 0 < len(text) < 280:  # check if tweet has a valid length
			raise ValueError("Too Long Tweet! tweet must be within 1 to 280 characters!")

		self.driver.get("https://twitter.com/compose/tweet")
		textArea = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div')))
		tweetBtn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div/span/span')
		textArea.send_keys(text)
		if self.take_screenshots:  # take screenshot
			self.driver.save_screenshot('img/tweet.png')
		tweetBtn.click()

	def quit(self):
		self.driver.quit()


def test():
	USERNAME = ""  # change me
	PASSWORD = ""  # change me
	raise Exception("Why are you so lazy! Change the login details with your username and password and comment this line!")

	bot = TwitterBot(USERNAME, PASSWORD)
	bot.tweet('hello world from python and selenium')
	bot.quit()


if __name__ == '__main__':
	test()
