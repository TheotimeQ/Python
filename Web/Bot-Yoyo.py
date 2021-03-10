# import urllib.request
# from bs4 import BeautifulSoup

# urlpage = 'https://shop.nvidia.com/fr-fr/geforce/store/gpu/?page=1&limit=9&locale=fr-fr&category=GPU&gpu=RTX%203080'

# page = urllib.request.urlopen(urlpage)

# Liens = soup.find('a', attrs={'class': 'featured-buy-link link-btn brand-green'})
# print(Liens)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

#DRIVER_PATH = "C:\Users\theot\.wdm\drivers\chromedriver\win32\88.0.4324.96\chromedriver.exe"
#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome()
#driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver = webdriver.Chrome("C:/Users/theot/.wdm/drivers/chromedriver/win32/88.0.4324.96/chromedriver.exe")
driver.get('https://shop.nvidia.com/fr-fr/geforce/store/gpu/?page=1&limit=9&locale=fr-fr&category=GPU&gpu=RTX%203080')

#content = driver.find_element_by_class_name('featured-buy-link')
#all_links = driver.find_elements_by_tag_name('a')
content = driver.find_element_by_css_selector('a.featured-buy-link').get_attribute("href")
print("Found : ")
print(content)

#pip install webdriver-manager
#pip install selenium