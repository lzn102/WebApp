from Warehouse import db
import datetime

# 多对多关系表
association_table = db.Table(
    'association',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('department_id', db.Integer, db.ForeignKey('department.id')),
    db.Column('partnerCategory_id', db.Integer, db.ForeignKey('partner_category.id')),
    db.Column('partner_id', db.Integer, db.ForeignKey('partner.id')),
    db.Column('unit_id', db.Integer, db.ForeignKey('unit.id')),
    db.Column('standard_id', db.Integer, db.ForeignKey('standard.id')),
    db.Column('goods_id', db.Integer, db.ForeignKey('goods.id')),
    db.Column('depotCategory_id', db.Integer, db.ForeignKey('depot_category.id')),
    db.Column('depot_id', db.Integer, db.ForeignKey('depot.id')),
    db.Column('type_id', db.Integer, db.ForeignKey('type.id')),
    db.Column('client_id', db.Integer, db.ForeignKey('client.id')),
    db.Column('deposit_id', db.Integer, db.ForeignKey('deposit.id')),
    db.Column('takeout_id', db.Integer, db.ForeignKey('takeout.id')),
    db.Column('damaged_id', db.Integer, db.ForeignKey('damaged.id')),
)


# 职位
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(10))  # 职位名
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间

    def __repr__(self):
        return '{}'.format(self.name)


# 部门
class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间

    def __repr__(self):
        return '{}'.format(self.name)


# 员工
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(10))  # 姓名
    telephone = db.Column(db.String(20))  # 手机
    password = db.Column(db.String(50))  # 密码
    department = db.relationship('Department', secondary=association_table)  # 部门
    role = db.relationship('Role', secondary=association_table)  # 职位
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间

    def __repr__(self):
        return '{}'.format(self.name)


# 客户
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    address = db.Column(db.String(200))  # 地址
    contact = db.Column(db.String(200))  # 联系人
    telephone = db.Column(db.String(20))  # 电话
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间

    def __repr__(self):
        return '{}'.format(self.name)


# 合作商类型
class PartnerCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间

    def __repr__(self):
        return '{}'.format(self.name)


# 合作商
class Partner(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    address = db.Column(db.String(200))  # 地址
    contact = db.Column(db.String(200))  # 联系人
    telephone = db.Column(db.String(20))  # 电话
    category = db.relationship('PartnerCategory', secondary=association_table)
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间

    def __repr__(self):
        return '{}'.format(self.name)


# 计量单位
class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间

    def __repr__(self):
        return '{}'.format(self.name)


# 产品规格
class Standard(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    remark = db.Column(db.String(200))  # 备注
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间

    def __repr__(self):
        return '{}'.format(self.name)



# 产品管理
class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    code = db.Column(db.String(200))  # 编号
    standard = db.relationship('Standard', secondary=association_table)  # 规格（尺码、长度等）
    unit = db.relationship('Unit', secondary=association_table)  # 单位
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间

    def __repr__(self):
        return '{0}'.format(self.code)


# 仓库类型
class DepotCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间

    def __repr__(self):
        return '{}'.format(self.name)


# 仓库
class Depot(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    category = db.relationship('DepotCategory', secondary=association_table)  # 种类
    address = db.Column(db.String(200))  # 地址
    contact = db.Column(db.String(200))  # 联系人
    telephone = db.Column(db.String(20))  # 电话
    remark = db.Column(db.String(200))  # 备注
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间

    def __repr__(self):
        return '{}'.format(self.name)


# 出入库类型
class TypeIO(db.Model):
    __tablename__ = 'type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间

    def __repr__(self):
        return '{}'.format(self.name)


# 入库管理
class Deposit(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 订单号
    goods = db.relationship('Goods', secondary=association_table)  # 产品
    amount = db.Column(db.Integer)  # 数量
    depot = db.relationship('Depot', secondary=association_table)  # 仓库
    type_io = db.relationship('TypeIO', secondary=association_table)  # 出入库类型
    partner = db.relationship('Partner', secondary=association_table)  # 合作商
    author = db.relationship('User', secondary=association_table)  # 制单人
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 制单时间
    status = db.Column(db.Boolean, default=False)  # 审核状态
    check = db.relationship('User', secondary=association_table)  # 审核人
    check_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 审核时间

    def __repr__(self):
        return '{}'.format(self.goods)


# 出库管理
class Takeout(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 订单号
    goods = db.relationship('Goods', secondary=association_table)  # 产品
    amount = db.Column(db.Integer)  # 数量
    depot = db.relationship('Depot', secondary=association_table)  # 仓库
    type_io = db.relationship('TypeIO', secondary=association_table)  # 出入库类型
    client = db.relationship('Client', secondary=association_table)  # 客户
    express = db.Column(db.String(200))  # 物流单号
    author = db.relationship('User', secondary=association_table)  # 制单人
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 制单时间
    status = db.Column(db.Boolean, default=False)  # 审核状态
    check = db.relationship('User', secondary=association_table)  # 审核人
    check_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 审核时间

    def __repr__(self):
        return '{}'.format(self.name)


# 报损管理
class Damaged(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 订单号
    goods = db.relationship('Goods', secondary=association_table)  # 产品名
    amount = db.Column(db.Integer)  # 数量
    depot = db.relationship('Depot', secondary=association_table)  # 仓库
    type_io = db.relationship('TypeIO', secondary=association_table)  # 出入库类型
    author = db.relationship('User', secondary=association_table)  # 制单人
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 制单时间
    status = db.Column(db.Boolean, default=False)  # 审核状态
    check = db.relationship('User', secondary=association_table)  # 审核人
    check_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 审核时间

    def __repr__(self):
        return '{}'.format(self.name)

