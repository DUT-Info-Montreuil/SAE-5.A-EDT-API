from unittest.mock import patch
from services.teaching_service import teaching_service
from configuration import connect_pg
import pytest

class TestTeachingService:

    def test_get_all_teachings_returns_list_of_all_teachings(self, mocker):
        mocker.patch.object(teaching_service, 'get_connection')
        teaching_service.get_connection.return_value = 'connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = [('1', 'Math', 4, 1, 'A', 'Intro to Math', 'blue', 'lecture', 2), ('2', 'Physics', 3, 2, 'B', 'Intro to Physics', 'red', 'lab', 1)]

        teaching_service_instance = teaching_service()

        result = teaching_service_instance.get_teachings()

        assert isinstance(result, list)
        assert len(result) == 2
        assert result[0]['id'] == '1'
        assert result[0]['title'] == 'Math'
        assert result[0]['hour_number'] == 4
        assert result[0]['semestre'] == 1
        assert result[0]['sequence'] == 'A'
        assert result[0]['description'] == 'Intro to Math'
        assert result[0]['color'] == 'blue'
        assert result[0]['teaching_type'] == 'lecture'
        assert result[0]['specialization_id'] == 2
        assert result[1]['id'] == '2'
        assert result[1]['title'] == 'Physics'
        assert result[1]['hour_number'] == 3
        assert result[1]['semestre'] == 2
        assert result[1]['sequence'] == 'B'
        assert result[1]['description'] == 'Intro to Physics'
        assert result[1]['color'] == 'red'
        assert result[1]['teaching_type'] == 'lab'
        assert result[1]['specialization_id'] == 1

    def test_get_teaching_by_id_returns_teaching_by_id(self, mocker):
        mocker.patch.object(teaching_service, 'get_connection')
        teaching_service.get_connection.return_value = 'connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = [('1', 'Math', 4, 1, 'A', 'Intro to Math', 'blue', 'lecture', 2)]

        teaching_service_instance = teaching_service()

        result = teaching_service_instance.get_teaching_by_id(1)

        assert isinstance(result, dict)
        assert result['id'] == '1'
        assert result['title'] == 'Math'
        assert result['hour_number'] == 4
        assert result['semestre'] == 1
        assert result['sequence'] == 'A'
        assert result['description'] == 'Intro to Math'
        assert result['color'] == 'blue'
        assert result['teaching_type'] == 'lecture'
        assert result['specialization_id'] == 2

    def test_identify_teaching_returns_teaching_by_attributes(self, mocker):
        mocker.patch.object(teaching_service, 'get_connection')
        teaching_service.get_connection.return_value = 'connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = [('1', 'Math', 4, 1, 'A', 'Intro to Math', 'blue', 'lecture', 2)]

        teaching_service_instance = teaching_service()

        teaching_data = {
            'title': 'Math',
            'hour_number': 4,
            'semestre': 1,
            'sequence': 'A',
            'specialization_id': 2
        }
        result = teaching_service_instance.identify_teaching(teaching_data)