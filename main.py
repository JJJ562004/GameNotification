from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from smtplib import SMTP
from email.mime.text import MIMEText

USER_MAIL = 'darknessrisesgamer999@gmail.com'
APP_PASS = 'jiao bdih vvop ufyq'

driver = webdriver.Chrome()
driver.get('https://store.epicgames.com/en-US/')
action = ActionChains(driver)
sleep(2)
action.scroll_by_amount(delta_x=0, delta_y=2300)
action.perform()
sleep(3)
value_name = driver.find_element(By.XPATH,
                                 value='//*[@id="dieselReactWrapper"]/div/div/div[4]/main/div[2]/div/div/div/div[3]/div[2]/span[1]/div/div/section/div/div[3]/div/div/div/a/div/div[2]/div/h6').text
value_date = driver.find_element(By.XPATH,
                                 value='//*[@id="dieselReactWrapper"]/div/div/div[4]/main/div[2]/div/div/div/div[3]/div[2]/span[1]/div/div/section/div/div[3]/div/div/div/a/div/div[2]/div/p/span').text

def mail(text):
    msg = MIMEText(text)
    msg['Subject'] = f"FREE GAME {value_name}"
    msg['From'] = USER_MAIL
    msg['To'] = USER_MAIL
    return msg


with SMTP('smtp.gmail.com') as smtp:
    smtp.starttls()
    smtp.login(USER_MAIL, APP_PASS)
    if value_date != "Free Now - Sep 26 at 10:00 PM":
        m = mail(f"{value_name} is not free yet, wait!")
    else:
        m = mail(f"{value_name} is noew free, get!")
    smtp.sendmail(USER_MAIL, USER_MAIL, m.as_string())
print("Mail sent!")
