from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


# 注册表单
class LoginForm(FlaskForm):
    # 用户名
    username = StringField('Username', validators=[DataRequired()], render_kw={'value': 'lizenan'})
    # 手机号
    telephone = StringField('Tel', validators=[Length(11,11), DataRequired()], render_kw={'value': '17605889887'})
    # 职位
    # role = SelectField('Role', choices=[(1,'员工'), (2,'合作商'), (3, '老板')], default=1)
    # 密码
    password = PasswordField('Password', validators=[Length(6,20), DataRequired()], render_kw={'placeholder': '设置密码'})
    # 验证密码
    verify_pwd = PasswordField('Verify_pwd', validators=[EqualTo('password'), DataRequired()], render_kw={'placeholder': '重复密码'})
    # 提交
    submit = SubmitField('Register')
