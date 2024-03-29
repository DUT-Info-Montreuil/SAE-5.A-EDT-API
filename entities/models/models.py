from services.sql_alchemy_service import db

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'university'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    
    def get_json(self):
        """ Formats data in JSON """
        return {
                'id': self.id,
                'username': self.username,
                'password': self.password
            }

class Student(db.Model):
    __tablename__ = 'students'
    __table_args__ = {'schema': 'university'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    last_name = db.Column(db.String(32), nullable=False)
    first_name = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    department_id = db.Column(db.Integer, nullable=False)
    group_id = db.Column(db.Integer, nullable=False)
    subgroup_id = db.Column(db.Integer, nullable=False)
    
    def get_json(self):
        """ Formats data in JSON """
        return {
                'id' : self.id,
                'last_name' : self.last_name,
                'first_name' : self.first_name,
                'user_id' : self.user_id,
                'department_id' : self.department_id,
                'group_id' : self.group_id,
                'subgroup_id' : self.subgroup_id
            }

class Department(db.Model):
    __tablename__ = 'departments'
    __table_args__ = {'schema': 'university'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False, unique=True)
    description = db.Column(db.String(128))
    degree_type = db.Column(db.String(50), nullable=False)
    personal_id = db.Column(db.Integer, nullable=False)
    
    def get_json(self):
        """ Formats data in JSON """
        return {
                'id' : self.id,
                'name' : self.name,
                'description' : self.description,
                'degree_type' : self.degree_type,
                'personal_id' : self.personal_id
            }

class Group(db.Model):
    __tablename__ = 'groups'
    __table_args__ = {'schema': 'university'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    promotion = db.Column(db.Integer)
    type = db.Column(db.String(5), nullable=False)
    department_id = db.Column(db.Integer, nullable=False)
    
    def get_json(self):
        """ Formats data in JSON """
        return {
                'id' : self.id,
                'promotion' : self.promotion,
                'type' : self.type,
                'department_id' : self.department_id
            }

class Subgroup(db.Model):
    __tablename__ = 'subgroups'
    __table_args__ = {'schema': 'university'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), nullable=False)
    group_id = db.Column(db.Integer, nullable=False)
    
    def get_json(self):
        """ Formats data in JSON """
        return {
                'id' : self.id,
                'name' : self.name,
                'group_id' : self.group_id
            }

class Personal(db.Model):
    __tablename__ = 'personals'
    __table_args__ = {'schema': 'university'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    last_name = db.Column(db.String(32), nullable=False)
    first_name = db.Column(db.String(32), nullable=False)
    personal_code = db.Column(db.String(16), unique=True, nullable=False)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    
    def get_json(self):
        """ Formats data in JSON """
        return {
                'id' : self.id,
                'last_name' : self.last_name,
                'first_name' : self.first_name,
                'personal_code' : self.personal_code,
                'user_id' : self.user_id
            }

class Course(db.Model):
    __tablename__ = 'courses'
    __table_args__ = {'schema': 'university'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.Text)
    starttime = db.Column(db.TIMESTAMP, nullable=False)
    endtime = db.Column(db.TIMESTAMP, nullable=False)
    course_type = db.Column(db.String(32), nullable=False)
    # teaching_id = db.Column(db.Integer, nullable=False)
    teaching_id = db.Column(db.Integer, db.ForeignKey('university.teachings.id'), nullable=False)
    rooms_courses = db.relationship('RoomsCourses', backref='course', lazy=True, primaryjoin="Course.id == RoomsCourses.course_id")
    personals_courses = db.relationship('PersonalsCourses', backref='course', lazy=True, primaryjoin="Course.id == PersonalsCourses.course_id")
    participates = db.relationship('Participates', backref='course', lazy=True, primaryjoin="Course.id == Participates.course_id")

    
    def get_json(self):
        """ Formats data in JSON """
        return {
                'id' : self.id,
                'description' : self.description,
                'start_time' : self.start_time,
                'end_time' : self.end_time,
                'course_type' : self.course_type,
                'teaching_id' : self.teaching_id
            }
    

class RoomsCourses(db.Model):
    __tablename__ = 'rooms_courses'
    __table_args__ = {'schema': 'university'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_id = db.Column(db.Integer, db.ForeignKey('university.courses.id'), nullable=False)
    rooms_id = db.Column(db.Integer, db.ForeignKey('university.rooms.id'), nullable=False)

class PersonalsCourses(db.Model):
    __tablename__ = 'personals_courses'
    __table_args__ = {'schema': 'university'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_id = db.Column(db.Integer, db.ForeignKey('university.courses.id'), nullable=False)
    personal_id = db.Column(db.Integer, db.ForeignKey('university.personals.id'), nullable=False)

class Participates(db.Model):
    __tablename__ = 'participates'
    __table_args__ = {'schema': 'university'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_id = db.Column(db.Integer, db.ForeignKey('university.courses.id'), nullable=False)
    subgroup_id = db.Column(db.Integer, db.ForeignKey('university.subgroups.id'), nullable=False)


class Room(db.Model):
    __tablename__ = 'rooms'
    __table_args__ = {'schema': 'university'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(32), nullable=False, unique=True)
    capacity = db.Column(db.Integer, nullable=False)
    has_computer = db.Column(db.Boolean, default=True)
    has_projector = db.Column(db.Boolean, default=True)
    
    def get_json(self):
        """ Formats data in JSON """
        return {
                'id' : self.id,
                'code' : self.code,
                'capacity' : self.capacity,
                'has_computer' : self.has_computer,
                'has_projector' : self.has_projector
            }

class Reminder(db.Model):
    __tablename__ = 'reminders'
    __table_args__ = {'schema': 'university'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
    description = db.Column(db.Text)
    course_id = db.Column(db.Integer, nullable=False)
    
    def get_json(self):
        """ Formats data in JSON """
        return {
                'id' : self.id,
                'name' : self.name,
                'description' : self.description,
                'course_id' : self.course_id
            }

class Specialization(db.Model):
    __tablename__ = 'specializations'
    __table_args__ = {'schema': 'university'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False, default='Semestre de préparation au parcours')
    department_id = db.Column(db.Integer, nullable=False)
    
    def get_json(self):
        """ Formats data in JSON """
        return {
                'id' : self.id,
                'code' : self.code,
                'name' : self.name,
                'department_id' : self.department_id
            }

class Teaching(db.Model):
    __tablename__ = 'teachings'
    __table_args__ = {'schema': 'university'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255))
    hour_number = db.Column(db.Integer)
    semestre = db.Column(db.Integer, nullable=False)
    sequence = db.Column(db.String(8), nullable=False)
    description = db.Column(db.Text)
    teaching_type = db.Column(db.String(32), default='RCC')
    color = db.Column(db.String(6))
    specialization_id = db.Column(db.Integer, nullable=False)
    
    def get_json(self):
        """ Formats data in JSON """
        return {
                'id' : self.id,
                'title' : self.title,
                'hour_number' : self.hour_number,
                'semestre' : self.semestre,
                'sequence' : self.sequence,
                'description' : self.description,
                'teaching_type' : self.teaching_type,
                'specialization_id' : self.specialization_id
            }


class Absent(db.Model):
    __tablename__ = 'absents'
    __table_args__ = {'schema': 'university'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    justified = db.Column(db.Boolean, default=True)
    student_number = db.Column(db.Integer, nullable=False)
    course_id = db.Column(db.Integer, nullable=False)
    
    def get_json(self):
        """ Formats data in JSON """
        return {
                'id' : self.id,
                'justified' : self.justified,
                'student_number' : self.student_number,
                'course_id' : self.course_id
            }

# class Participate(db.Model):
#     __tablename__ = 'participates'
#     __table_args__ = {'schema': 'university'}

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     course_id = db.Column(db.Integer, nullable=False)
#     subgroup_id = db.Column(db.Integer, nullable=False)

#     def get_json(self):
#         """ Formats data in JSON """
#         return {
#                 'id' : self.id,
#                 'course_id' : self.course_id,
#                 'subgroup_id' : self.subgroup_id
#             }
        
class Responsible(db.Model):
    __tablename__ = 'responsibles'
    __table_args__ = {'schema': 'university'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    personal_id = db.Column(db.Integer, nullable=False)
    teaching_id = db.Column(db.Integer, nullable=False)
    
    def get_json(self):
        """ Formats data in JSON """
        return {
                'id' : self.id,
                'personal_id' : self.personal_id,
                'teaching_id' : self.teaching_id
            }
