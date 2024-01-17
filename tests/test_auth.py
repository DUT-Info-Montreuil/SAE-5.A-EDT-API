from unittest.mock import patch
from services.auth_service import auth_service
import pytest

class TestAuthService:

    def test_login_with_correct_username_and_password_returns_username(self):
        auth_service_instance = auth_service()

        data = {
            'username': 'john',
            'password': 'password123'
        }

        result = auth_service_instance.login(data)
        assert result == 'john'


    def test_login_with_correct_username_and_incorrect_password_returns_bad_username_or_password(self):
        auth_service_instance = auth_service()

        data = {
            'username': 'john',
            'password': 'wrongpassword'
        }

        result = auth_service_instance.login(data)
        assert result == 'Bad username or password'


    def test_login_with_incorrect_username_returns_bad_username_or_password(self):
        auth_service_instance = auth_service()

        data = {
            'username': 'nonexistent',
            'password': 'password123'
        }

        result = auth_service_instance.login(data)
        assert result == 'Bad username or password'


    def test_login_with_username_containing_special_characters_returns_bad_username_or_password(self):
        auth_service_instance = auth_service()

        data = {
            'username': 'user@name',
            'password': 'password123'
        }

        result = auth_service_instance.login(data)
        assert result == 'Bad username or password'


    def test_login_with_password_containing_special_characters_returns_bad_username_or_password(self):
        auth_service_instance = auth_service()

        data = {
            'username': 'john',
            'password': 'pass@word123'
        }

        result = auth_service_instance.login(data)
        assert result == 'Bad username or password'


    def test_login_with_username_longer_than_50_characters_returns_bad_username_or_password(self):
        auth_service_instance = auth_service()

        data = {
            'username': 'averylongusernamethatislongerthan50charactersandshouldreturnbadusernameorpassword',
            'password': 'password123'
        }

        result = auth_service_instance.login(data)
        assert result == 'Bad username or password'