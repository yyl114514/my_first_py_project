import requests

from config import BASE_URL, USERNAME, PASSWORD


def create_authorized_session():
    session = requests.Session() #创建一个能保存状态的客户端对象

    response = session.post(
        f"{BASE_URL}/admin/login",
        json={
            "username": USERNAME,
            "password": PASSWORD,
        },
        timeout=5,
    )

    body = response.json()#response只是字符串，把 JSON 字符串解析成 Python 对象,login_body 就变成了字典

    if response.status_code != 200:
        raise RuntimeError(f"HTTP请求失败: {response.status_code}")

    if body.get("code") != 200:
        raise RuntimeError(f"登录失败: {body.get('message')}")

    authorization = body["data"]["tokenHead"] + body["data"]["token"]

    session.headers.update({
        "Authorization": authorization,
    })

    return session
