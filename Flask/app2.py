#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------

# from flask import Flask
# from flask import request
# from flask import render_template
# from flask import redirect, url_for
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField

# app = Flask(__name__)
# # creating a CSRF toke by the below config..
# # we should use this in env. for best practice

# app.config['SECRET_KEY']= "mysecretkey"
# class TestForm(FlaskForm):
#     cat_breed = StringField("What is cat's breed?")
#     submit = SubmitField("Submit")
# @app.route("/",methods = ['GET','POST'])
# def index():
#     cat_breed = False
#     form = TestForm()
#     if form.validate_on_submit():
#         cat_breed = form.cat_breed.data
#         form.cat_breed.data=" "

#     return render_template("index.html",cat_breed=cat_breed, form=form)

# if __name__ =='__main__':
#     app.run(debug =True)
#-----------------------------------------------------------------------
# from flask import Flask, render_template, redirect, url_for, session
# from flask_wtf import FlaskForm
# from wtforms import StringField,BooleanField, DateTimeField,RadioField,SelectField,TextAreaField,SubmitField
# from wtforms.validators import DataRequired
# app = Flask(__name__)
# app.config['SECRET_KEY']="mysecret_key"

# class InfoForm(FlaskForm):
#     breed = StringField("what breed are you?",validators=[DataRequired()])
#     tomcat = BooleanField("Have you been tomcat?")
#     mood = RadioField("Please Choose your mood: ", choices = [('mood_one','Happy'),('modd_two','Excited')])
#     food_choice = SelectField('Choose your fav food:', choices = [('chi','chicken'),('bef','beef'),('fis','Fish')])
#     feedback = TextAreaField()
#     submit = SubmitField('Submit')

# @app.route('/',methods=['GET','POST'])
# def index():
#     form = InfoForm()
#     if form.validate_on_submit():
#         session['breed']= form.breed.data
#         session['tomcat']= form.tomcat.data
#         session['mood']= form.mood.data
#         session['food_choide']= form.food_choice.data
#         session['feedback']=form.feedback.data
#         return redirect(url_for('thankyou'))
#     return render_template('home1.html',form=form)

# @app.route('/thankyou')
# def thankyou():
#     return render_template('thanks.html')

# if __name__=='__main__':
#     app.run(debug=True)
#-----------------------------------------------------------------------
# from flask import Flask, render_template, redirect, url_for, session,flash
# from flask_wtf import FlaskForm
# from wtforms import StringField,BooleanField, DateTimeField,RadioField,SelectField,TextAreaField,SubmitField
# from wtforms.validators import DataRequired

# app = Flask(__name__)
# app.config['SECRET_KEY']="mysecret_key"
# @app.route('/',methods=['GET','POST'])

# class SimpleForm(FlaskForm):
#     submit = SubmitField("Click me!!")

# def index():
#     form = SimpleForm()
#     if form.validate_on_submit():
#         flash("You just clicked the button")
#         return redirect(url_for("index"))

#     return render_template("home2.html",form=form)

# if __name__=="__main__":
#     app.run(debug=True)
        
#-----------------------------------------------
# from flask import Flask, render_template, redirect, url_for, session,flash
# from flask_wtf import FlaskForm
# from wtforms import StringField,BooleanField, DateTimeField,RadioField,SelectField,TextAreaField,SubmitField
# from wtforms.validators import DataRequired
# app = Flask(__name__)
# app.config['SECRET_KEY'] = "mysecret_key"

# class SImpleForm(FlaskForm):
#     submit = SubmitField("Click me!!")

# @app.route('/',methods=['GET','POST'])
# def index():
#     form = SImpleForm()
#     if form.validate_on_submit():
#         flash("You just clicked the button!!!!!")
#         return redirect(url_for("index"))
#     return render_template("home2.html",form=form)


# if __name__=='__main__':
#     app.run(debug=True)

#-----------------------------------------------------------------------
# from flask import Flask, render_template, redirect, url_for, session,flash
# from flask_wtf import FlaskForm
# from wtforms import StringField,BooleanField, DateTimeField,RadioField,SelectField,TextAreaField,SubmitField
# from wtforms.validators import DataRequired
# app = Flask(__name__)
# app.config['SECRET_KEY'] = "mysecret_key"

# class InfoForm(FlaskForm):
#     breed = StringField('What breed are you?')
#     submit = SubmitField('submit')

# @app.route('/',methods=['GET','POST'])
# def index():
#     form = InfoForm()
#     if form.validate_on_submit():
#         session['breed'] = form.breed.data
#         flash(f'You just chagned your breed to:{session["breed"]}')

#         return redirect(url_for('index'))
#     return render_template('home3.html',form=form)

# if __name__=='__main__':
#     app.run(debug=True)

#-----------------------------------------------------------------------
#--------------------------# installed psycopg2 ------------------------------------------


# # connect postgres with flask
# import psycopg2
# from psycopg2 import Error

# try:
#     # Connect to an existing database
#     connection = psycopg2.connect(user="postgres",
#                                   password="Finserv@2023",
#                                   host="127.0.0.1",
#                                   port="5432",
#                                   database="postgres")

#     # Create a cursor to perform database operations
#     cursor = connection.cursor()

#     # Print PostgreSQL details
#     print("PostgreSQL server information")
#     print(connection.get_dsn_parameters(), "\n")
#     # Executing a SQL query
#     cursor.execute("SELECT * from Color2;")
    
#     # Fetch result
#     record = cursor.fetchone()
#     print("You are connected to - ", record, "\n")

# except (Exception, Error) as error:
#     print("Error while connecting to PostgreSQL", error)
# finally:
#     if (connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")
#-----------------------------------------------------------------------

import psycopg2
from psycopg2 import Error
try:
    # Connect to an existing database
    conn = psycopg2.connect(user="postgres",
                                  password="Finserv@2023",
                                  database="postgres")
    cursor = conn.cursor()
    # cursor.execute('CREATE TABLE test(id serial primary key, num integer, data varchar)')

    # cursor.execute('Insert into test(num,data)values(%s ,%s)',(101,"maths"))
    # cursor.execute('Insert into test(num,data)values(%s ,%s)',(102,"english"))
   
    cursor.execute("Select * from test")
    cursor.execute("update test set data = 'chemistry' where id =1 ")
    cursor.execute("Select * from test")
    print(cursor.fetchall())
    print(cursor.fetchone())
    print(cursor.fetchmany())
    #cursor.execute("delete from test where id = 2")
    conn.commit()


    
except(Exception,Error)as e:
    print('Error: ',e)

    