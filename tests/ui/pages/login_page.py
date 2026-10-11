from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config import login_page_url,home_page_url
#设置浏览器，启动浏览器
class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    def open(self):
        self.driver.get(f'{login_page_url}')
        return self
    def send_username(self,username):
        send_username = self.driver.find_element(By.NAME, "username")

        send_username.send_keys(Keys.CONTROL, "a")
        send_username.send_keys(Keys.BACKSPACE)

        send_username.send_keys(f"{username}")
        return self
    def send_password(self,password):
        send_password = self.driver.find_element(By.NAME, "password")

        send_password.send_keys(f"{password}")
        return self
    def click_login_button(self):
        self.driver.find_element(By.XPATH,'//button[.//span[normalize-space()="登录"]]').click()
        return self

    def wait_for_home(self):
        WebDriverWait(self.driver, 10).until(
                    lambda driver: f"{home_page_url}" == driver.current_url
                )
        return self
        
        