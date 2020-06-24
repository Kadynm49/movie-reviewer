from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    review_type = RadioField('Review Type', choices=[('a', 'Positive'), ('n', 'Negative'), ('a', 'Average')], validators=[DataRequired()])
    submit = SubmitField()