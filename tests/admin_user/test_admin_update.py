import allure
import time
import pytest
from api.admin_user_api import admin_update,admin_get_by_id
@allure.epic('我的第一个pytest项目')
@allure.feature('后台用户管理模块')
@allure.story('用户信息修改')
@allure.title('用户信息修改用例')

@pytest.mark.admin
def test_admin_update(api_session,registered_admin):

    old_username = registered_admin['username']
    old_email = registered_admin['email']
    user_id = registered_admin['id']

    timestamp = int(time.time())
    new_username = f'auto_user_{timestamp}'
    new_email = f'auto_email_{timestamp}@qq.com'

    update_data = {
    "username": new_username,
    "icon": "string",
    "email": new_email,
    "nickName": "string",
    "note": "string"
    }

    response = admin_update(api_session,user_id,update_data)

    assert response.status_code == 200
    data = response.json()
    assert data['code'] == 200

    response = admin_get_by_id(api_session,user_id)
    
    assert response.status_code == 200
    data = response.json()
    assert data['code'] == 200

    assert data['data']['username'] !=old_username
    assert data['data']['email'] !=old_email

    assert data['data']['username'] == new_username
    assert data['data']['email'] == new_email



