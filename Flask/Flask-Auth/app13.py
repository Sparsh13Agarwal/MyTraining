from flask_bcrypt import Bcrypt

# bcrypt = Bcrypt()

# hashed_pass = bcrypt.generate_password_hash("mypassword")
# print(hashed_pass)

# check1 = bcrypt.check_password_hash(hashed_pass,"mypass")
# print(check1)

# check2 =bcrypt.check_password_hash(hashed_pass,"mypassword")
# print(check2)

#------------------------------------------------------------------------

from werkzeug.security import generate_password_hash,check_password_hash
hashed_pass = generate_password_hash('mypassword')
print(hashed_pass)

check1 = check_password_hash(hashed_pass,'wrng-pass')
print(check1)

check2 = check_password_hash(hashed_pass,"mypassword")
print(check2)

