from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed


class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Remember Login')
    botao_submite_login = SubmitField('Login')


class FormCriarConta(FlaskForm):
    username = StringField('User name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(6, 20)])
    confirmacao = PasswordField('Confirm Password', validators=[
                                DataRequired(), EqualTo('password')])
    botao_submite = SubmitField('Create Account')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('Email already used')


class FormEditProfile(FlaskForm):
    username = StringField('User name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    user_photo = FileField("Update profile photo", validators=[
                           FileAllowed(['jpg', 'png'])])

    curso_excel = BooleanField('Excel')
    curso_vba = BooleanField('VBA')
    curso_powerbi = BooleanField('Power BI')
    curso_python = BooleanField('Python')
    curso_presentation = BooleanField('Presentation')
    curso_sql = BooleanField('SQL')
    botton_edit_profile = SubmitField('Confirm Edit')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError("Email already registered")


class FormCriarPost(FlaskForm):
    titulo = StringField('Title ', validators=[DataRequired(), Length(2, 140)])
    corpo = TextAreaField('Write here', validators=[DataRequired()])
    btn_submit = SubmitField('Publish Post')

# from project_name import app, database
# from comunidadeimpressionadora.models import Usuario
# app.app_context().push()
# database.create_all()
# usuario = Usuario.query.filter_by(email="igorbroch11@gmail.com").first()
# I had to use this command to make it work
