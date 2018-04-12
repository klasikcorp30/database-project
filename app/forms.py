from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, RadioField,SelectField,DateField

from wtforms import validators, ValidationError

class RegistrationForm(FlaskForm):
   first_name = StringField("First Name",[validators.Required("Please enter your name")])

   last_name = StringField("Last Name",[validators.Required("Please enter your name")])

   email = StringField("Email",[validators.Required()])

   dob = DateField("Date of Birth",[validators.Required()],format= '%Y-%m-%d')

   username = StringField("Username",[validators.Required('A username is required')])

   password = StringField("Password",[validators.Required("Minimum eight characters, at least one letter, one number and one special character"),
            validators.regexp("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")])
   
   retype_password = StringField("Retype Password",[validators.EqualTo(password,"Passwords do not match")])

   submit = SubmitField("Submit")

class MealPlan(FlaskForm):
    calories = IntegerField("Calories", [validators.Required()])
    week = DateField("Week", [validators.Required()])
    create = SubmitField("Create")
    max_calories = IntegerField("Max Calories",[validators.Required()])
    meal_type = SelectField("Meal Type",[validators.Required()],
        choices=[('Breakfast','Breakfast'),('Lunch','Lunch'),('Dinner','Dinner')])
    
