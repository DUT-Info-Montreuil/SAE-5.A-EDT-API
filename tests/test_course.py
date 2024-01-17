from unittest.mock import patch
from services.course_service import course_service
import pytest

class TestCourseService:

    def test_return_all_courses(self, mocker):
        mocker.patch.object(course_service, 'execute_query_and_get_statement', return_value=[{'id': 1, 'name': 'Math'}, {'id': 2, 'name': 'Science'}])

        course_service_instance = course_service()

        courses = course_service_instance.get_courses()

        assert courses == [{'id': 1, 'name': 'Math'}, {'id': 2, 'name': 'Science'}]


    def test_return_empty_list(self, mocker):
        mocker.patch.object(course_service, 'execute_query_and_get_statement', return_value=[])

        course_service_instance = course_service()

        courses = course_service_instance.get_courses()

        assert courses == []

    def test_handle_query_failure(self, mocker):
        mocker.patch.object(course_service, 'execute_query_and_get_statement', side_effect=Exception('Query failed'))

        course_service_instance = course_service()

        courses = course_service_instance.get_courses()

        assert courses == 'Query failed'


    def test_handle_invalid_statement_format(self, mocker):
        mocker.patch.object(course_service, 'execute_query_and_get_statement', return_value='Invalid statement')

        course_service_instance = course_service()

        courses = course_service_instance.get_courses()

        assert courses == 'Invalid statement format'


    def test_handle_empty_query_string(self, mocker):
        mocker.patch.object(course_service, 'execute_query_and_get_statement', return_value=None)

        course_service_instance = course_service()

        courses = course_service_instance.get_courses()

        assert courses == 'Empty query string'

    def test_handle_empty_statement(self, mocker):
        mocker.patch.object(course_service, 'execute_query_and_get_statement', return_value=[])

        course_service_instance = course_service()

        courses = course_service_instance.get_courses()

        assert courses == 'Empty statement'