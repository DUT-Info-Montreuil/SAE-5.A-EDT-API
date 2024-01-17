from unittest.mock import patch
from services.specialization_service import specialization_service
from configuration import connect_pg
import pytest

class TestSpecializationService:

    def test_get_specializations(self, mocker):
        mocker.patch.object(specialization_service, 'get_connection')
        specialization_service.get_connection.return_value = 'connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = [('1', 'ABC', 'Specialization 1', '1'), ('2', 'DEF', 'Specialization 2', '2')]

        specialization_service_instance = specialization_service()

        specializations = specialization_service_instance.get_specializations()

        assert specializations == [{'id': '1', 'code': 'ABC', 'name': 'Specialization 1', 'department_id': '1'}, {'id': '2', 'code': 'DEF', 'name': 'Specialization 2', 'department_id': '2'}]

    def test_get_specialization_by_id(self, mocker):
        mocker.patch.object(specialization_service, 'get_connection')
        specialization_service.get_connection.return_value = 'connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = [('1', 'ABC', 'Specialization 1', '1')]

        specialization_service_instance = specialization_service()

        specialization = specialization_service_instance.get_specialization_by_id(1)

        assert specialization == {'id': '1', 'code': 'ABC', 'name': 'Specialization 1', 'department_id': '1'}

    def test_identify_specialization(self, mocker):
        mocker.patch.object(specialization_service, 'get_connection')
        specialization_service.get_connection.return_value = 'connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = [('1', 'ABC', 'Specialization 1', '1'), ('2', 'ABC', 'Specialization 2', '2')]

        specialization_service_instance = specialization_service()

        data = {'code': 'ABC'}
        identified_specializations = specialization_service_instance.identify_specialization(data)

        assert identified_specializations == [{'id': '1', 'code': 'ABC', 'name': 'Specialization 1', 'department_id': '1'}, {'id': '2', 'code': 'ABC', 'name': 'Specialization 2', 'department_id': '2'}]

    def test_get_specialization_by_id_nonexistent_id(self, mocker):
        mocker.patch.object(specialization_service, 'get_connection')
        specialization_service.get_connection.return_value = 'connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = []

        specialization_service_instance = specialization_service()

        specialization = specialization_service_instance.get_specialization_by_id(1)

        assert specialization == None

    def test_identify_specialization_nonexistent_code(self, mocker):
        mocker.patch.object(specialization_service, 'get_connection')
        specialization_service.get_connection.return_value = 'connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = []

        specialization_service_instance = specialization_service()

        data = {'code': 'XYZ'}
        identified_specializations = specialization_service_instance.identify_specialization(data)

        assert identified_specializations == []