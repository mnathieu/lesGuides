from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def accountLogin(driver, user, pswrd):
    driver.get("https://guides-prod.audaxis.com/compierezk/")
    assert 'Bienvenue sur SCRIBe' in driver.title
    element = driver.find_element_by_id("inputid")
    element.clear()
    element.send_keys(user)
    element = driver.find_element_by_id("inputpwd")
    element.send_keys(pswrd)
    element.send_keys(Keys.RETURN)
    time.sleep(2)
    element = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/table/tbody/tr/td/div/div/div[1]/div/div[2]/div/table/tbody/tr[6]/td/div/table/tbody/tr/td[3]/table/tbody/tr/td/div/span[1]/table/tbody/tr[2]/td[2]")
    element.click()

def connectToScribe():
    driver = webdriver.Firefox()
    driver.get("https://guides-prod.audaxis.com/compierezk/")
    assert 'Bienvenue sur SCRIBe' in driver.title
    return driver

def addMember(driver):
    gestion_des_membres = driver.find_element_by_xpath("//*[starts-with(@id,\"z_\") and contains(@id, \"_84!open\")]")
    time.sleep(2)
    gestion_des_membres.click()
    time.sleep(2)
    membres = driver.find_element_by_xpath("//*[starts-with(@id,\"z_\") and contains(@id, \"_d4!hvig\")]")
    membres.click()
