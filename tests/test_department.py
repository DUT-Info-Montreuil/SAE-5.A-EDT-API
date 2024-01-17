from unittest.mock import patch
from services.department_service import department_service
import pytest


class TestDepartmentService:

    def test_get_departments(self):
        department_service_obj = department_service()
        departments = department_service_obj.get_departments()
        assert isinstance(departments, list)
        assert all(isinstance(department, dict) for department in departments)

    def test_get_department_by_id(self):
        department_service_obj = department_service()
        department = department_service_obj.get_department_by_id(1)
        assert isinstance(department, dict)


    def test_identify_department(self):
        department_service_obj = department_service()
        data = {
            'name': 'Computer Science',
            'degree_type': 'Bachelor'
        }
        identified_departments = department_service_obj.identify_department(data)
        assert isinstance(identified_departments, list)
        assert all(isinstance(department, dict) for department in identified_departments)

    def test_get_department_by_id_nonexistent(self):
        department_service_obj = department_service()
        department = department_service_obj.get_department_by_id(100)
        assert department is None


    def test_identify_department_no_match(self):
        department_service_obj = department_service()
        data = {
            'name': 'Nonexistent Department',
            'degree_type': 'Bachelor'
        }
        identified_departments = department_service_obj.identify_department(data)
        assert identified_departments == []


    def test_add_department_no_personal_id(self):
        department_service_obj = department_service()
        data = {
            'name': 'Mathematics',
            'description': 'Department of Mathematics',
            'degree_type': 'Bachelor'
        }
        with pytest.raises(Exception):
            department_service_obj.add_department(data)