from unittest.mock import patch
from services.subgroup_service import subgroup_service
from configuration import connect_pg
import pytest

class TestSubgroupService:

    def test_get_subgroups(self, mocker):
        mocker.patch.object(subgroup_service, 'get_connection')
        subgroup_service.get_connection.return_value = mocker.Mock()

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = [('1', 'Subgroup 1', '1'), ('2', 'Subgroup 2', '2')]

        result = subgroup_service.get_subgroups()

        assert result == [{'id': '1', 'name': 'Subgroup 1', 'group_id': '1'}, {'id': '2', 'name': 'Subgroup 2', 'group_id': '2'}]

    def test_get_subgroup_by_id(self, mocker):
        mocker.patch.object(subgroup_service, 'get_connection')
        subgroup_service.get_connection.return_value = mocker.Mock()

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = [('1', 'Subgroup 1', '1')]

        result = subgroup_service.get_subgroup_by_id(1)

        assert result == {'id': '1', 'name': 'Subgroup 1', 'group_id': '1'}

    def test_get_subgroup_by_group_id(self, mocker):
        mocker.patch.object(subgroup_service, 'get_connection')
        subgroup_service.get_connection.return_value = mocker.Mock()

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = [('1', 'Subgroup 1', '1'), ('2', 'Subgroup 2', '1')]

        result = subgroup_service.get_subgroup_by_group_id(1)

        assert result == [{'id': '1', 'name': 'Subgroup 1', 'group_id': '1'}, {'id': '2', 'name': 'Subgroup 2', 'group_id': '1'}]

    def test_get_subgroup_by_id_nonexistent(self, mocker):
        mocker.patch.object(subgroup_service, 'get_connection')
        subgroup_service.get_connection.return_value = mocker.Mock()

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = []

        result = subgroup_service.get_subgroup_by_id(1)

        assert result is None

    def test_identify_subgroup_nonexistent(self, mocker):
        mocker.patch.object(subgroup_service, 'get_connection')
        subgroup_service.get_connection.return_value = mocker.Mock()

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = []

        result = subgroup_service.identify_subgroup({'name': 'Nonexistent Subgroup', 'group_id': 1})

        assert result == []