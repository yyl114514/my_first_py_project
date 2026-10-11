from config import USERNAME,PASSWORD,home_page_url
import pytest
import allure
from tests.ui.pages.login_page import LoginPage

@allure.epic('我的第一个pytest项目')
@allure.feature('web测试模块')
@allure.story('登录测试')
@allure.title('登录测试用例')
@pytest.mark.web
def test_admin_login(driver):
    page = LoginPage(driver)
    page.open()
    page.send_username(f'{USERNAME}')
    page.send_password(f'{PASSWORD}')
    page.click_login_button()
    page.wait_for_home()
    assert driver.current_url == f"{home_page_url}"
    