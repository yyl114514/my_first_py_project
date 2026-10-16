import pytest
import allure
from api.brand_api import brand_update,brand_get_info_by_id,brand_update_showStatus_batch
from common.assertions import assert_response_success
from common.assertions import assert_response_success
from api.brand_api import brand_update_factoryStatus_batch, brand_delete_batch

@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('批量删除品牌')
@allure.title('批量删除品牌成功')
@pytest.mark.brand
def test_brand_delete_batch(api_session,add_temp_brands):
    response = brand_delete_batch(api_session,add_temp_brands)

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 200
    assert body['message'] == '操作成功'
    assert body['data'] == len(add_temp_brands)

    for brand_id in add_temp_brands:
        response = brand_get_info_by_id(api_session,brand_id)
        body = assert_response_success(response)
        assert body['data'] == None

@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('批量删除品牌')
@allure.title('批量删除品牌时全部输入错误的ids(888,999)')
@pytest.mark.brand
def test_brand_delete_batch_with_all_not_exist_id(api_session,add_temp_brands):
    add_temp_brands = [888,999]
    response = brand_delete_batch(api_session,add_temp_brands)

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 500
    assert body['message'] == '操作失败'
    assert body['data'] == None

@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('批量删除品牌')
@allure.title('批量删除品牌时输入部分正确，部分错误的ids')
@pytest.mark.brand
def test_brand_delete_batch_with_part_not_exist_id(api_session,add_temp_brands):
    add_temp_brands.append(999)
    response = brand_delete_batch(api_session,add_temp_brands)

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 200
    assert body['message'] == '操作成功'
    assert body['data'] == len(add_temp_brands) - 1

    for brand_id in add_temp_brands:
        if brand_id != 999:
            response = brand_get_info_by_id(api_session,brand_id)
            body = assert_response_success(response)
            assert body['data'] == None
