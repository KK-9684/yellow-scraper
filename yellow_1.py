import pandas as pd
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import undetected_chromedriver as uc

options = uc.ChromeOptions() 
options.headless = True 
url = "https://www.yellowpages.com.au/search/listings?clue=Renovations&locationClue=Greater+Sydney%2C+NSW"
end = 30
count = 0
url_list = []
driver = uc.Chrome()
driver.maximize_window()
for i in range(1, end):
    driver.get(url + "&pageNumber=" + str(i))
    time.sleep(3)
    for row in driver.find_elements(By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div/div[1]/div[2]/div[position() <= last()-4]"):
        try:
            a_tag = row.find_element(By.TAG_NAME, 'a')
            try:
                if (a_tag.get_attribute('href') is not None and "isTopOfList" not in a_tag.get_attribute('href') and "www.thryv.com.au" not in a_tag.get_attribute('href')):
                    url_list.append(a_tag.get_attribute('href'))
            except NoSuchElementException:
                pass
        except NoSuchElementException:
            pass
    if (i%7 == 0 or i == end-1):
        count = count + 1
        df = pd.DataFrame({'url_list': url_list})
        df.to_csv('list'+str(count)+'.csv', index=False, encoding='utf-8')
        url_list = []
driver.close()



