import pytest
import allure
# import time
from api.admin_user_api import admin_list,admin_get_by_id
# @pytest.mark.temp
@allure.epic('我的第一个pytest项目')
@allure.feature('后台用户管理模块')
@allure.story('完整查询测试')
@allure.title('完整查询测试用例')

@pytest.mark.admin
def test_admin_query(api_session,registered_admin):
    # user_id = None
    # try:
    #     timestamp = int(time.time())
    #     username = f'{timestamp}'
    #     email = f'{timestamp}@qq.com'
        

    #     response =  admin_register(
    #         api_session,
    #         request_data= {
    #             "username": username,#字符串?
    #             "password": '123',
    #             "icon": "string",
    #             "email": email,
    #             "nickName": "string",
    #             "note": "string"
    #             }
    #         )
    #     assert response.status_code == 200
    #     body = response.json()
    #     assert body['code'] == 200

        # user_id = body['data']['id']
    username = registered_admin['username']
    email = registered_admin['email']
    user_id = registered_admin['id']

    response = admin_list(api_session,username)
    assert response.status_code == 200
    body = response.json()
    assert body['code'] == 200
    
    users_list = body['data']['list']

    temp = None
    for i in users_list:
        if i['username'] == username:
            temp = i
            break

    assert temp is not None
    assert temp['username'] == username
    assert temp['email'] == email
    assert temp["id"] == user_id


    response = admin_get_by_id(api_session,user_id)
    assert response.status_code == 200
    body = response.json()
    assert body['code'] == 200

    assert body['data']['username'] == username
    assert body['data']['email'] == email
    # finally:
    #     if user_id is not None :
    #         admin_delete(api_session,user_id)





