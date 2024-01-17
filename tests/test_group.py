from unittest.mock import patch
from services.group_service import group_service
import pytest

class TestGroupService:

    def test_get_groups_returns_list_of_all_groups(self):
        group_service_instance = group_service()
        groups = group_service_instance.get_groups()
        assert isinstance(groups, list)
        assert all(isinstance(group, dict) for group in groups)

    def test_get_group_by_id_returns_group_by_id(self):
        group_service_instance = group_service()
        group_id = 1
        group = group_service_instance.get_group_by_id(group_id)
        assert isinstance(group, dict)
        assert group['id'] == group_id

    def test_identify_group_identifies_group_by_promotion_and_type(self):
        group_service_instance = group_service()
        data = {
            'promotion': '2022',
            'department_id': '1'
        }
        identified_groups = group_service_instance.identify_group(data)
        assert isinstance(identified_groups, list)
        assert all(isinstance(group, dict) for group in identified_groups)

    def test_get_group_by_id_returns_none_if_group_does_not_exist(self):
        group_service_instance = group_service()
        group_id = 100
        group = group_service_instance.get_group_by_id(group_id)
        assert group is None

    def test_identify_group_returns_empty_list_if_no_group_matches(self):
        group_service_instance = group_service()
        data = {
            'promotion': '2025',
            'department_id': '4'
        }
        identified_groups = group_service_instance.identify_group(data)
        assert identified_groups == []

    def test_add_group_raises_error_if_department_id_does_not_exist(self):
        group_service_instance = group_service()
        new_group_data = {
            'promotion': '2023',
            'type': 'A',
            'department_id': '100'
        }
        with pytest.raises(Exception):
            group_service_instance.add_group(new_group_data)