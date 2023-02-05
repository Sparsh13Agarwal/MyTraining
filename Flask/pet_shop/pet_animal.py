from flask import Flask, render_template, redirect, url_for, session,flash
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField, DateTimeField,RadioField,SelectField,TextAreaField,SubmitField
from wtforms.validators import DataRequired
from pet_db import DBConnection
from pet_config import *
from pet_log import *

app = Flask(__name__)   
# logging.basicConfig(filename="pet_app.log", level=logging.DEBUG,format=f'%(asctime)s %(levelname)s %(name)s %(message)s',filemode='w')
app.config['SECRET_KEY'] = "mysecret_key"




tablename = 'pet_info'
class pet_Info(FlaskForm):
    pet_name = StringField("Pet Name:",validators=[DataRequired()])
    pet_type = SelectField("What pet",choices=[('dog','dog'),('cat','cat')])
    breed = StringField("What breed:",validators=[DataRequired()])
    pet_color = StringField("Pet color:")
    owner_name = StringField("Owner Name:",validators=[DataRequired()])
    submit = SubmitField("Submit")

class pet_info_Delete(FlaskForm):
    pet_id = StringField("Pet id: ",validators=[DataRequired()])
    submit = SubmitField("Submit")

class pet_info_Update(FlaskForm):
    pet_id = StringField("Pet id: ",validators=[DataRequired()])
    pet_name = StringField("Pet Name:",validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/')
def home():
    try:
        # app.logger.log_level("hi homeee")
        logger.info("Hi homeee")
        return render_template('pet_home.html')
    except psycopg2.Error as er:
        logger.error(exc_info=True)

@app.route('/register',methods =['GET','POST'])
def register():
    try:
        try:
            form = pet_Info()
            if form.validate_on_submit():
                session['pet_name']=form.pet_name.data
                session['pet_type'] = form.pet_type.data
                session['breed']= form.breed.data
                session['pet_color']=form.pet_color.data
                session['owner_name']=form.owner_name.data
                db = DBConnection()
                db.connect_db()
                db.insert_record(tablename,form.pet_name.data,form.pet_type.data,form.breed.data,form.pet_color.data,form.owner_name.data)
                # app.logger.info("register page rendered successfully")
                do_something()
                return redirect(url_for('thankyou'))
        except psycopg2.Error as e:
            logger.error('Error:',e)
            logger.info('e1')
        return render_template('pet_reg.html',form = form)
    except psycopg2.Error as e:
        print('errr',e)
        logger.info('e2')
        logger.error("error is",e)
        

@app.route('/log',methods=['GET','POST'])
def log():
    try:
        return render_template('pet_log.html',data = log_info())
    except psycopg2.Error as err:
        logger.error(err)

@app.route('/thankyou')
def thankyou():
    return render_template('pet_thanks.html')


@app.route('/display',methods = ['GET','POST'])
def display():
    db = DBConnection()
    db.connect_db()
    pets = db.fetchall_record(tablename)
    return render_template('pet_display.html',pets = pets)

@app.route('/delete',methods = ['GET','POST'])
def delete():

    form = pet_info_Delete()
    if form.validate_on_submit():
        session['pet_id']=form.pet_id.data
        db = DBConnection()
        db.connect_db()
        db.delete_record(tablename,form.pet_id.data)
        return redirect(url_for('delete_successfully'))

    return render_template('pet_delete.html',form = form)


@app.route('/update',methods = ['GET','POST'])
def update():
    form = pet_info_Update()
    if form.validate_on_submit():
        session['pet_id']=form.pet_id.data
        session['pet_name']= form.pet_name.data
        db= DBConnection()
        db.connect_db()
        res = db.update_record(tablename,form.pet_id.data,form.pet_name.data)
        if res:
            return redirect(url_for('update_successfully'))
        else:
            return redirect(url_for('err'))
    return render_template('pet_update.html',form = form)

@app.route('/error')
def err():
    return render_template('pet_error.html')

@app.route('/delete_successfully')
def delete_successfully():
    return render_template('pet_delete_successfully.html')

@app.route('/update_successfully')
def update_successfully():
    return render_template('pet_update_successfully.html')


if __name__=='__main__':
    app.run(debug=True)
    