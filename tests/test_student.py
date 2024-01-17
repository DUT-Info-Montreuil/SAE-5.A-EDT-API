from unittest.mock import patch
from services.student_service import student_service
from configuration import connect_pg

class TestStudentService:

    def test_get_students_returns_list_of_students(self, mocker):
        mocker.patch.object(student_service, 'get_connection')
        student_service.get_connection.return_value = 'connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = [('1', 'Doe', 'John', '1', '1', '1')]

        service = student_service()

        result = service.get_students()

        assert result == [{'id': '1', 'last_name': 'Doe', 'first_name': 'John', 'user_id': '1', 'department_id': '1', 'group_id': '1', 'subgroup_id': '1'}]


    def test_get_student_by_id_returns_student_by_id(self, mocker):
        mocker.patch.object(student_service, 'get_connection')
        student_service.get_connection.return_value = 'connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = [('1', 'Doe', 'John', '1', '1', '1')]

        service = student_service()

        result = service.get_student_by_id(1)

        assert result == {'id': '1', 'last_name': 'Doe', 'first_name': 'John', 'user_id': '1', 'department_id': '1', 'group_id': '1', 'subgroup_id': '1'}


    def test_get_student_by_department_returns_list_of_students_by_department_id(self, mocker):
        mocker.patch.object(student_service, 'get_connection')
        student_service.get_connection.return_value = 'connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = [('1', 'Doe', 'John', '1', '1', '1')]

        service = student_service()

        result = service.get_student_by_department(1)

        assert result == [{'id': '1', 'last_name': 'Doe', 'first_name': 'John', 'user_id': '1', 'department_id': '1', 'group_id': '1', 'subgroup_id': '1'}]


    def test_get_students_returns_empty_list_if_no_students(self, mocker):
        mocker.patch.object(student_service, 'get_connection')
        student_service.get_connection.return_value = 'connection'

        mocker.patch.object(connect_pg, 'get_query')
        connect_pg.get_query.return_value = []

        service = student_service()

        result = service.get_students()

        assert result == []

    def test_get_student_by_id_returns_none_if_student_id_does_not_exist(self, mocker):
        mocker.patch.object(student_service, 'get_connection')
        student_service.get_connection.return_value = 'connection'

        mocker.patch