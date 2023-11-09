class CourseModel:
    def __init__(self, id, description, startTime, duree, course_type, personal_id, rooms_id, teaching_id, personal_last_name, personal_first_name, teaching_title, room_code):
        self.id = id
        self.description = description
        self.startTime = startTime
        self.duree = duree
        self.course_type = course_type
        self.personal_id = personal_id
        self.rooms_id = rooms_id
        self.teaching_id = teaching_id
        
        # personal
        self.personal_last_name = personal_last_name
        self.personal_first_name = personal_first_name
        
        # teaching
        self.teaching_title = teaching_title
        
        # room
        self.room_code = room_code
        
    def __str__(self):
        return "Course id: %s, description: %s" % (self.id, self.description)

    def jsonify(self):
        return {
            "id": self.id,
            "description": self.description,
            "startTime": str(self.startTime),
            "duree": str(self.duree),
            "course_type": self.course_type,
            "personal_id": self.personal_id,
            "rooms_id": self.rooms_id,
            "teaching_id": self.teaching_id,
            "personal_last_name": self.personal_last_name,
            "personal_first_name": self.personal_first_name,
            "teaching_title": self.teaching_title,
            "room_code": self.room_code
        }
