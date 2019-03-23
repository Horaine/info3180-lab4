from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired 

class UploadForm():
    photo = ('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])
    description = StringField('Description', validators=[DataRequired()])