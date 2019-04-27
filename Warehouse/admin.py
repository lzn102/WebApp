from Warehouse import warehouse, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .models import *


admin = Admin(app=warehouse, name='系统后台', template_mode='bootstrap3')


class UserView(ModelView):
    can_delete = False
    # 命名数据库字段
    column_labels = dict(
        name='姓名',
        telephone='手机',
        role='角色',
        create_time='创建时间'
    )
    # 隐藏的数据库字段
    column_exclude_list = (
        'password'
    )


admin.add_view(UserView(User, db.session, name='员工'))
admin.add_view(ModelView(Role, db.session, name='职位'))
admin.add_view(ModelView(Department, db.session, name='部门'))
admin.add_view(ModelView(Client, db.session, name='客户'))
admin.add_view(ModelView(Partner, db.session, name='合作商'))
admin.add_view(ModelView(Unit, db.session, name='单位'))
admin.add_view(ModelView(GoodsCategory, db.session, name='产品种类'))
admin.add_view(ModelView(Standard, db.session, name='规格'))
admin.add_view(ModelView(Goods, db.session, name='产品'))
admin.add_view(ModelView(DepotCategory, db.session, name='仓库类型'))
admin.add_view(ModelView(Depot, db.session, name='仓库'))
admin.add_view(ModelView(TypeIO, db.session, name='出入库类型'))
admin.add_view(ModelView(Deposit, db.session, name='入库'))
admin.add_view(ModelView(Takeout, db.session, name='出库'))
admin.add_view(ModelView(Damaged, db.session, name='报损'))
