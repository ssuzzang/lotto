from flask_app import mongodb

class Users(mongodb.Model):
    __tablename__ = 'users'

    id = mongodb.Column(mongodb.Integer, primary_key=True)
    date = mongodb.Column(mongodb.String(), nullable=False)
    num = mongodb.Column(mongodb.String(), nullable=False)


    def __repr__(self):
        return f"<User('{self.id}')>"
