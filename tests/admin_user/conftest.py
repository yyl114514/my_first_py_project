import time
import pytest
from api.admin_user_api import admin_register,admin_delete
import allure


@pytest.fixture
def registered_admin(api_session):
    user_id = None
    try:
        timestamp = int(time.time())
        username = f'{timestamp}'
        email = f'{timestamp}@qq.com'
            
    
        response =  admin_register(
            api_session,
            request_data= {
                "username": username,#字符串?
                "password": '123',
                "icon": "string",
                "email": email,
                "nickName": "string",
                "note": "string"
                }
                )
        
        assert response.status_code == 200
        body = response.json()
        assert body['code'] == 200
        
        data = body['data']
        
        user_id = data['id']

        
        yield data
    finally:
        if user_id is not None:
            admin_delete(api_session,user_id)
