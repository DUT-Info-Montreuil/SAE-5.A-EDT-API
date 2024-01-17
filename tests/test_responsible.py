from unittest.mock import patch
from services.responsible_service import responsible_service
from configuration import connect_pg
import pytest

class TestResponsibleService:

    def test_get_responsibles_returns_list_of_responsibles(self, mocker):
        mocker.patch.object(responsible_service, 'get_connection')
        responsible_service.get_connection.return_value = 'mock_connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = [('1', '1', '1'), ('2', '2', '2')]

        result = responsible_service.get_responsibles()

        assert result == [{'id': '1', 'personal_id': '1', 'teaching_id': '1'}, {'id': '2', 'personal_id': '2', 'teaching_id': '2'}]

    def test_get_responsible_by_id_returns_responsible_by_id(self, mocker):
        mocker.patch.object(responsible_service, 'get_connection')
        responsible_service.get_connection.return_value = 'mock_connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = [('1', '1', '1')]

        result = responsible_service.get_responsible_by_id(1)

        assert result == {'id': '1', 'personal_id': '1', 'teaching_id': '1'}

    def test_identify_responsible_identifies_responsible_by_personal_id_and_teaching_id(self, mocker):
        mocker.patch.object(responsible_service, 'get_connection')
        responsible_service.get_connection.return_value = 'mock_connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = [('1', '1', '1')]

        data = {'personal_id': 1, 'teaching_id': 1}
        result = responsible_service.identify_responsible(data)

        assert result == [{'id': '1', 'personal_id': '1', 'teaching_id': '1'}]

    def test_get_responsible_by_id_returns_none_if_no_responsible_found_with_given_id(self, mocker):
        mocker.patch.object(responsible_service, 'get_connection')
        responsible_service.get_connection.return_value = 'mock_connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = []

        result = responsible_service.get_responsible_by_id(1)

        assert result is None

    def test_identify_responsible_returns_empty_list_if_no_responsible_found_with_given_personal_id_and_teaching_id(self, mocker):
        mocker.patch.object(responsible_service, 'get_connection')
        responsible_service.get_connection.return_value = 'mock_connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = []

        data = {'personal_id': 1, 'teaching_id': 1}
        result = responsible_service.identify_responsible(data)

        # Assert the result
        assert result == []
