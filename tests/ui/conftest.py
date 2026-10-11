from selenium import webdriver # 用于操作浏览器
from selenium.webdriver.chrome.options import Options # 用于设置谷歌浏览器
import pytest
#设置浏览器，启动浏览器
@pytest.fixture
def driver():
    # 创建设置浏览器对象
    q1 = Options()
    # 保持浏览器打开状态(默认是代码执行完浏览器自动关闭的)
    # q1.add_experimental_option('detach',True)
    # 创建并启动浏览器
    driver = webdriver.Chrome(options=q1)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()