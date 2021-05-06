from wtforms import SubmitField,TextAreaField, SelectField,StringField, ValidationError
from ..models import User, Blogs
from flask_wtf import FlaskForm
from wtforms.validators import Required, DataRequired, Length


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    blog_category = TextAreaField('Category', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    blog_description = StringField("Give a short decription of your blog",validators = [Required(),Length(min=20,max=400,message='Must be between 200-400 characters')])
    submit = SubmitField('Post')