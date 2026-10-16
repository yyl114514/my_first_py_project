import pytest
import allure
from api.brand_api import brand_update,brand_get_info_by_id,brand_update_showStatus_batch
from common.assertions import assert_response_success
from common.assertions import assert_response_success

@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('批量更新显示状态')
@allure.title('批量更新显示状态成功')
@pytest.mark.brand
def test_brand_update_showStatus_batch(api_session,add_temp_brands):
    new_showStatus = 0
    response = brand_update_showStatus_batch(api_session,new_showStatus,add_temp_brands)

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 200
    assert body['message'] == '操作成功'
    assert body['data'] == len(add_temp_brands)

    for brand_id in add_temp_brands:
        response = brand_get_info_by_id(api_session,brand_id)
        body = assert_response_success(response)
        assert body['data']["showStatus"] == new_showStatus


@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('批量更新显示状态')
@allure.title('批量更新显示状态时输入不存在的id(999)')
@pytest.mark.brand
def test_brand_update_showStatus_batch_with_not_exist_id(api_session,add_temp_brands):
    new_showStatus = 0
    add_temp_brands.append(999)
    response = brand_update_showStatus_batch(api_session,new_showStatus,add_temp_brands)

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 200
    assert body['message'] == '操作成功'
    assert body['data'] == len(add_temp_brands) - 1

    for brand_id in add_temp_brands:
        if brand_id != 999:
            response = brand_get_info_by_id(api_session,brand_id)
            body = assert_response_success(response)
            assert body['data']["showStatus"] == new_showStatus

@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('批量更新显示状态')
@allure.title('批量更新显示状态时showStatus为2')
@pytest.mark.xfail   ####真正的bug,接口没有做校验,所以这个用例是失败的,所以加上xfail标记
@pytest.mark.brand
def test_brand_update_showStatus_batch_with_showStatus_is_2(api_session,add_temp_brands):
    new_showStatus = 2
    response = brand_update_showStatus_batch(api_session,new_showStatus,add_temp_brands)

    assert response.status_code == 200

    body = response.json()
    assert body['code'] == 404
    assert body['message'] == 'showStatus显示状态不正确'

    for brand_id in add_temp_brands:
        response = brand_get_info_by_id(api_session,brand_id)
        body = assert_response_success(response)
        assert body['data']["showStatus"] != new_showStatus