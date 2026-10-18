from api.brand_api import brand_create,brand_delete,brand_list_by_name,brand_get_info_by_id
from data.factories import auto_create_brand_info
from common.assertions import assert_response_success,assert_page_total,assert_business_error
import pytest

import allure 
@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('品牌删除')
@allure.title('品牌删除成功')
@pytest.mark.brand
def test_brand_delete(api_session):
    brand_id = None
    delete = False
    try:
        brand_info = auto_create_brand_info()
        response = brand_create(api_session,brand_info)

        body = assert_response_success(response)
        assert body['data'] == 1

        response = brand_list_by_name(api_session,brand_info['name'])

        body = assert_page_total(response,1)

        for i in body['data']['list']:
            if i['name'] == brand_info['name']:
                brand_id = i['id']

        response = brand_delete(api_session,brand_id)

        assert_response_success(response)

        delete = True

        response = brand_get_info_by_id(api_session,brand_id)

        body = assert_response_success(response)
        assert body['data'] == None

    finally:
        if brand_id is not None and delete is False:
            brand_delete(api_session,brand_id)

@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('品牌删除')
@allure.title('删除品牌时输入不存在的ids')
@pytest.mark.brand
def test_brand_delete_with_not_exist_id(api_session):
    brand_id = None
    delete = False
    try:
        brand_info = auto_create_brand_info()
        response = brand_create(api_session,brand_info)

        body = assert_response_success(response)
        assert body['data'] == 1

        response = brand_list_by_name(api_session,brand_info['name'])

        body = assert_page_total(response,1)

        for i in body['data']['list']:
            if i['name'] == brand_info['name']:
                brand_id = i['id']

        response = brand_delete(api_session,brand_id+1000)

        assert_business_error(response,500,None)

        delete = False

        response = brand_get_info_by_id(api_session,brand_id)

        body = assert_response_success(response)
        assert body['data']['name'] == brand_info['name']

    finally:
        if brand_id is not None and delete is False:
            brand_delete(api_session,brand_id)