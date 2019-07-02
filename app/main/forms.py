from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from ..models import User, Pitch, Category, Comment


class PitchForm(FlaskForm):
    pitch_content = TextAreaField('Your New pitch content here',validators=[DataRequired()])
    choose_category = SelectField('Category',choices=[('Interview','Interview'),('product','product')], validators=[DataRequired()])
    submit = SubmitField()

class CommentForm(FlaskForm):
    comment = TextAreaField('Insert your comment here', validators=[DataRequired])
    submit = SubmitField()

class CategoryForm(FlaskForm):
    choose_category = SelectField('Category',choices=[('Interview','Interview'),('product','product')], validators=[DataRequired()])
    submit = SubmitField()

