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

    # Relation inverse avec la table User (un étudiant appartient à un utilisateur)
    user = db.relationship('User', back_populates='students', foreign_keys=[user_id])

    # Relation avec la table Department (un étudiant appartient à un département)
    department = db.relationship('Department', backref='students', lazy=True)

    # Relation avec la table Group (un étudiant appartient à un groupe)
    group = db.relationship('Group', backref='students', lazy=True)

    # Relation avec la table Subgroup (un étudiant appartient à un sous-groupe)
    subgroup = db.relationship('Subgroup', backref='students', lazy=True)

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
    
    # Relation avec la table Personal (un département est associé à un personnel)
    personal = db.relationship('Personal', backref='department', lazy=True)

    # Relation avec la table Specialization (un département a plusieurs spécialisations)
    specializations = db.relationship('Specialization', backref='department', lazy=True)
    
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
    
    # Relation avec la table Department (un groupe appartient à un département)
    department = db.relationship('Department', backref='groups', lazy=True)

    # Relation avec la table Student (un groupe a plusieurs étudiants)
    students = db.relationship('Student', backref='group', lazy=True)
    
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
    
    # Relation avec la table Group (un sous-groupe appartient à un groupe)
    group = db.relationship('Group', backref='subgroups', lazy=True)
    
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

    # Relation avec la table User (un personnel est associé à un utilisateur)
    user = db.relationship('User', backref='personals', lazy=True)

    # Relation avec la table Department (un personnel appartient à un département)
    department_id = db.Column(db.Integer, db.ForeignKey('university.departments.id'), nullable=False)
    department = db.relationship('Department', backref='personals', lazy=True)

    # Relation avec la table Role (un personnel a un rôle)
    role_id = db.Column(db.Integer, db.ForeignKey('university.roles.id'), nullable=False)
    role = db.relationship('Role', backref='personals', lazy=True)

    # Relation avec la table Teaching (un personnel donne des enseignements)
    teachings = db.relationship('Teaching', backref='personal', lazy=True)

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

    # Relation avec la table Personal (un rôle est associé à un personnel)
    personal = db.relationship('Personal', backref='role', lazy=True)

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

    # Relation avec la table Personal (un cours est associé à un personnel)
    personal = db.relationship('Personal', backref='courses', lazy=True)

    # Relation avec la table Room (un cours a lieu dans une salle)
    room = db.relationship('Room', backref='courses', lazy=True)

    # Relation avec la table Teaching (un cours est associé à un enseignement)
    teaching = db.relationship('Teaching', backref='courses', lazy=True)

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

    # Relation avec la table Course (une salle peut être associée à plusieurs cours)
    courses = db.relationship('Course', backref='room', lazy=True)

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

    # Relation avec la table Course (un rappel est associé à un cours)
    course = db.relationship('Course', backref='reminders', lazy=True)

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

    # Relation avec la table Department (une spécialisation est associée à un département)
    department = db.relationship('Department', backref='specializations', lazy=True)

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

    # Relation avec la table Specialization (un enseignement est associé à une spécialisation)
    specialization = db.relationship('Specialization', backref='teachings', lazy=True)

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

    # Relation avec la table Student (une absence est associée à un étudiant)
    student = db.relationship('Student', backref='absents', lazy=True)

    # Relation avec la table Course (une absence est associée à un cours)
    course = db.relationship('Course', backref='absents', lazy=True)

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

    # Relation avec la table Course (une participation est associée à un cours)
    course = db.relationship('Course', backref='participates', lazy=True)

    # Relation avec la table Subgroup (une participation est associée à un sous-groupe)
    subgroup = db.relationship('Subgroup', backref='participates', lazy=True)

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
    
    # Relation avec la table Personal (un responsable est associé à un personnel)
    personal = db.relationship('Personal', backref='responsibles', lazy=True)

    # Relation avec la table Teaching (un responsable est associé à un enseignement)
    teaching = db.relationship('Teaching', backref='responsibles', lazy=True)

    
    def get_json(self):
        """ Formats data in JSON """
        return {
                'id' : self.id,
                'personal_id' : self.personal_id,
                'teaching_id' : self.teaching_id
            }
