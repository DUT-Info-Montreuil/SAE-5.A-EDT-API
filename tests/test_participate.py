from unittest.mock import patch
from services.participate_service import participate_service
from configuration import connect_pg
import pytest

class TestParticipateService:

    def test_get_participates(self, mocker):
        mocker.patch.object(participate_service, 'get_connection')
        participate_service.get_connection.return_value = 'connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = [('1', '1', '1'), ('2', '2', '2')]

        result = participate_service.get_participates()

        assert result == [{'id': '1', 'course_id': '1', 'subgroup_id': '1'}, {'id': '2', 'course_id': '2', 'subgroup_id': '2'}]

    def test_get_participate_by_id(self, mocker):
        mocker.patch.object(participate_service, 'get_connection')
        participate_service.get_connection.return_value = 'connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = [('1', '1', '1')]

        result = participate_service.get_participate_by_id(1)

        assert result == {'id': '1', 'course_id': '1', 'subgroup_id': '1'}

    def test_identify_participate(self, mocker):
        mocker.patch.object(participate_service, 'get_connection')
        participate_service.get_connection.return_value = 'connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = [('1', '1', '1'), ('2', '2', '2')]

        data = {'course_id': 1, 'subgroup_id': 1}
        result = participate_service.identify_participate(data)

        assert result == [{'id': '1', 'course_id': '1', 'subgroup_id': '1'}]

    def test_get_participate_by_invalid_id(self, mocker):
        mocker.patch.object(participate_service, 'get_connection')
        participate_service.get_connection.return_value = 'connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = []

        result = participate_service.get_participate_by_id(1)

        assert result == {}

    def test_identify_participate_with_invalid_data(self, mocker):
        mocker.patch.object(participate_service, 'get_connection')
        participate_service.get_connection.return_value = 'connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = []

        data = {'course_id': 1, 'subgroup_id': 1}
        result = participate_service.identify_participate(data)

        assert result == []

    def test_add_participate_with_missing_data(self, mocker):
        mocker.patch.object(participate_service, 'get_connection')
        participate_service.get_connection.return_value = 'connection'

        data = {'subgroup_id': 1}
        with pytest.raises(KeyError):
            participate_service.add_participate(data)

        data = {'course_id': 1}
        with pytest.raises(KeyError):
            participate_service.add_particip