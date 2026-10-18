import pytest
from api.brand_api import brand_update,brand_get_info_by_id,brand_list_by_name,brand_create,brand_delete
from data.factories import auto_create_brand_info
from common.assertions import assert_response_success,assert_page_total
import allure 
@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('根据品牌名称分页获取品牌列表')
@allure.title('根据品牌名称分页获取品牌列表成功')
@pytest.mark.brand
def test_brand_list_by_name(api_session):
    brand_ids = []
    brand_names = []
    special_characters = 'の'
    try:
        for i in range(3):
            brand_info = auto_create_brand_info()
            brand_info['name'] = f"{special_characters}{i+1}"
            brand_names.append(brand_info['name'])
            response = brand_create(api_session,brand_info)

            assert_response_success(response)

        response = brand_list_by_name(api_session,special_characters)
        
        body = assert_page_total(response,3)

        for i in body['data']['list']:
            if i['name'] in brand_names:
                brand_ids.append(i['id'])
        
    finally:
        for id in brand_ids:
            if id is not None:
                brand_delete(api_session,id)


@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('根据品牌名称分页获取品牌列表')
@allure.title('根据不存在的品牌名称分页查询返回空列表')
@pytest.mark.brand
def test_brand_list_by_name_with_not_exist_keyword(api_session):
    response = brand_list_by_name(api_session,'不存在的品牌名称')

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 200
    assert body['data']['total'] == 0
    assert body['data']['list'] == []


@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('根据品牌名称分页获取品牌列表')
@allure.title('使用 showStatus=2 过滤品牌列表的行为')
@pytest.mark.brand
def test_brand_list_by_name_with_showStatus_is_2(api_session):
    brand_ids = []
    brand_names = []
    special_characters = 'の'
    try:
        for i in range(3):
            brand_info = auto_create_brand_info()
            brand_info['name'] = f"{special_characters}{i+1}"
            brand_names.append(brand_info['name'])
            response = brand_create(api_session,brand_info)

            assert_response_success(response)
        response = brand_list_by_name(api_session,special_characters)
        body = assert_page_total(response,3)

        for i in body['data']['list']:
            if i['name'] in brand_names:
                brand_ids.append(i['id'])

        response = brand_list_by_name(api_session,special_characters,showStatus=2)

        body = assert_page_total(response,0)
        
    finally:
        for id in brand_ids:
            if id is not None:
                brand_delete(api_session,id)

@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('根据品牌名称分页获取品牌列表')
@allure.title('页码超过最后一页时返回空列表但 total 不变')
@pytest.mark.brand
def test_brand_list_by_name_with_pageNum_exceed_last_page(api_session):
    brand_ids = []
    brand_names = []
    special_characters = 'の'
    try:
        for i in range(3):
            brand_info = auto_create_brand_info()
            brand_info['name'] = f"{special_characters}{i+1}"
            brand_names.append(brand_info['name'])
            response = brand_create(api_session,brand_info)

            assert_response_success(response)
        response = brand_list_by_name(api_session,special_characters)
        body = assert_page_total(response,3)

        for i in body['data']['list']:
            if i['name'] in brand_names:
                brand_ids.append(i['id'])

        response = brand_list_by_name(api_session,special_characters,pageNum=999)

        body = assert_page_total(response,3)
        assert body['data']['list'] == []

        
    finally:
        for id in brand_ids:
            if id is not None:
                brand_delete(api_session,id)

@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('根据品牌名称分页获取品牌列表')
@allure.title('页码为 0 时分页参数处理')
@pytest.mark.xfail(strict=True,reason='页码为 0是非法的应该报错')
@pytest.mark.brand
def test_brand_list_by_name_with_pageNum_is_0(api_session):
    brand_ids = []
    brand_names = []
    special_characters = 'の'
    try:
        for i in range(3):
            brand_info = auto_create_brand_info()
            brand_info['name'] = f"{special_characters}{i+1}"
            brand_names.append(brand_info['name'])
            response = brand_create(api_session,brand_info)

            assert_response_success(response)

        response = brand_list_by_name(api_session,special_characters)
        
        body = assert_page_total(response,3)
        
        for i in body['data']['list']:
            if i['name'] in brand_names:
                brand_ids.append(i['id'])

        response = brand_list_by_name(api_session,special_characters,pageNum=0)

        assert response.status_code == 200
        body = response.json()
        assert body["code"] == 404
        assert body["data"] is None
        
    finally:
        for id in brand_ids:
            if id is not None:
                brand_delete(api_session,id)

@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('根据品牌名称分页获取品牌列表')
@allure.title('每页数量为 0 时分页参数处理')
@pytest.mark.xfail(strict=True,reason='每页数量为 0 是非法的应该报错')
@pytest.mark.brand
def test_brand_list_by_name_with_pageSize_is_0(api_session):
    brand_ids = []
    brand_names = []
    special_characters = 'の'
    try:
        for i in range(3):
            brand_info = auto_create_brand_info()
            brand_info['name'] = f"{special_characters}{i+1}"
            brand_names.append(brand_info['name'])
            response = brand_create(api_session,brand_info)

            assert_response_success(response)

        response = brand_list_by_name(api_session,special_characters)
        body = assert_page_total(response,3)

        for i in body['data']['list']:
            if i['name'] in brand_names:
                brand_ids.append(i['id'])

        response = brand_list_by_name(api_session,special_characters,pageSize=0)

        assert response.status_code == 200
        body = response.json()
        assert body["code"] == 404
        assert body["data"] is None
        
    finally:
        for id in brand_ids:
            if id is not None:
                brand_delete(api_session,id)

@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('根据品牌名称分页获取品牌列表')
@allure.title('每页数量为负数时分页参数处理')
@pytest.mark.xfail(strict=True,reason='每页数量为负数是非法的应该报错')
@pytest.mark.brand
def test_brand_list_by_name_with_pageSize_is_negative(api_session):
    brand_ids = []
    brand_names = []
    special_characters = 'の'
    try:
        for i in range(3):
            brand_info = auto_create_brand_info()
            brand_info['name'] = f"{special_characters}{i+1}"
            brand_names.append(brand_info['name'])
            response = brand_create(api_session,brand_info)

            assert_response_success(response)

        response = brand_list_by_name(api_session,special_characters)
        body = assert_page_total(response,3)

        for i in body['data']['list']:
            if i['name'] in brand_names:
                brand_ids.append(i['id'])

        response = brand_list_by_name(api_session,special_characters,pageSize=-1)

        assert response.status_code == 200
        body = response.json()
        assert body["code"] == 404
        assert body["data"] is None

        
    finally:
        for id in brand_ids:
            if id is not None:
                brand_delete(api_session,id)