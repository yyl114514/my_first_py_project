import pytest
from api.brand_api import brand_update,brand_get_info_by_id

import allure 
@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('品牌修改')
@allure.title('品牌修改用例')

@pytest.mark.brand
def test_brand_update(api_session,add_temp_brand):
    new_name ='abcde'
    new_brand_info = {
        "name": new_name,
        "firstLetter": "a",
        "sort": 0,
        "factoryStatus": 0,
        "showStatus": 0,
        "logo": "string",
        "bigPic": "string",
        "brandStory": "string"
    }
    response = brand_update(api_session,new_brand_info,add_temp_brand['id'])

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 200
    assert body['data'] == 1

    response = brand_get_info_by_id(api_session,add_temp_brand["id"])

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 200

    assert body['data']['name'] == new_name
    assert body['data']['firstLetter'] == 'a'

    

