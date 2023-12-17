from services.sql_alchemy_service import db
from configuration import connect_pg
from entities.models.models import *

class Service:
    connection = None

    def get_connection(self):
        if(self.connection == None):
            self.connection = connect_pg.connect()
        return self.connection

    def connect(self):
        self.connection = connect_pg.connect()
        
    def disconnect(self):
        connect_pg.disconnect(self.connection)
        self.connection = None
    
    # === region : User ===

    def get_all_users(self):
        users = User.query.all()
        user_list = []

        for user in users:
            user_data = user.get_json()
            user_list.append(user_data)

        return user_list
    
    def get_user_by_id(self, user_id):
        user = User.query.get(user_id)

        if user:
            user_data = user.get_json()
            return user_data
        else:
            return None
    
    def find_user(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        users = User.query.filter_by(**conditions)

        user_list = []

        for user in users:
            user_list.append(user.get_json())

        return user_list
    
    def delete_user(self, user_id):
        user = User.query.get(user_id)

        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        else:
            return False
    
    def update_user(self, user_id, new_data):
        user = User.query.get(user_id)

        if user:
            for key, value in new_data.items():
                setattr(user, key, value)

            db.session.commit()
            return True
        else:
            return False
    # === endregion : User ===


    # === region : Student ===

    def get_all_students(self):
        students = Student.query.all()
        student_list = []

        for student in students:
            student_data = student.get_json()
            student_list.append(student_data)

        return student_list
    
    def get_student_by_id(self, student_id):
        student = Student.query.get(student_id)

        if student:
            student_data = student.get_json()
            return student_data
        else:
            return None
    
    def find_student(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        students = Student.query.filter_by(**conditions)

        student_list = []

        for student in students:
            student_list.append(student.get_json())

        return student_list
    
    def delete_student(self, student_id):
        student = Student.query.get(student_id)

        if student:
            db.session.delete(student)
            db.session.commit()
            return True
        else:
            return False
    
    def update_student(self, student_id, new_data):
        student = Student.query.get(student_id)

        if student:
            for key, value in new_data.items():
                setattr(student, key, value)

            db.session.commit()
            return True
        else:
            return False
    # === endregion : Student ===

    # === region : Department ===
    def get_all_departments(self):
        departments = Department.query.all()
        department_list = []

        for department in departments:
            department_data = department.get_json()
            department_list.append(department_data)

        return department_list
    
    def get_department_by_id(self, department_id):
        department = Department.query.get(department_id)

        if department:
            department_data = department.get_json()
            return department_data
        else:
            return None
    
    def find_department(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        departments = Department.query.filter_by(**conditions)

        department_list = []

        for department in departments:
            department_list.append(department.get_json())

        return department_list
    
    def delete_department(self, department_id):
        department = Department.query.get(department_id)

        if department:
            db.session.delete(department)
            db.session.commit()
            return True
        else:
            return False
    
    def update_department(self, department_id, new_data):
        department = Department.query.get(department_id)

        if department:
            for key, value in new_data.items():
                setattr(department, key, value)

            db.session.commit()
            return True
        else:
            return False
    # === endregion : Department ===

    
    # === region : Group ===
    def get_all_groups(self):
        groups = Group.query.all()
        group_list = []

        for group in groups:
            group_data = group.get_json()
            group_list.append(group_data)

        return group_list
    
    def get_group_by_id(self, group_id):
        group = Group.query.get(group_id)

        if group:
            group_data = group.get_json()
            return group_data
        else:
            return None
    
    def find_group(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        groups = Group.query.filter_by(**conditions)

        group_list = []

        for group in groups:
            group_list.append(group.get_json())

        return group_list
    
    def delete_group(self, group_id):
        group = Group.query.get(group_id)

        if group:
            db.session.delete(group)
            db.session.commit()
            return True
        else:
            return False
    
    def update_group(self, group_id, new_data):
        group = Group.query.get(group_id)

        if group:
            for key, value in new_data.items():
                setattr(group, key, value)

            db.session.commit()
            return True
        else:
            return False
    # === endregion : Group ===


    # === region : Subgroup ===
    def get_all_subgroups(self):
        subgroups = Subgroup.query.all()
        subgroup_list = []

        for subgroup in subgroups:
            subgroup_data = subgroup.get_json()
            subgroup_list.append(subgroup_data)

        return subgroup_list
    
    def get_subgroup_by_id(self, subgroup_id):
        subgroup = Subgroup.query.get(subgroup_id)

        if subgroup:
            subgroup_data = subgroup.get_json()
            return subgroup_data
        else:
            return None
    
    def find_subgroup(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        subgroups = Subgroup.query.filter_by(**conditions)

        subgroup_list = []

        for subgroup in subgroups:
            subgroup_list.append(subgroup.get_json())

        return subgroup_list
    
    def delete_subgroup(self, subgroup_id):
        subgroup = Subgroup.query.get(subgroup_id)

        if subgroup:
            db.session.delete(subgroup)
            db.session.commit()
            return True
        else:
            return False
    
    def update_subgroup(self, subgroup_id, new_data):
        subgroup = Subgroup.query.get(subgroup_id)

        if subgroup:
            for key, value in new_data.items():
                setattr(subgroup, key, value)

            db.session.commit()
            return True
        else:
            return False
    # === endregion : Subgroup ===


    # === region : Personal ===
    def get_all_personals(self):
        personals = Personal.query.all()
        personal_list = []

        for personal in personals:
            personal_data = personal.get_json()
            personal_list.append(personal_data)

        return personal_list
    
    def get_personal_by_id(self, personal_id):
        personal = Personal.query.get(personal_id)

        if personal:
            personal_data = personal.get_json()
            return personal_data
        else:
            return None
    
    def find_personal(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        personals = Personal.query.filter_by(**conditions)

        personal_list = []

        for personal in personals:
            personal_list.append(personal.get_json())

        return personal_list
    
    def delete_personal(self, personal_id):
        personal = Personal.query.get(personal_id)

        if personal:
            db.session.delete(personal)
            db.session.commit()
            return True
        else:
            return False
    
    def update_personal(self, personal_id, new_data):
        personal = Personal.query.get(personal_id)

        if personal:
            for key, value in new_data.items():
                setattr(personal, key, value)

            db.session.commit()
            return True
        else:
            return False
    # === endregion : Personal ===

    
    # === region : Role ===
    def get_all_roles(self):
        roles = Role.query.all()
        role_list = []

        for role in roles:
            role_data = role.get_json()
            role_list.append(role_data)

        return role_list
    
    def get_role_by_id(self, role_id):
        role = Role.query.get(role_id)

        if role:
            role_data = role.get_json()
            return role_data
        else:
            return None
    
    def find_role(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        roles = Role.query.filter_by(**conditions)

        role_list = []

        for role in roles:
            role_list.append(role.get_json())

        return role_list
    
    def delete_role(self, role_id):
        role = Role.query.get(role_id)

        if role:
            db.session.delete(role)
            db.session.commit()
            return True
        else:
            return False
    
    def update_role(self, role_id, new_data):
        role = Role.query.get(role_id)

        if role:
            for key, value in new_data.items():
                setattr(role, key, value)

            db.session.commit()
            return True
        else:
            return False
    # === endregion : Role ===

    
    # === region : Course ===
    def get_all_courses(self):
        courses = Course.query.all()
        course_list = []

        for course in courses:
            course_data = course.get_json()
            course_list.append(course_data)

        return course_list
    
    def get_course_by_id(self, course_id):
        course = Course.query.get(course_id)

        if course:
            course_data = course.get_json()
            return course_data
        else:
            return None
    
    def find_course(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        courses = Course.query.filter_by(**conditions)

        course_list = []

        for course in courses:
            course_list.append(course.get_json())

        return course_list
    
    def delete_course(self, course_id):
        course = Course.query.get(course_id)

        if course:
            db.session.delete(course)
            db.session.commit()
            return True
        else:
            return False
    
    def update_course(self, course_id, new_data):
        course = Course.query.get(course_id)

        if course:
            for key, value in new_data.items():
                setattr(course, key, value)

            db.session.commit()
            return True
        else:
            return False
    # === endregion : Course ===

    
    # === region : Room ===
    def get_all_rooms(self):
        rooms = Room.query.all()
        room_list = []

        for room in rooms:
            room_data = room.get_json()
            room_list.append(room_data)

        return room_list
    
    def get_room_by_id(self, room_id):
        room = Room.query.get(room_id)

        if room:
            room_data = room.get_json()
            return room_data
        else:
            return None
    
    def find_room(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        rooms = Room.query.filter_by(**conditions)

        room_list = []

        for room in rooms:
            room_list.append(room.get_json())

        return room_list
    
    def delete_room(self, room_id):
        room = Room.query.get(room_id)

        if room:
            db.session.delete(room)
            db.session.commit()
            return True
        else:
            return False
    
    def update_room(self, room_id, new_data):
        room = Room.query.get(room_id)

        if room:
            for key, value in new_data.items():
                setattr(room, key, value)

            db.session.commit()
            return True
        else:
            return False
    # === endregion : Room ===


    # === region : Reminder ===
    def get_all_reminders(self):
        reminders = Reminder.query.all()
        reminder_list = []

        for reminder in reminders:
            reminder_data = reminder.get_json()
            reminder_list.append(reminder_data)

        return reminder_list
    
    def get_reminder_by_id(self, reminder_id):
        reminder = Reminder.query.get(reminder_id)

        if reminder:
            reminder_data = reminder.get_json()
            return reminder_data
        else:
            return None
    
    def find_reminder(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        reminders = Reminder.query.filter_by(**conditions)

        reminder_list = []

        for reminder in reminders:
            reminder_list.append(reminder.get_json())

        return reminder_list
    
    def delete_reminder(self, reminder_id):
        reminder = Reminder.query.get(reminder_id)

        if reminder:
            db.session.delete(reminder)
            db.session.commit()
            return True
        else:
            return False
    
    def update_reminder(self, reminder_id, new_data):
        reminder = Reminder.query.get(reminder_id)

        if reminder:
            for key, value in new_data.items():
                setattr(reminder, key, value)

            db.session.commit()
            return True
        else:
            return False
    # === endregion : Reminder ===


    # === region : Specialization ===
    def get_all_specializations(self):
        specializations = Specialization.query.all()
        specialization_list = []

        for specialization in specializations:
            specialization_data = specialization.get_json()
            specialization_list.append(specialization_data)

        return specialization_list
    
    def get_specialization_by_id(self, specialization_id):
        specialization = Specialization.query.get(specialization_id)

        if specialization:
            specialization_data = specialization.get_json()
            return specialization_data
        else:
            return None
    
    def find_specialization(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        specializations = Specialization.query.filter_by(**conditions)

        specialization_list = []

        for specialization in specializations:
            specialization_list.append(specialization.get_json())

        return specialization_list
    
    def delete_specialization(self, specialization_id):
        specialization = Specialization.query.get(specialization_id)

        if specialization:
            db.session.delete(specialization)
            db.session.commit()
            return True
        else:
            return False
    
    def update_specialization(self, specialization_id, new_data):
        specialization = Specialization.query.get(specialization_id)

        if specialization:
            for key, value in new_data.items():
                setattr(specialization, key, value)

            db.session.commit()
            return True
        else:
            return False
    # === endregion : Specialization ===


    # === region : Teaching ===
    def get_all_teachings(self):
        teachings = Teaching.query.all()
        teaching_list = []

        for teaching in teachings:
            teaching_data = teaching.get_json()
            teaching_list.append(teaching_data)

        return teaching_list
    
    def get_teaching_by_id(self, teaching_id):
        teaching = Teaching.query.get(teaching_id)

        if teaching:
            teaching_data = teaching.get_json()
            return teaching_data
        else:
            return None
    
    def find_teaching(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        teachings = Teaching.query.filter_by(**conditions)

        teaching_list = []

        for teaching in teachings:
            teaching_list.append(teaching.get_json())

        return teaching_list
    
    def delete_teaching(self, teaching_id):
        teaching = Teaching.query.get(teaching_id)

        if teaching:
            db.session.delete(teaching)
            db.session.commit()
            return True
        else:
            return False
    
    def update_teaching(self, teaching_id, new_data):
        teaching = Teaching.query.get(teaching_id)

        if teaching:
            for key, value in new_data.items():
                setattr(teaching, key, value)

            db.session.commit()
            return True
        else:
            return False
    # === endregion : Teaching ===

    
    # === region : Absent ===
    def get_all_absents(self):
        absents = Absent.query.all()
        absent_list = []

        for absent in absents:
            absent_data = absent.get_json()
            absent_list.append(absent_data)

        return absent_list
    
    def get_absent_by_id(self, absent_id):
        absent = Absent.query.get(absent_id)

        if absent:
            absent_data = absent.get_json()
            return absent_data
        else:
            return None
    
    def find_absent(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        absents = Absent.query.filter_by(**conditions)

        absent_list = []

        for absent in absents:
            absent_list.append(absent.get_json())

        return absent_list
    
    def delete_absent(self, absent_id):
        absent = Absent.query.get(absent_id)

        if absent:
            db.session.delete(absent)
            db.session.commit()
            return True
        else:
            return False
    
    def update_absent(self, absent_id, new_data):
        absent = Absent.query.get(absent_id)

        if absent:
            for key, value in new_data.items():
                setattr(absent, key, value)

            db.session.commit()
            return True
        else:
            return False
    # === endregion : Absent ===


    # === region : Participate ===
    def get_all_participates(self):
        participates = Participate.query.all()
        participate_list = []

        for participate in participates:
            participate_data = participate.get_json()
            participate_list.append(participate_data)

        return participate_list
    
    def get_participate_by_id(self, participate_id):
        participate = Participate.query.get(participate_id)

        if participate:
            participate_data = participate.get_json()
            return participate_data
        else:
            return None
    
    def find_participate(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        participates = Participate.query.filter_by(**conditions)

        participate_list = []

        for participate in participates:
            participate_list.append(participate.get_json())

        return participate_list
    
    def delete_participate(self, participate_id):
        participate = Participate.query.get(participate_id)

        if participate:
            db.session.delete(participate)
            db.session.commit()
            return True
        else:
            return False
    
    def update_participate(self, participate_id, new_data):
        participate = Participate.query.get(participate_id)

        if participate:
            for key, value in new_data.items():
                setattr(participate, key, value)

            db.session.commit()
            return True
        else:
            return False
    # === endregion : Participate ===


    # === region : Responsible ===
    def get_all_responsibles(self):
        responsibles = Responsible.query.all()
        responsible_list = []

        for responsible in responsibles:
            responsible_data = responsible.get_json()
            responsible_list.append(responsible_data)

        return responsible_list
    
    def get_responsible_by_id(self, responsible_id):
        responsible = Responsible.query.get(responsible_id)

        if responsible:
            responsible_data = responsible.get_json()
            return responsible_data
        else:
            return None
    
    def find_responsible(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        responsibles = Responsible.query.filter_by(**conditions)

        responsible_list = []

        for responsible in responsibles:
            responsible_list.append(responsible.get_json())

        return responsible_list
    
    def delete_responsible(self, responsible_id):
        responsible = Responsible.query.get(responsible_id)

        if responsible:
            db.session.delete(responsible)
            db.session.commit()
            return True
        else:
            return False
    
    def update_responsible(self, responsible_id, new_data):
        responsible = Responsible.query.get(responsible_id)

        if responsible:
            for key, value in new_data.items():
                setattr(responsible, key, value)

            db.session.commit()
            return True
        else:
            return False
    # === endregion : Responsible ===