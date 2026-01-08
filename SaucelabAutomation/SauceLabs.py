
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



chrome_options = Options()
chrome_options.add_argument("--start-maximized")

#chrome_options.add_argument("--incognito")

#Location to chromedriver
service = Service('/Users/pratikshya/Downloads/chromedriver-mac-arm64/chromedriver')

#initialize the driver
driver = webdriver.Chrome(service=service, options=chrome_options)

#open sanitize email
driver.get("https://sauce-demo.myshopify.com")
wait = WebDriverWait(driver, 10)

def click_element(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    element.click()

def send_keys_to_element(driver, xpath, keys):
    element = driver.find_element(By.XPATH, xpath)
    element.clear()
    element.send_keys(keys)

def clear_element(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    element.clear()

#For sign up
sign_up = "//a[normalize-space()='Sign up']"
click_element(driver, sign_up)
print("signup button is clicked")
time.sleep(3)

#Verify registration page opens properly by checking the url
if "register" in driver.current_url:
    print("Registration form loaded successfully")
else:
    print("Warning: Registration form may not have loaded properly - current URL:", driver.current_url)
time.sleep(2)
first_name = "//input[@id='first_name']"
send_keys_to_element(driver, first_name, "Pratikshya")
print("First name is entered")
time.sleep(3)
last_name = "//input[@id='last_name']"
send_keys_to_element(driver, last_name, "Bhattarai")
print("Last name is entered")
time.sleep(3)
email_add = "//input[@id='email']"
# Generate a unique email address each time
# time.time() comes from python's built-in time module
# It returns the current time in seconds since jan 1, 1970
# int(time.time()) converts that floating-point number into an integer
# f" ...." This is an f-string(formatted string). It lets you insert python expressions directly inside {}
# "testuser_{int(time.time())}@gmail.com" The timestamp is inserted into the email string


unique_email = f"testuser_{int(time.time())}@gmail.com"
send_keys_to_element(driver, email_add, unique_email)
print("Email is entered")

password = "//input[@id='password']"
send_keys_to_element(driver, password, "Pratik@123")
print("Password is entered")

create_acc = "//input[@value='Create']"
click_element(driver, create_acc)

#Assertion for sign up
logout_btn_element = driver.find_element(By.XPATH, "//a[text()='Log Out']")
if logout_btn_element:
    print("Registration successful - log out element found")
else:
    print("Registration not succesful - log out element not found")

#For login
login_btn = "//a[normalize-space()='Log In']"
click_element(driver, login_btn)

login_email = "//input[@id='customer_email']"
send_keys_to_element(driver, login_email, "sabitra231@gmail.com")

login_password = "//input[@id='customer_password']"
send_keys_to_element(driver, login_password, "Pratik@123")

signin_btn = "//input[@value='Sign In']"
click_element(driver, signin_btn)

#For My Account
my_account = "//a[@href='/account'][normalize-space()='My Account']"
click_element(driver, my_account)

#For about us
about_us = "//div[@class='seven columns offset-by-one desktop']//a[normalize-space()='About Us']"
click_element(driver, about_us)

# Verify that we are in about us page
if "about-us" in driver.current_url:
    print("We are in about us page")

else:
    print("We are not in about us page")



time.sleep(30)






# sign_up = wait.until(
#     EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Sign up']"))
# )
# sign_up.click()
#
# first_name = wait.until(
#     EC.visibility_of_element_located((By.XPATH, "//input[@id='first_name']"))
# )
# first_name.send_keys("pratikshya")
#
# last_name = wait.until(
#     EC.visibility_of_element_located((By.XPATH, "//input[@id='last_name']"))
# )
# last_name.send_keys("Bhattarai")
#
# email_add = wait.until(
#     EC.visibility_of_element_located((By.XPATH, "//input[@id='email']"))
# )
#
# email_add.send_keys("prabinbhattarai414@gmail.com")
#
# password = wait.until(
#     EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))
# )
#
# password.send_keys("Pratik@123")
#
# create_acc = wait.until(
#     EC.visibility_of_element_located((By.XPATH, "//input[@value='Create']"))
# )
# create_acc.click()

# login_in = wait.until(
#     EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Log In']"))
#
# )
# login_in.click()
#
# login_email = wait.until(
#     EC.visibility_of_element_located((By.XPATH, "//input[@id='customer_email']"))
# )
# login_email.send_keys("prabinbhattarai414@gmail.com")
#
# login_password = wait.until(
#     EC.visibility_of_element_located((By.XPATH, "//input[@id='customer_password']"))
# )
# login_password.send_keys("Pratik@231")
#
# signin_btn = wait.until(
#     EC.visibility_of_element_located((By.XPATH, "//input[@value='Sign In']"))
# )
# signin_btn.click()
