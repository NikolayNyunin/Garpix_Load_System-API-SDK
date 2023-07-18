import pytest
from configparser import ConfigParser

from auth import login, AuthenticationError

config = ConfigParser()
config.read('../config.ini')
USERNAME = config.get('user_info', 'username')
PASSWORD = config.get('user_info', 'password')


# noinspection PyArgumentList, PyTypeChecker
class TestLogin:
    def test_login_correct(self):
        tokens = login(USERNAME, PASSWORD)
        assert isinstance(tokens, dict)
        assert 'access_token' in tokens and 'refresh_token' in tokens \
               and 'token_type' in tokens and 'access_token_expires' in tokens \
               and 'refresh_token_expires' in tokens

    def test_login_incorrect(self):
        with pytest.raises(AuthenticationError):
            login('test', 'test')

    def test_login_wrong_types_1(self):
        with pytest.raises(TypeError):
            login('test', 15)

    def test_login_wrong_types_2(self):
        with pytest.raises(TypeError):
            login(10, True)

    def test_login_incomplete_1(self):
        with pytest.raises(TypeError):
            login('test')

    def test_login_incomplete_2(self):
        with pytest.raises(TypeError):
            login()

    def test_login_wrong_type_and_incomplete(self):
        with pytest.raises(TypeError):
            login(5.0)
