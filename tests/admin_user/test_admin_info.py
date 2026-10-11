import allure
import pytest
# from api import create_authorized_session   conftest.py中已经用session了，不用调用了
from config import BASE_URL
@allure.epic('我的第一个pytest项目')
@allure.feature('后台用户管理模块')
@allure.story('查询登录的用户信息')
@allure.title('查询登录的用户信息用例')

@pytest.mark.admin
def test_get_admin_info(api_session):#用api_session来接受conftest.py中的session
    response = api_session.get(f"{BASE_URL}/admin/info",timeout=5)

    body = response.json()

    assert response.status_code == 200
    assert body['code'] == 200

    assert body["data"]["username"] == "admin"
    assert "超级管理员" in body["data"]["roles"]
