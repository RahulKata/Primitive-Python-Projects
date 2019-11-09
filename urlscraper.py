import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

# =============================================================================
# make sure to 
# * pip install selenium *
# before you proceeeeeeeed
# =============================================================================


class urlscraper:
    def __init__(self,search):
        self.search = search
        self.bot = webdriver.Chrome(executable_path="D:/chromedriver.exe")
    
                
# =============================================================================
# Make sure to visit " https://www.seleniumhq.org/download/ " and download the latest webdriver
# Unzip and change the executable_path accordingly
# =============================================================================


    def enter_search(self):
        
# =============================================================================
# this csv file will be created and saved in the cwd (current working directory)
# =============================================================================   
        csv_file = open(f'{self.search}_links.csv','w',newline='')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['URL']) 
        
        
        bot = self.bot
        bot.get('https://images.google.com/')
        time.sleep(2)
        search_field = bot.find_element_by_class_name('gLFyf')
        search_field.clear()
        search_field.send_keys(self.search)
        search_field.send_keys(Keys.RETURN)
        time.sleep(2)
        for i in range(2):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(10)
            images = bot.find_elements_by_class_name("rg_i")
            for image in images:
                src = image.get_attribute('src')
                print(src)
                if(src!=None):
                    csv_writer.writerow([src])


kr = urlscraper('kingjames')
kr.enter_search()

