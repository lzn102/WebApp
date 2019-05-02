from Warehouse import warehouse, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .models import *


admin = Admin(app=warehouse, name='系统后台', template_mode='bootstrap3')


class UserView(ModelView):
    can_delete = False  # 不能做删除操作
    # column_display_pk = True  # 显示模型的主键
    column_display_all_relations = True
    column_labels = dict(name='姓名', telephone='手机', role='职位', department='部门', create_time='创建时间')  # 命名数据库字段
    column_exclude_list = ('password', )  # 隐藏的数据库字段


class RoleView(ModelView):
    can_delete = False
    column_labels = dict(name='职位', remark='备注', create_time='创建时间')


class DepartmentView(ModelView):
    can_delete = False
    column_labels = dict(name='部门', superior_category='上级部门', creat_time='创建时间')


class ClientView(ModelView):
    can_delete = False
    column_labels = dict(name='名称', address='地址', contact='联系人', telephone='电话', remark='备注', email='邮件', creat_time='创建时间')


class PartnerCategoryView(ModelView):
    can_delete = False
    column_display_all_relations = True
    column_labels = dict(name='名称', remark='备注', creat_time='创建时间', partners='合作商')


class PartnerView(ModelView):
    can_delete = False
    column_display_all_relations = True
    column_auto_select_related = True
    column_labels = dict(name='名称', address='地址', contact='联系人', telephone='电话', remark='备注', email='邮件', category='类型', creat_time='创建时间')


class UnitView(ModelView):
    can_delete = False
    column_labels = dict(name='名称', creat_time='创建时间')



class StandardView(ModelView):
    can_delete = False
    column_labels = dict(name='名称', remark='备注', creat_time='创建时间')


class GoodsView(ModelView):
    can_delete = False
    column_display_all_relations = True
    column_labels = dict(name='名称', inside_code='内部编号', external_code='外部编号', standard='规格', category='种类', unit='单位', weight='重量', price='价格', remark='备注', creat_time='创建时间')


class DepotCategoryView(ModelView):
    can_delete = False
    column_labels = dict(name='名称', remark='备注', creat_time='创建时间')


class DepotView(ModelView):
    can_delete = False
    column_labels = dict(name='名称', depot_category='类型', address='地址', area='面积', contact='联系人', telephone='电话', remark='备注', creat_time='创建时间')


class TypeIOView(ModelView):
    can_delete = False
    column_labels = dict(name='名称', remark='备注', creat_time='创建时间')


class DepositView(ModelView):
    can_delete = False
    column_display_pk = True
    column_display_all_relations = True
    column_labels = dict(id='单号', goods='产品', code='编号', batch='批次', standard_id='规格', amount='数量', depot='仓库', type_io='出入库类型', partner='合作商', author='制单人', creat_time='制单时间', status='审核状态', check='审核人', check_time='审核时间')


class TakeoutView(ModelView):
    can_delete = False
    column_display_pk = True
    column_labels = dict(id='单号', goods='产品', code='编号', batch='批次', standard='规格', amount='数量', depot='仓库', type_io='出入库类型', client='客户', express='物流单号', author='制单人', creat_time='制单时间', status='审核状态', check='审核人', check_time='审核时间')


class DamagedView(ModelView):
    can_delete = False
    column_display_pk = True
    column_display_all_relations = True

    column_labels = dict(id='单号', goods='产品', code='编号', batch='批次', standard='规格', amount='数量', depot='仓库', type_io='出入库类型', author='制单人', creat_time='制单时间', status='审核状态', check='审核人', check_time='审核时间')


admin.add_view(UserView(User, db.session, name='员工'))
admin.add_view(RoleView(Role, db.session, name='职位'))
admin.add_view(DepartmentView(Department, db.session, name='部门'))
admin.add_view(ClientView(Client, db.session, name='客户'))
admin.add_view(PartnerCategoryView(PartnerCategory, db.session, name='合作商类型'))
admin.add_view(PartnerView(Partner, db.session, name='合作商'))
admin.add_view(UnitView(Unit, db.session, name='单位'))
admin.add_view(StandardView(Standard, db.session, name='规格'))
admin.add_view(GoodsView(Goods, db.session, name='产品'))
admin.add_view(DepotCategoryView(DepotCategory, db.session, name='仓库类型'))
admin.add_view(DepotView(Depot, db.session, name='仓库'))
admin.add_view(TypeIOView(TypeIO, db.session, name='出入库类型'))
admin.add_view(DepositView(Deposit, db.session, name='入库'))
admin.add_view(TakeoutView(Takeout, db.session, name='出库'))
admin.add_view(DamagedView(Damaged, db.session, name='报损'))
