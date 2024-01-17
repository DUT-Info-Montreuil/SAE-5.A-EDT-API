from unittest.mock import patch
from services.room_service import room_service
from configuration import connect_pg
import pytest


class TestRoomService:

    def test_get_rooms(self):
        room_service_obj = room_service()
        rooms = room_service_obj.get_rooms()
        assert isinstance(rooms, list)
        assert all(isinstance(room, dict) for room in rooms)

    def test_get_room_by_id(self):
        room_service_obj = room_service()
        room_id = 1
        room = room_service_obj.get_room_by_id(room_id)
        assert isinstance(room, dict)
        assert room['id'] == room_id

    def test_identify_room(self):
        room_service_obj = room_service()
        room_code = "A101"
        identified_rooms = room_service_obj.identify_room({'code': room_code})
        assert isinstance(identified_rooms, list)
        assert all(isinstance(room, dict) for room in identified_rooms)

    def test_get_room_by_id_nonexistent_id(self):
        room_service_obj = room_service()
        room_id = 100
        room = room_service_obj.get_room_by_id(room_id)
        assert room is None

    def test_identify_room_nonexistent_code(self):
        room_service_obj = room_service()
        room_code = "Z999"
        identified_rooms = room_service_obj.identify_room({'code': room_code})
        assert identified_rooms == []

    def test_add_room_existing_code(self):
        room_service_obj = room_service()
        existing_room_data = {
            'code': 'A101',
            'capacity': 50,
            'has_computer': True,
            'has_projector': False
        }
        new_room_id = room_service_obj.add_room(existing_room_data)
        assert new_room_id is None