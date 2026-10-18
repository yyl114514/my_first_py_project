import pytest
from api.brand_api import brand_update,brand_get_info_by_id
from data.factories import auto_create_brand_info
from common.assertions import assert_response_success,assert_page_total
import allure 
@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('根据编号查询品牌信息')
@allure.title('根据编号查询品牌信息成功')
@pytest.mark.brand
def test_brand_get_info_by_id(api_session,add_temp_brand):
    response = brand_get_info_by_id(api_session,add_temp_brand["id"])

    body = assert_response_success(response)

    assert body['data']['name'] == add_temp_brand['name']
    assert body['data']['firstLetter'] == add_temp_brand['firstLetter']


@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('根据编号查询品牌信息')
@allure.title('根据编号查询品牌信息时输入不存在的编号')
@pytest.mark.brand
def test_brand_get_info_by_id_with_not_exist_id(api_session,add_temp_brand):
    response = brand_get_info_by_id(api_session,add_temp_brand["id"]+1000)

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 200
    assert body['data'] == None