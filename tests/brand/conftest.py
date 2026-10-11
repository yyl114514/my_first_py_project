import pytest
from api.brand_api import brand_create,brand_delete,auto_create_brand_info,brand_list_by_name
@pytest.fixture
def add_temp_brand(api_session):
    brand_id = None
    brand_name = None
    brand_firstLetter = None
    
    try:
        brand_info = auto_create_brand_info()
        response = brand_create(api_session,brand_info)

        assert response.status_code == 200

        body = response.json()
        assert body['code'] == 200
        assert body['data'] == 1

        response = brand_list_by_name(api_session,brand_info['name'])

        assert response.status_code == 200
        
        body = response.json()
        assert body['code'] == 200

        assert body['data']['total'] == 1

        for i in body['data']['list']:
            if i['name'] == brand_info['name']:
                brand_id = i['id']
                brand_name = i['name']
                brand_firstLetter = i['firstLetter']

        assert brand_id is not None
        assert brand_name is not None
        assert brand_firstLetter is not None
        brand_info = {
            "name": brand_name,
            "firstLetter": brand_firstLetter,
            "id":brand_id
        }
        yield  brand_info

    finally:
        if brand_id is not None:
            brand_delete(api_session,brand_id)