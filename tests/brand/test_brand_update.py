import pytest
from api.brand_api import brand_update,brand_get_info_by_id
from data.factories import auto_create_brand_info
from common.assertions import assert_response_success,assert_page_total
import allure 
@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('品牌修改')
@allure.title('品牌信息修改成功')
@pytest.mark.brand
def test_brand_update(api_session,add_temp_brand):
    new_name ='abcde'
    new_brand_info = auto_create_brand_info()
    new_brand_info['name'] = new_name

    response = brand_update(api_session,new_brand_info,add_temp_brand['id'])

    assert_response_success(response)

    response = brand_get_info_by_id(api_session,add_temp_brand["id"])

    body = assert_response_success(response)

    assert body['data']['name'] == new_name
    assert body['data']['firstLetter'] == 'a'


@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('品牌修改')
@allure.title('品牌信息更新时id不存在')
@pytest.mark.brand
def test_brand_update_id_not_exist(api_session,add_temp_brand):
    new_brand_info = auto_create_brand_info()
    new_brand_info['name'] = 'abcde'
    response = brand_update(api_session,new_brand_info,add_temp_brand['id']+1000)

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 500
    
@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('品牌修改')
@allure.title('品牌信息更新时name为空')
@pytest.mark.brand
def test_brand_update_name_is_null(api_session,add_temp_brand):
    new_brand_info = auto_create_brand_info()
    new_brand_info['name'] = ""
    response = brand_update(api_session,new_brand_info,add_temp_brand['id'])

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 404
    assert body['message'] == 'name不能为空'

    response = brand_get_info_by_id(api_session,add_temp_brand["id"])
    body = assert_response_success(response)
    assert body['data']['name'] == add_temp_brand['name']

@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('品牌修改')
@allure.title('更新品牌时factoryStatus=2')
@pytest.mark.brand
def test_brand_update_factoryStatus_is_2(api_session,add_temp_brand):
    new_brand_info = auto_create_brand_info()
    new_brand_info['name'] = 'abcde'
    new_brand_info["factoryStatus"] = 2
    response = brand_update(api_session,new_brand_info,add_temp_brand['id'])

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 404
    assert body['message'] == 'factoryStatus厂家状态不正确'

    response = brand_get_info_by_id(api_session,add_temp_brand["id"])
    body = assert_response_success(response)
    assert body['data']["factoryStatus"] == add_temp_brand['factoryStatus']


@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('品牌修改')
@allure.title('更新品牌时sort=-1')
@pytest.mark.brand
def test_brand_update_sort_is_minus_1(api_session,add_temp_brand):
    new_brand_info = auto_create_brand_info()
    new_brand_info['name'] = 'abcde'
    new_brand_info["sort"] = -1
    response = brand_update(api_session,new_brand_info,add_temp_brand['id'])

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 404
    assert body['message'] == 'sort最小不能小于0'

    response = brand_get_info_by_id(api_session,add_temp_brand["id"])
    body = assert_response_success(response)
    assert body['data']["sort"] == add_temp_brand['sort']

@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('品牌修改')
@allure.title('更新品牌时showStatus=2')
@pytest.mark.brand
def test_brand_update_showStatus_is_2(api_session,add_temp_brand):
    new_brand_info = auto_create_brand_info()
    new_brand_info['name'] = 'abcde'
    new_brand_info["showStatus"] = 2
    response = brand_update(api_session,new_brand_info,add_temp_brand['id'])

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 404
    assert body['message'] == 'showStatus显示状态不正确'

    response = brand_get_info_by_id(api_session,add_temp_brand["id"])
    body = assert_response_success(response)
    assert body['data']["showStatus"] == add_temp_brand['showStatus']

@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('品牌修改')
@allure.title('更新品牌时logo为空')
@pytest.mark.brand
def test_brand_update_logo_is_null(api_session,add_temp_brand):
    new_brand_info = auto_create_brand_info()
    new_brand_info['name'] = 'abcde'
    new_brand_info["logo"] = ""
    response = brand_update(api_session,new_brand_info,add_temp_brand['id'])

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 404
    assert body['message'] == 'logo不能为空'

    response = brand_get_info_by_id(api_session,add_temp_brand["id"])
    body = assert_response_success(response)
    assert body['data']["logo"] == add_temp_brand['logo']

