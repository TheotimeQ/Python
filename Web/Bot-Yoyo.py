#Python version 3.8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import smtplib, ssl

#driver = webdriver.Chrome(ChromeDriverManager().install()) #Do it only the first time and get the ChromeDriverPath

#Geting chrome driver
DRIVER_PATH = "C:/Users/theot/.wdm/drivers/chromedriver/win32/88.0.4324.96/chromedriver.exe" #Carefull it's / not \
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

# on rentre les renseignements pris sur le site du fournisseur
smtp_adress = 'smtp.gmail.com'
smtp_port = 465

# on rentre les informations sur notre adresse e-mail
email_adress = 'bot.mail.zel@gmail.com'
email_password = 'ZelBot1234'

# on rentre les informations sur le destinataire
email_receiver = 'yohan.wander@gmail.com'

# on crée la connexion mail
context = ssl.create_default_context()

while 1==1 :
    #Load the site
    driver.get('https://shop.nvidia.com/fr-fr/geforce/store/gpu/?page=1&limit=9&locale=fr-fr&category=GPU&gpu=RTX%203080')

    #Find the link
    Href = driver.find_element_by_css_selector('a.featured-buy-link').get_attribute("href")
    print(Href)

    if(Href != "javascript:void(0);"):
        print("Send mail")
        with smtplib.SMTP_SSL(smtp_adress, smtp_port, context=context) as server:
            # connexion au compte
            server.login(email_adress, email_password)
            # envoi du mail
            server.sendmail(email_adress, email_receiver, Href)

    







#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Instalation librairies :

#pip install webdriver-manager
#pip install selenium

#Other cool comand
#driver = webdriver.Chrome("C:/Users/theot/.wdm/drivers/chromedriver/win32/88.0.4324.96/chromedriver.exe")

#driver.close()
