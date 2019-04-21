from Warehouse import warehouse as app
from Warehouse import db
from flask import render_template, redirect, flash, url_for
from flask import request  # request.args.get 方法获取html指定name的值
from .forms import LoginForm
from .models import User, Store


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()

    if request.method == "POST":
        if form.validate():
            username = form.username.data
            telephone = form.telephone.data
            # role = form.role.data
            password = form.password.data
            user = User(name=username, phone=telephone, password=password)
            db.session.add(user)
            db.session.commit()
            return '注册成功'

        else:
            return '注册失败'
    else:
        return render_template('index.html', form=form)
