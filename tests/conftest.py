import pytest
import allure
from api.login_api import create_authorized_session


@pytest.fixture(scope="session")
def api_session():
    session = create_authorized_session()
    yield session
    session.close()

    