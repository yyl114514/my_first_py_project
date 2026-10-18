import pytest
import allure
from api.brand_api import brand_get_info_by_id
from common.assertions import assert_response_success
from common.assertions import assert_response_success
from api.brand_api import brand_update_factoryStatus_batch

@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('批量更新厂家制造商状态')
@allure.title('批量更新厂家制造商状态成功')
@pytest.mark.brand
def test_brand_update_factoryStatus_batch(api_session,add_temp_brands):
    new_factoryStatus = 0
    response = brand_update_factoryStatus_batch(api_session,new_factoryStatus,add_temp_brands)

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 200
    assert body['message'] == '操作成功'
    assert body['data'] == len(add_temp_brands)

    for brand_id in add_temp_brands:
        response = brand_get_info_by_id(api_session,brand_id)
        body = assert_response_success(response)
        assert body['data']["factoryStatus"] == new_factoryStatus

@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('批量更新厂家制造商状态')
@allure.title('批量更新厂家制造商状态时输入不存在的ids(999)')
@pytest.mark.brand
def test_brand_update_factoryStatus_batch_with_not_exist_id(api_session,add_temp_brands):
    new_factoryStatus = 0
    add_temp_brands.append(999)
    response = brand_update_factoryStatus_batch(api_session,new_factoryStatus,add_temp_brands)

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 200
    assert body['message'] == '操作成功'
    assert body['data'] == len(add_temp_brands) - 1

    for brand_id in add_temp_brands:
        if brand_id != 999:
            response = brand_get_info_by_id(api_session,brand_id)
            body = assert_response_success(response)
            assert body['data']["factoryStatus"] == new_factoryStatus

@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('批量更新厂家制造商状态')
@allure.title('批量更新厂家制造商状态时factoryStatus=2')
@pytest.mark.xfail(
    strict=True,
    reason="BUG-002:批量更新 factoryStatus 未校验非法值",
)
@pytest.mark.brand
def test_brand_update_factoryStatus_batch_with_factoryStatus_is_2(api_session,add_temp_brands):
    new_factoryStatus = 2
    response = brand_update_factoryStatus_batch(api_session,new_factoryStatus,add_temp_brands)

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 404
    assert body['message'] == '操作失败'
    assert body['data'] == len(add_temp_brands)

    for brand_id in add_temp_brands:
        response = brand_get_info_by_id(api_session,brand_id)
        body = assert_response_success(response)
        assert body['data']["factoryStatus"] != new_factoryStatus

