from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import DataRequired

class LoginForm(Form):
	openid = StringField('openid', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)

class ReviewForm(Form):
        ratingChoices = [('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)]
        cleanliness = SelectField(label='Cleanliness', choices=ratingChoices)
        crowdedness = SelectField(label='Crowdedness', choices=ratingChoices)
        numberOfStalls = SelectField(label='Number of Stalls', choices=ratingChoices)
        
