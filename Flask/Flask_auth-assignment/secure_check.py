from user_model import *

db.create_all()

u1 = User('rohan','mypass1')
u2 = User('rahul','mypass2')

db.session.add_all([u1,u2])
db.session.commit()

# users = [(u1.id,u1.username,u1.password),(u2.id,u2.username,u2.password)]
users = [u1,u2]

username_table = {u.username:u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username,password):
    user = username_table.get(username,None)
    if user and password == user.password:
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id,None)
