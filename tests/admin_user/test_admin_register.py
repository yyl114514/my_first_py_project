import allure
# from config import BASE_URL
import pytest
import time
from api.admin_user_api import admin_register,admin_delete
# @pytest.mark.temp
@allure.epic('我的第一个pytest项目')
@allure.feature('后台用户管理模块')
@allure.story('用户注册功能测试')
@allure.title('用户注册功能测试用例')

@pytest.mark.admin
def test_admin_register(api_session):
    try:
        timestamp = int(time.time())
        auto_username = f'auto_user_{timestamp}'
        auto_email = f'auto_email_{timestamp}@qq.com'
        user_id = None

        response = admin_register(
            api_session,
                {
                "username": f"{auto_username}",
                "password": "123",
                "icon": "string",
                "email": f"{auto_email}",
                "nickName": "用户",
                "note": "string"
                }
            )

        assert response.status_code ==200

        body = response.json()

        assert body['code'] ==200

        user_id = body['data']['id']
        print(f"新添加用户：{body['data']['username']}")

        assert body['data']['username'] == auto_username
        assert body["data"]["email"] == auto_email

    finally:
        if user_id!= None:
            admin_delete(api_session,user_id)