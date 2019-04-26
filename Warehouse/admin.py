from Warehouse import warehouse, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .models import User, Partner, Store


admin = Admin(app=warehouse, name='系统后台', template_mode='bootstrap3')


class UserView(ModelView):
    can_delete = False
    # 命名数据库字段
    column_labels = dict(
        name='姓名',
        phone='手机',
        role='角色',
        create_time='创建时间'
    )
    # 隐藏的数据库字段
    column_exclude_list = (
        'password'
    )


admin.add_view(UserView(User, db.session, name='员工'))
admin.add_view(ModelView(Partner, db.session, name='合作商'))
admin.add_view(ModelView(Store, db.session, name='仓库'))
