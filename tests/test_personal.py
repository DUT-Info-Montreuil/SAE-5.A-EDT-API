from unittest.mock import patch
from services.personal_service import personal_service
import pytest

class TestPersonalService:

    def test_get_roles_existing_user(self, mocker):
        mocker.patch('services.personal_service.Service.get_connection')
        mocker.patch('services.personal_service.connect_pg.get_query', return_value=[('admin',)])

        personal_service_instance = personal_service()

        result = personal_service_instance.get_roles({'username': 'john_doe'})

        assert result == {'role': 'admin'}

    def test_total_hours_existing_personal(self, mocker):
        mocker.patch('services.personal_service.Service.get_connection')
        mocker.patch('services.personal_service.connect_pg.get_query', return_value=[(3600,)])

        personal_service_instance = personal_service()

        result = personal_service_instance.total_hours(1)

        assert result == {'temps': 60}

    def test_get_personals(self, mocker):
        mocker.patch('services.personal_service.Service.get_connection')
        mocker.patch('services.personal_service.connect_pg.get_query', return_value=[(1, 'Doe', 'John', 'JD123', 'admin', 1), (2, 'Smith', 'Jane', 'JS456', 'user', 2)])

        personal_service_instance = personal_service()

        result = personal_service_instance.get_personals()

        assert result == [{'id': 1, 'last_name': 'Doe', 'first_name': 'John', 'personal_code': 'JD123', 'roles': 'admin', 'user_id': 1}, {'id': 2, 'last_name': 'Smith', 'first_name': 'Jane', 'personal_code': 'JS456', 'roles': 'user', 'user_id': 2}]

    def test_get_roles_non_existing_user(self, mocker):
        mocker.patch('services.personal_service.Service.get_connection')
        mocker.patch('services.personal_service.connect_pg.get_query', return_value=[])

        personal_service_instance = personal_service()

        result = personal_service_instance.get_roles({'username': 'john_doe'})

        assert result is None

    def test_total_hours_no_courses(self, mocker):
        mocker.patch('services.personal_service.Service.get_connection')
        mocker.patch('services.personal_service.connect_pg.get_query', return_value=[(None,)])

        personal_service_instance = personal_service()

        result = personal_service_instance.total_hours(1)

        assert result == {}

    def test_get_personal_by_id_non_existing_personal(self, mocker):
        mocker.patch('services.personal_service.Service.get_connection')
        mocker.patch('services.personal_service.connect_pg.get_query', return_value=[])

        personal_service_instance = personal_service()

        result = personal_service_instance.get_personal_by_id(1)

        assert result == {}