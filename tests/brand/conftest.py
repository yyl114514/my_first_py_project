import pytest
from api.brand_api import brand_create,brand_delete,brand_list_by_name
from data.factories import auto_create_brand_info
from common.assertions import assert_response_success,assert_page_total
@pytest.fixture
def add_temp_brand(api_session):##pytest的fixture函数,返回一个字典,里面包含了品牌的id、name、firstLetter
    brand_id = None
    brand_name = None
    brand_firstLetter = None

    try:
        brand_info = auto_create_brand_info()
        response = brand_create(api_session,brand_info)

        assert_response_success(response)

        response = brand_list_by_name(api_session,brand_info['name'])


        body = assert_page_total(response,1)

        for i in body['data']['list']:
            if i['name'] == brand_info['name']:
                brand_id = i['id']
                brand_name = i['name']
                brand_firstLetter = i['firstLetter']

        assert brand_id is not None
        assert brand_name is not None
        assert brand_firstLetter is not None

        brand_info ['name'] = brand_name
        brand_info ['firstLetter'] = brand_firstLetter
        brand_info ['id'] = brand_id

        yield  brand_info

    finally:
        if brand_id is not None:
            brand_delete(api_session,brand_id)

@pytest.fixture
def add_temp_brands(api_session):#一次创建3条临时数据,返回一个数组,里面包含了3个id
    brand_ids = []
    try:
        for i in range(3):
            brand_info = auto_create_brand_info()
            response = brand_create(api_session,brand_info)

            assert_response_success(response)

            response = brand_list_by_name(api_session,brand_info['name'])

            body = assert_page_total(response,1)

            for i in body['data']['list']:
                if i['name'] == brand_info['name']:
                    brand_ids.append(i['id'])
        yield  brand_ids

    finally:
        for id in brand_ids:
            if id is not None:
                brand_delete(api_session,id)