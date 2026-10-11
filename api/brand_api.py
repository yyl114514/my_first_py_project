

import time
from config import BASE_URL


def auto_create_brand_info():

    timestamp = int(time.time())
    auto_name = f'auto_name_{timestamp}'
    auto_firstLetter = auto_name[0]

    auto_info = {
    "name": auto_name,
    "firstLetter": auto_firstLetter,
    "sort": 0,
    "factoryStatus": 0,
    "showStatus": 0,
    "logo": "string",
    "bigPic": "string",
    "brandStory": "string"
    }
    return auto_info

def brand_create(api_session,brand_info):
    response = api_session.post(
        f'{BASE_URL}/brand/create',
        json = brand_info,
        timeout = 5
    )
    return response

def brand_update(api_session,brand_info,brand_id):
    response = api_session.post(
        f'{BASE_URL}/brand/update/{brand_id}',
        json = brand_info,
        timeout = 5
    )
    return response

def brand_get_info_by_id(api_session,brand_id):
    response = api_session.get(
        f'{BASE_URL}/brand/{brand_id}',
        timeout = 5
    )
    return response

def brand_delete(api_session,brand_id):
    response = api_session.get(
        f'{BASE_URL}/brand/delete/{brand_id}',
        timeout = 5
    )
    return response

def brand_list_by_name(api_session,keyword = None,pageNum = 1,pageSize = 5):
    my_params = { ##如何传递参数：准备一个字典，左边的键名就是后端规定的名字
            "keyword" : keyword,
            "pageNum" : pageNum,
            "pageSize" : pageSize,
        }
    response = api_session.get(
        f'{BASE_URL}/brand/list',
        params = my_params,
        timeout = 5
    )
    return response
