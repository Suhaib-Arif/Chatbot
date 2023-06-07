from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired


class MyForms(FlaskForm):
    ques1 = TextAreaField("Describe your health conditions", validators=[DataRequired()],widget=TextArea())
    ques2 = TextAreaField("Describe the severity of condition ", validators=[DataRequired()], widget=TextArea())
    reply_field = TextAreaField("The response", render_kw={"readonly": True, "class": "text-input"})