import pytest
from api.brand_api import brand_list_all
from common.assertions import assert_response_success,assert_page_total
import allure 
@allure.epic('我的第一个pytest项目')
@allure.feature('品牌管理模块')
@allure.story('获取全部品牌列表')
@allure.title('获取全部品牌列表成功')
@pytest.mark.brand
def test_brand_list_all(api_session):
    response = brand_list_all(api_session)
    assert_response_success(response)
       