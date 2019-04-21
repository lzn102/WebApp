from Warehouse import warehouse as app
from Warehouse import db
from flask import render_template, redirect, flash, url_for
from flask import request  # request.args.get 方法获取html指定name的值
from .forms import LoginForm
from .models import User, Store


@app.route('/', methods=['GET', 'POST'])
def register():
    form = LoginForm()

    # 确认手机号码是否被注册过
    have_phone = User.query.filter_by(phone=form.telephone.data).all()
    if have_phone:
        context = {
            "content": '该手机号已被注册,请确认或更换手机号码!'
        }
        return render_template('register.html', form=form, context=context)

    # 表单提交验证
    if request.method == "POST":
        # form.validate_on_submit() 等于 method验证+form验证, 缺点是有些情况表单验证错误不提示
        if form.validate():
            username = form.username.data
            telephone = form.telephone.data
            role = form.role.data
            password = form.password.data
            user = User(name=username, phone=telephone, role=role, password=password)
            db.session.add(user)
            db.session.commit()
            return '注册成功'

        # 表单验证失败
        else:
            context1 = {
                'content':'注册失败,请按照提示重新尝试;若无提示请联系网站管理员'
            }
            return render_template('register.html', form=form, context1=context1)

    # GET请求返回的Html页面
    else:
        return render_template('register.html', form=form)
