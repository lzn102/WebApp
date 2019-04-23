# 表单基类
from flask_wtf import FlaskForm

# 对应Html的表单字段
from wtforms import StringField, PasswordField, SelectField, SubmitField, IntegerField
from wtforms.fields.html5 import TelField

# 表单的验证条件
from wtforms.validators import DataRequired, Length, EqualTo


# 注册表单
class RegisterForm(FlaskForm):
    # 用户名
    """ render_kw 中可以添加html的属性值 """
    username = StringField('姓名', validators=[DataRequired()], render_kw={'placeholder': '姓名'})
    # 手机号
    telephone = TelField('电话', validators=[DataRequired(), Length(11)], render_kw={'placeholder': '手机'})
    # 职位
    """ 此处default的数字需要转为字符串,因为表单提交后数字会转为字符串,不然views视图函数不能通过表单验证"""
    role = SelectField('职位', choices=[('staff', '员工'), ('creator', '合作商'), ('boss', '老板')], default='staff')
    # 密码
    password = PasswordField('密码', validators=[Length(6, 20), DataRequired()], render_kw={'placeholder': '设置密码'})
    # 验证密码
    verify_pwd = PasswordField('确认密码', validators=[EqualTo('password'), DataRequired()], render_kw={'placeholder': '重复密码'})
    # 提交
    submit = SubmitField('注册')


# 登录表单
class LoginForm(FlaskForm):
    telephone = TelField('电话', validators=[DataRequired(), Length(11)], render_kw={'placeholder': '手机'})
    password = PasswordField('密码', validators=[Length(6, 20), DataRequired()], render_kw={'placeholder': '密码'})
    submit = SubmitField('登录')


class AddStore(FlaskForm):
    serial = StringField('编号', validators=[DataRequired()], render_kw={'placeholder': '编号'})
    size = SelectField('规格', choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('Other', '其它'), ('XXS', 'XXS'), ('XS', 'XS'), ('XL', 'XL'), ('XXL', 'XXL')], default='S')
    number = IntegerField('数量', validators=[DataRequired()], render_kw={'placeholder': '编号'})
    unit = SelectField('单位', choices=[('a', '件'), ('b', '条'), ('c', '箱'), ('d', '个'), ('Other', '其它')], default='a')
    category = SelectField('类别', choices=[('overcoat', '大衣'), ('fabric', '面料'), ('cardigan', '羊毛衫'), ('sample_clothing', '样衣'), ('Other', '其它')], default='overcoat')
    partner = SelectField('')


    # 编号
    serial = db.Column(db.String(50))
    # 规格
    size = db.Column(db.String(20))
    # 数量
    number = db.Column(db.Integer)
    # 单位
    unit = db.Column(db.String(5))
    # 类别
    category = db.Column(db.String(10))
    # 合作商
    partner = db.Column(db.String(50))
    # 制单人
    creator = db.Column(db.String(10))
    # 制单时间
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    # 审核状态
    status = db.Column(db.Boolean)
    # 审核人
    reviewer = db.Column(db.String(10))
    # 审核时间
    review_time = db.Column(db.DateTime, default=datetime.datetime.now)