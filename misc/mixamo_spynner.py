from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.mixamo.com/motions")

login_form = driver.find_element_by_xpath("//a[@class='md-trigger']")
login_form.click()
email_input = driver.find_element_by_xpath("//input[@name='user_session[login]']")
email_input.send_keys("owen661120ver2@gmail.com")
password_input = driver.find_element_by_xpath("//input[@name='user_session[password]']")
password_input.send_keys("wenkaikoto74")
login_submit = driver.find_element_by_xpath("//input[@class='primary-button'][@value='Log In']")
login_submit.click()


content = driver.find_element_by_class_name("listOfMotions")


