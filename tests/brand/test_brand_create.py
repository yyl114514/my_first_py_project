import pytest
from api.brand_api import brand_create,brand_delete,brand_list_by_name
from data.factories import auto_create_brand_info
from common.assertions import assert_response_success,assert_page_total
import allure 
@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('品牌添加')
@allure.title('品牌添加成功用例')
@pytest.mark.brand 
def test_brand_create(api_session):
    brand_id = None
    try:
        brand_info = auto_create_brand_info()
        response = brand_create(api_session,brand_info)

        assert_response_success(response)

        response = brand_list_by_name(api_session,brand_info['name'])

        body = assert_response_success(response)

        for i in body['data']['list']:
            if i['name'] == brand_info['name']:
                brand_id = i['id']
        assert brand_id is not None
    finally:
        if brand_id is not None:
            brand_delete(api_session,brand_id)
            


@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('品牌添加')
@allure.title('添加品牌时名称为空')
@pytest.mark.brand
def test_brand_create_name_is_null(api_session):
    brand_info = auto_create_brand_info()
    brand_info["name"] = ""
    response = brand_create(api_session,brand_info)

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 404
    assert body['message'] == 'name不能为空'


@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('品牌添加')
@allure.title('创建品牌时factoryStatus=2')
@pytest.mark.brand
def test_brand_create_factoryStatus_is_2(api_session):
    brand_info = auto_create_brand_info()
    brand_info["factoryStatus"] = 2
    response = brand_create(api_session,brand_info)

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 404
    assert body['data'] == None

    response = brand_list_by_name(api_session,brand_info['name'])
    
    assert_page_total(response,0)

@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('品牌添加')
@allure.title('创建品牌时sort=-1')
@pytest.mark.brand
def test_brand_create_sort_is_minus_1(api_session):
    brand_info = auto_create_brand_info()
    brand_info["sort"] = -1

    response = brand_create(api_session,brand_info)

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 404
    assert body['data'] == None

    response = brand_list_by_name(api_session,brand_info['name'])
    
    assert_page_total(response,0)

@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('品牌添加')
@allure.title('创建品牌时showStatus=2')
@pytest.mark.brand
def test_brand_create_showStatus_is_2(api_session):
    
    brand_info = auto_create_brand_info()
    brand_info["showStatus"] = 2
    response = brand_create(api_session,brand_info)

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 404
    assert body['data'] == None

    response = brand_list_by_name(api_session,brand_info['name'])
    
    assert_page_total(response,0)

@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('品牌添加')
@allure.title('创建品牌时logo为空')
@pytest.mark.brand
def test_brand_create_logo_is_null(api_session):
    brand_info = auto_create_brand_info()
    brand_info["logo"] = ""

    response = brand_create(api_session,brand_info)

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 404
    assert body['data'] == None

    response = brand_list_by_name(api_session,brand_info['name'])

    assert_page_total(response,0)

