from unittest.mock import patch
from services.rooms_courses_service import rooms_courses_service
from configuration import connect_pg
import pytest

class TestRoomsCoursesService:

    def test_get_all_rooms_courses(self):
        rooms_courses_service_obj = rooms_courses_service()
        all_rooms_courses = rooms_courses_service_obj.get_rooms_courses()
        assert isinstance(all_rooms_courses, list)
        assert len(all_rooms_courses) > 0

    def test_get_specific_rooms_courses(self):
        rooms_courses_service_obj = rooms_courses_service()
        rooms_courses_id = 1
        specific_rooms_courses = rooms_courses_service_obj.get_rooms_courses_by_id(rooms_courses_id)
        assert isinstance(specific_rooms_courses, dict)
        assert specific_rooms_courses != {}

    def test_add_new_rooms_courses(self):
        rooms_courses_service_obj = rooms_courses_service()
        new_rooms_courses_data = {
            'course_id': 2,
            'rooms_id': 3
        }
        new_rooms_courses_id = rooms_courses_service_obj.add_rooms_courses(new_rooms_courses_data)
        assert isinstance(new_rooms_courses_id, int)

    def test_get_empty_rooms_courses(self):
        rooms_courses_service_obj = rooms_courses_service()
        all_rooms_courses = rooms_courses_service_obj.get_rooms_courses()
        assert isinstance(all_rooms_courses, list)
        assert len(all_rooms_courses) == 0

    def test_get_nonexistent_rooms_courses(self):
        rooms_courses_service_obj = rooms_courses_service()
        rooms_courses_id = 9999
        specific_rooms_courses = rooms_courses_service_obj.get_rooms_courses_by_id(rooms_courses_id)
        assert isinstance(specific_rooms_courses, dict)
        assert specific_rooms_courses == {}

    def test_add_invalid_rooms_courses(self):
        rooms_courses_service_obj = rooms_courses_service()
        new_rooms_courses_data = {
            'rooms_id': 3
        }
        new_rooms_courses_id = rooms_courses_service_obj.add_rooms_courses(new_rooms_courses_data)
        assert new_rooms_courses_id is None

        new_rooms_courses_data = {
            'course_id': 2
        }
        new_rooms_courses_id = rooms_courses_service_obj.add_rooms_courses(new_rooms_courses_data)
        assert new_rooms_courses_id is None