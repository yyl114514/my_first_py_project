import allure
from api.admin_user_api import admin_delete,admin_get_by_id,admin_register
import time
import pytest
@allure.epic('我的第一个pytest项目')
@allure.feature('后台用户管理模块')
@allure.story('用户删除')
@allure.title('用户删除用例')

@pytest.mark.admin
def test_admin_delete(api_session):
    user_id = None
    delete = False
    try:
        timestamp = int(time.time())
        user_name = f'auto_user{timestamp}'
        email = f'auto_email{timestamp}@qq.com'
        

        data = {
        "username": user_name,
        "password": "string",
        "icon": "string",
        "email": email,
        "nickName": "string",
        "note": "string"
        }

        response = admin_register(api_session,data)

        assert response.status_code == 200
        body = response.json()
        assert body['code'] == 200

        user_id = body['data']['id']
    
    
        response = admin_delete(api_session,user_id)

        assert response.status_code == 200
        body = response.json()
        assert body['code'] == 200
        assert body['data'] == 1

        delete = True

        response = admin_get_by_id(api_session,user_id)

        assert response.status_code == 200
        body = response.json()

        assert body['code'] == 200
        assert body['data'] is None ##null 不是字符串 

    finally:
        if user_id is not None and delete is False:
            admin_delete(api_session,user_id)