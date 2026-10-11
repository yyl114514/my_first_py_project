import pytest
from api.brand_api import brand_create,brand_delete,auto_create_brand_info,brand_list_by_name
import allure 
@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('品牌添加')
@allure.title('品牌添加用例')
@pytest.mark.brand
def test_brand_create(api_session):
    brand_id = None
    try:
        brand_info = auto_create_brand_info()
        response = brand_create(api_session,brand_info)

        assert response.status_code == 200

        body = response.json()
        assert body['code'] == 200
        assert body['data'] == 1

        response = brand_list_by_name(api_session,brand_info['name'])

        assert response.status_code == 200
        
        body = response.json()
        assert body['code'] == 200

        assert body['data']['total'] == 1

        for i in body['data']['list']:
            if i['name'] == brand_info['name']:
                brand_id = i['id']
        assert brand_id is not None
    finally:
        if brand_id is not None:
            brand_delete(api_session,brand_id)