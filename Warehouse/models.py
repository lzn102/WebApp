from Warehouse import db
import datetime


# 员工
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(10))  # 姓名
    telephone = db.Column(db.Integer)  # 手机
    role = db.relationship('Role')  # 职位
    role_id = db.Column(db.String(200), db.ForeignKey('role.id'))  # 对应的外键
    department = db.relationship('Department')  # 部门
    department_id = db.Column(db.String(200), db.ForeignKey('department.id'))  # 对应的外键
    password = db.Column(db.String(50))  # 密码
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间
    deposit = db.Column(db.String(200), db.ForeignKey('deposit.id'))
    takeout = db.Column(db.String(200), db.ForeignKey('takeout.id'))
    Damaged = db.Column(db.String(200), db.ForeignKey('damaged.id'))

    def __repr__(self):
        return '{}'.format(self.name)


# 职位
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(10))  # 职位名
    remark = db.Column(db.String(200))  # 备注
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


# 客户
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    address = db.Column(db.String(200))  # 地址
    contact = db.Column(db.String(200))  # 联系人
    telephone = db.Column(db.Integer)  # 电话
    remark = db.Column(db.String(200))  # 备注
    email = db.Column(db.String(200))  # 邮件
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间
    takeout = db.Column(db.String(200), db.ForeignKey('takeout.id'))

    def __repr__(self):
        return '{}'.format(self.name)


# 合作商类型
class PartnerCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    remark = db.Column(db.String(200))  # 备注
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间

    def __repr__(self):
        return '{}'.format(self.name)


# 合作商
class Partner(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    address = db.Column(db.String(200))  # 地址
    contact = db.Column(db.String(200))  # 联系人
    telephone = db.Column(db.Integer)  # 电话
    remark = db.Column(db.String(200))  # 备注
    email = db.Column(db.String(200))  # 邮件
    category = db.relationship('PartnerCategory')  # 类型
    partners = db.Column(db.String(200), db.ForeignKey('partner_category.id'))
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间
    deposit = db.Column(db.String(200), db.ForeignKey('deposit.id'))

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
    inside_code = db.Column(db.String(200))  # 内部编号
    external_code = db.Column(db.String(200))  # 外部编号
    standard = db.relationship('Standard')  # 规格（尺码、长度等）
    standard_id = db.Column(db.String(200), db.ForeignKey('standard.id'))
    unit = db.relationship('Unit')  # 单位
    unit_id = db.Column(db.String(200), db.ForeignKey('unit.id'))
    weight = db.Column(db.Integer)  # 重量
    price = db.Column(db.Float)  # 价格
    remark = db.Column(db.String(200))  # 备注
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间
    deposit = db.Column(db.String(200), db.ForeignKey('deposit.id'))
    takeout = db.Column(db.String(200), db.ForeignKey('takeout.id'))
    Damaged = db.Column(db.String(200), db.ForeignKey('damaged.id'))

    def __repr__(self):
        return '{}'.format(self.name)


# 仓库类型
class DepotCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    remark = db.Column(db.String(200))  # 备注
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间

    def __repr__(self):
        return '{}'.format(self.name)


# 仓库
class Depot(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    category_id = db.Column(db.String(200), db.ForeignKey('depot_category.id'))  # 仓库类型
    depot_category = db.relationship('DepotCategory')
    address = db.Column(db.String(200))  # 地址
    area = db.Column(db.Integer)  # 面积
    contact = db.Column(db.String(200))  # 联系人
    telephone = db.Column(db.Integer)  # 电话
    remark = db.Column(db.String(200))  # 备注
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间
    deposit = db.Column(db.String(200), db.ForeignKey('deposit.id'))
    takeout = db.Column(db.String(200), db.ForeignKey('takeout.id'))
    Damaged = db.Column(db.String(200), db.ForeignKey('damaged.id'))

    def __repr__(self):
        return '{}'.format(self.name)


# 出入库类型
class TypeIO(db.Model):
    __tablename__ = 'type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    remark = db.Column(db.String(200))  # 备注
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间
    deposit = db.Column(db.String(200), db.ForeignKey('deposit.id'))
    takeout = db.Column(db.String(200), db.ForeignKey('takeout.id'))
    Damaged = db.Column(db.String(200), db.ForeignKey('damaged.id'))

    def __repr__(self):
        return '{}'.format(self.name)


# 入库管理
class Deposit(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 订单号
    goods = db.relationship('Goods')  # 产品
    amount = db.Column(db.Integer)  # 数量
    depot = db.relationship('Depot')  # 仓库
    type_io = db.relationship('TypeIO')  # 出入库类型
    partner = db.relationship('Partner')  # 合作商
    author = db.relationship('User')  # 制单人
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 制单时间
    status = db.Column(db.Boolean, default=False)  # 审核状态
    check = db.relationship('User')  # 审核人
    check_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 审核时间

    def __repr__(self):
        return '{}'.format(self.name)


# 出库管理
class Takeout(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 订单号
    goods = db.relationship('Goods')  # 产品
    amount = db.Column(db.Integer)  # 数量
    depot = db.relationship('Depot')  # 仓库
    type_io = db.relationship('TypeIO')  # 出入库类型
    client = db.relationship('Client')  # 客户
    express = db.Column(db.String(200))  # 物流单号
    author = db.relationship('User')  # 制单人
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 制单时间
    status = db.Column(db.Boolean, default=False)  # 审核状态
    check = db.relationship('User')  # 审核人
    check_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 审核时间

    def __repr__(self):
        return '{}'.format(self.name)


# 报损管理
class Damaged(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 订单号
    goods = db.relationship('Goods')  # 产品名
    amount = db.Column(db.Integer)  # 数量
    depot = db.relationship('Depot')  # 仓库
    type_io = db.relationship('TypeIO')  # 出入库类型
    author = db.relationship('User')  # 制单人
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 制单时间
    status = db.Column(db.Boolean, default=False)  # 审核状态
    check = db.relationship('User')  # 审核人
    check_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 审核时间

    def __repr__(self):
        return '{}'.format(self.name)


