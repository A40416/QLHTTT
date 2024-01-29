from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SelectField, SubmitField, IntegerField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

class RegistrationForm(FlaskForm):
    username = StringField('Tên đăng nhập', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Một khẩu', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Nhập lại mật khẩu', validators=[DataRequired(), EqualTo('password')])
    first_name = StringField('Họ khách hàng', validators=[DataRequired()])
    last_name = StringField('Tên khách hàng', validators=[DataRequired()])
    birthdate = DateField('Ngày sinh', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    income = IntegerField('Thu nhập', validators=[DataRequired()])
    gender = SelectField('Giới tính', choices=[('M', 'Nam'), ('F', 'Nữ')])
    address = StringField('Địa chỉ', validators=[DataRequired()])
    phone = StringField('Điện thoại', validators=[DataRequired()])
    submit = SubmitField('Đăng ký')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Registration successful!', 'success')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)