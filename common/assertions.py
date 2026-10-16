
def assert_response(response,expected_code):
    assert response.status_code == expected_code


def assert_response_success(response):
    assert response.status_code == 200
    body = response.json()
    assert body['code'] == 200
    return body

def assert_business_error(response, expected_code, expected_data):
    assert response.status_code == 200
    body = response.json()
    assert body['code'] == expected_code
    assert body['data'] == expected_data
    return body

def assert_response_data(response, expected_data=1):
    assert response.status_code == 200
    body = response.json()
    assert body['code'] == 200
    assert body['data'] == expected_data
    return body

def assert_response_data_is_null(response):
    assert response.status_code == 200
    body = response.json()
    assert body['code'] == 200
    assert body['data'] is None
    return body

def assert_page_total(response, expected_total):
    assert response.status_code == 200
    body = response.json()
    assert body['code'] == 200
    assert body['data']['total'] == expected_total
    return body