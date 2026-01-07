
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

#Location to chromedriver
service = Service('/Users/pratikshya/Downloads/chromedriver-mac-arm64/chromedriver')

#initialize the driver
driver = webdriver.Chrome(service=service, options=chrome_options)

#open sanitize email
driver.get("https://sauce-demo.myshopify.com/account/login")
wait = WebDriverWait(driver, 10)

# user = wait.until(
#     EC.visibility_of_element_located((By.XPATH, "//input[@id='idToken1']"))
# )
# user.send_keys("standard_user")
#
# password = wait.until(
#     EC.visibility_of_element_located((By.XPATH, "//input[@id='idToken2']"))
# )
#
# password.send_keys("secret_sauce")
#
# login_btn = wait.until(
#     EC.visibility_of_element_located((By.XPATH, "//input[@id='loginButton_0']"))
# )
#
# login_btn.click()

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

login_in = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Log In']"))

)
login_in.click()

login_email = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@id='customer_email']"))
)
login_email.send_keys("sabitra231@gmail.com")

login_password = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@id='customer_password']"))
)
login_password.send_keys("Pratik@231")

signin_btn = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@value='Sign In']"))
)
signin_btn.click()

time.sleep(10)
