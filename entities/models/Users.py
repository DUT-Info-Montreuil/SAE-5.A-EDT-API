from sqlAlchemyModel import db, table_users
# Dynamically create the model User based on the reflected table (table in the db)
class User(db.Model):
    __table__ = table_users