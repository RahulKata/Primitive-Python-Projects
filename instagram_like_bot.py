import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# =============================================================================
# make sure to 
# * pip install selenium *
# before you proceeeeeeeed
# =============================================================================

class InstaBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(executable_path="D:/chromedriver.exe")
        
# =============================================================================
# Make sure to visit " https://www.seleniumhq.org/download/ " and download the latest webdriver
# Unzip and change the executable_path accordingly
# =============================================================================

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/')
        time.sleep(3)
        bot.find_element_by_class_name("coreSpriteFacebookIconInverted").click()
        time.sleep(3)
        email = bot.find_element_by_id('email')
        password = bot.find_element_by_id('pass')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

    def like_photo(self,hashtag):
        bot = self.bot
        bot.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        time.sleep(4)
        for i in range(4):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)

        hrefs = bot.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        for i in pic_hrefs:
            print(i)
        print(f'{hashtag} photos: {len(pic_hrefs)}')

        # Liking photos
        for pic_href in pic_hrefs:
            bot.get(pic_href)
            time.sleep(3)
            bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                bot.find_element_by_link_text("Like").click()
                time.sleep(18)  # translates to 200 pics/hr -> insta limit
            except Exception as e:
                time.sleep(2)


# =============================================================================
# Enter your username and password in the InstaBot()  function 
# and also the hashtag you are looking for, in the like_photo() function
# =============================================================================

kr = InstaBot('your_username@gmail.com','password')
kr.login()
kr.like_photo('hashtag')

