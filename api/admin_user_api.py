from config import BASE_URL

def admin_register(api_session,request_data):
    response = api_session.post(
        f'{BASE_URL}/admin/register',
        json = request_data,
        timeout = 5
    )
    return response

def admin_delete(api_session,id):
    response =api_session.post(
        f"{BASE_URL}/admin/delete/{id}",
        timeout = 5
    )
    return response


def admin_list(api_session,keyword = None,pageSize =5,pageNum = 1):
    params = { ##如何传递参数：准备一个字典，左边的键名就是后端规定的名字
        "keyword" : keyword,
        "pageSize" : pageSize,
        "pageNum" : pageNum,
    }
    response =api_session.get(
        f'{BASE_URL}/admin/list',
        params = params,#然后令params = 字典名
        timeout = 5
        )
    return response

def admin_get_by_id(api_session,id):
    response = api_session.get(f'{BASE_URL}/admin/{id}',timeout = 5)
    return response

def admin_update(api_session,id,data):
    response = api_session.post(
        f'{BASE_URL}/admin/update/{id}',
        json = data,
        timeout = 5
        )
    return response

