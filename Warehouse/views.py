from Warehouse import warehouse as app
from Warehouse import db
from flask import render_template, redirect, flash, url_for
from flask import request  # request.args.get 方法获取html指定name的值
from .forms import RegisterForm, LoginForm
from .models import User, Deposit, Takeout
from datetime import datetime, date, timedelta


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    login_form = LoginForm()

    # 确认手机号码是否被注册过
    have_phone = User.query.filter_by(telephone=form.telephone.data).count()
    if have_phone != 0:
        context = {
            "content": '该手机号已被注册,请确认或更换手机号码!'
        }
        return render_template('register.html', form=form, context=context)

    # 表单提交验证
    elif request.method == "POST":
        # form.validate_on_submit() 等于 method验证+form验证, 缺点是有些情况表单验证错误不提示
        if form.validate():
            username = form.username.data
            telephone = form.telephone.data
            role = form.role.data
            password = form.password.data
            user = User(name=username, telephone=telephone, role=role, password=password)
            db.session.add(user)
            db.session.commit()
            # return render_template('login.html', form=login_form)
            return redirect(url_for(login))
        # 表单验证失败
        else:
            context1 = {
                'content':'注册失败,请按照提示重新尝试;若无提示请联系网站管理员'
            }
            return render_template('register.html', form=form, context1=context1)

    # GET请求返回的Html页面
    else:
        return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        # 确认手机号码是否被注册过
        have_phone = User.query.filter_by(telephone=form.telephone.data).count()
        if have_phone == 0:
            context = {
                "content": '该手机号未注册,请先去注册!'
            }
            return render_template('login.html', form=form, context=context)

        elif form.validate():
            telephone = form.telephone.data
            password = form.password.data

            user = User.query.filter_by(telephone=telephone).first()
            if user.password == password:
                return 'login'

            context1 = {
                "content": "密码错误!"
            }
            return render_template('login.html', form=form, context1=context1)

    return render_template('login.html', form=form)


@app.route('/', methods=['GET', 'POST'])
def index():
    today = datetime.now().strftime('%Y-%m-%d')
    if request.method == 'POST':
        if request.args.get('date') == today:
            yesterday = (date.today() + timedelta(days=-1)).strftime("%Y-%m-%d")
            deposit_list = Deposit.query.filter(Deposit.creat_time.contains(yesterday)).all()
            takeout_list = Takeout.query.filter(Takeout.creat_time.contains(yesterday)).all()
            context1 = {
                "deposits": deposit_list,
                "takeouts": takeout_list
            }
            return render_template('index.html', context1=context1)
        return 'hello'
    else:
        deposit_list = Deposit.query.filter(Deposit.creat_time.contains(today)).all()
        takeout_list = Takeout.query.filter(Takeout.creat_time.contains(today)).all()

        context = {
            "deposits": deposit_list,
            "takeouts": takeout_list
        }

        return render_template('index.html', context=context)
