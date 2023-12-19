from services.sql_alchemy_service import db

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'university'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    # Relation avec la table Student (un utilisateur peut être lié à plusieurs étudiants)
    students = db.relationship('Student', backref='user', lazy=True, primaryjoin='User.id == foreign(Student.user_id)')

    # Relation avec la table Personal (un utilisateur peut être lié à plusieurs personnels)
    personals = db.relationship('Personal', backref='user', lazy=True, primaryjoin='User.id == foreign(Personal.user_id)')

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
    mail = db.Column(db.String(64), nullable=False, unique=True)
    phone_number = db.Column(db.String(14), nullable=False, unique=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    department_id = db.Column(db.Integer, nullable=False)
    group_id = db.Column(db.Integer, nullable=False)
    subgroup_id = db.Column(db.Integer, nullable=False)

    absents = db.relationship('Absent', backref='student', lazy=True, primaryjoin='Student.id == foreign(Absent.student_number)')

    def get_json(self):
        """ Formats data in JSON """
        return {
                'id' : self.id,
                'last_name' : self.last_name,
                'first_name' : self.first_name,
                'mail' : self.mail,
                'phone_number' : self.phone_number,
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
    
    # Relationships    
    students = db.relationship('Student', backref='department', lazy=True, primaryjoin='Department.id == foreign(Student.department_id)')
    
    groups = db.relationship('Group', backref='department', lazy=True, primaryjoin='Department.id == foreign(Group.department_id)')
    
    specializations = db.relationship('Specialization', backref='department', lazy=True, primaryjoin='Department.id == foreign(Specialization.department_id)')

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
    
    # Relationships
    students = db.relationship('Student', backref='group', lazy=True, primaryjoin='Group.id == foreign(Student.group_id)')
    
    subgroups = db.relationship('Subgroup', backref='group', lazy=True, primaryjoin='Group.id == foreign(Subgroup.group_id)')

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
    
    # Relationships
    students = db.relationship('Student', backref='subgroup', lazy=True, primaryjoin='Subgroup.id == foreign(Student.subgroup_id)')
    
    participates = db.relationship('Participate', backref='subgroup', lazy=True, primaryjoin='Subgroup.id == foreign(Participate.subgroup_id)')
    
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
    mail = db.Column(db.String(64), nullable=False)
    personal_code = db.Column(db.String(16), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('university.users.id'), unique=True, nullable=False)
    phone_number = db.Column(db.String(14), nullable=False, unique=True)


    # Relationships
    departments = db.relationship('Department', backref='personal', lazy=True, primaryjoin='Personal.id == foreign(Department.personal_id)')
    roles = db.relationship('Role', backref='personal', lazy=True, primaryjoin='Personal.id == foreign(Role.personal_id)')
    courses = db.relationship('Course', backref='personal', lazy=True, primaryjoin='Personal.id == foreign(Course.personal_id)')
    responsibles = db.relationship('Responsible', backref='personal', lazy=True, primaryjoin='Personal.id == foreign(Responsible.personal_id)')
    
    def get_json(self):
        """ Formats data in JSON """
        return {
                'id' : self.id,
                'last_name' : self.last_name,
                'first_name' : self.first_name,
                'mail' : self.mail,
                'personal_code' : self.personal_code,
                'user_id' : self.user_id,
                'phone_number' : self.phone_number
            }

class Role(db.Model):
    __tablename__ = 'roles'
    __table_args__ = {'schema': 'university'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(128))
    personal_id = db.Column(db.Integer, db.ForeignKey('university.personals.id'), nullable=False)

    def get_json(self):
        """ Formats data in JSON """
        return {
                'id' : self.id,
                'name' : self.name,
                'description' : self.description,
                'personal_id' : self.personal_id
            }

class Course(db.Model):
    __tablename__ = 'courses'
    __table_args__ = {'schema': 'university'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.Text)
    start_time = db.Column(db.TIMESTAMP, nullable=False)
    end_time = db.Column(db.TIMESTAMP, nullable=False)
    course_type = db.Column(db.String(32), nullable=False)
    personal_id = db.Column(db.Integer, db.ForeignKey('university.personals.id'), nullable=False)
    rooms_id = db.Column(db.Integer, db.ForeignKey('university.rooms.id'), nullable=False)
    teaching_id = db.Column(db.Integer, db.ForeignKey('university.teachings.id'), nullable=False)

    # Relationships
    Reminder = db.relationship('Reminder', backref='course', lazy=True, primaryjoin='Course.id == foreign(Reminder.course_id)')
    Absent = db.relationship('Absent', backref='course', lazy=True, primaryjoin='Course.id == foreign(Absent.course_id)')
    Participate = db.relationship('Participate', backref='course', lazy=True, primaryjoin='Course.id == foreign(Participate.course_id)')

    def get_json(self):
        """ Formats data in JSON """
        return {
                'id' : self.id,
                'description' : self.description,
                'start_time' : self.start_time,
                'end_time' : self.end_time,
                'course_type' : self.course_type,
                'personal_id' : self.personal_id,
                'rooms_id' : self.rooms_id,
                'teaching_id' : self.teaching_id
            }

class Room(db.Model):
    __tablename__ = 'rooms'
    __table_args__ = {'schema': 'university'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(32), nullable=False, unique=True)
    capacity = db.Column(db.Integer, nullable=False)
    has_computer = db.Column(db.Boolean, default=True)
    has_projector = db.Column(db.Boolean, default=True)

    # Relationships
    courses = db.relationship('Course', backref='room', lazy=True, primaryjoin='Room.id == foreign(Course.rooms_id)')
    
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
    course_id = db.Column(db.Integer, db.ForeignKey('university.courses.id'), nullable=False)

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
    department_id = db.Column(db.Integer, db.ForeignKey('university.departments.id'), nullable=False)

    # Relationships
    teaching = db.relationship('Teaching', backref='specialization', lazy=True, primaryjoin='Specialization.id == foreign(Teaching.specialization_id)')
    
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
    specialization_id = db.Column(db.Integer, db.ForeignKey('university.specializations.id'), nullable=False)

    # Relationships
    courses = db.relationship('Course', backref='teaching', lazy=True, primaryjoin='Teaching.id == foreign(Course.teaching_id)')
    responsible = db.relationship('Responsible', backref='teaching', lazy=True, primaryjoin='Teaching.id == foreign(Responsible.teaching_id)')

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
    student_number = db.Column(db.Integer, db.ForeignKey('university.students.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('university.courses.id'), nullable=False)

    def get_json(self):
        """ Formats data in JSON """
        return {
                'id' : self.id,
                'justified' : self.justified,
                'student_number' : self.student_number,
                'course_id' : self.course_id
            }

class Participate(db.Model):
    __tablename__ = 'participates'
    __table_args__ = {'schema': 'university'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_id = db.Column(db.Integer, db.ForeignKey('university.courses.id'), nullable=False)
    subgroup_id = db.Column(db.Integer, db.ForeignKey('university.subgroups.id'), nullable=False)

    def get_json(self):
        """ Formats data in JSON """
        return {
                'id' : self.id,
                'course_id' : self.course_id,
                'subgroup_id' : self.subgroup_id
            }
        
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
