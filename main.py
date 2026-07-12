"""
Red underlines? Install the required packages first:
Open the Terminal in PyCharm (bottom left).

On Windows type:
python -m pip install -r requirements.txt

On macOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
"""
from flask_bootstrap import Bootstrap4
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError

# def validate_email():
#     print("Email must contain @ and .")
#     def _validate_email(form, field):
#         if '@' not in field.data or '.' not in field.data:
#             raise ValidationError('Please enter a valid email address')
#     return _validate_email

class MyForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8,
                                                                                  message="Password must be at least 8 characters long")])
    submit = SubmitField(label='login')


app = Flask(__name__)

bootstrap = Bootstrap4(app)

app.secret_key = "kunalmore"


@app.route("/")
def home():
    return render_template('index.html', bootstrap=bootstrap)


@app.route("/login" , methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form, bootstrap=bootstrap)


if __name__ == '__main__':
    app.run(debug=True)
