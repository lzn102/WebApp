from Warehouse import db
import datetime


# 员工
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(10))  # 姓名
    telephone = db.Column(db.Integer)  # 手机
    role = db.relationship('Role')  # 职位
    department = db.relationship('Department')  # 部门
    password = db.Column(db.String(50))  # 密码
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间
    deposit = db.Column(db.String(200), db.ForeignKey('deposit.id'))
    takeout = db.Column(db.String(200), db.ForeignKey('takeout.id'))
    Damaged = db.Column(db.String(200), db.ForeignKey('damaged.id'))


# 职位
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(10))  # 职位名
    remark = db.Column(db.String)  # 备注
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间
    user = db.Column(db.String(200), db.ForeignKey('user.id'))  # 对应的外键

    def __repr__(self):
        return '{}'.format(self.name)


# 部门
class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    superior_category = db.Column(db.String(200))  # 父类别
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间
    user = db.Column(db.String(200), db.ForeignKey('user.id'))  # 对应的外键

    def __repr__(self):
        return '{}'.format(self.name)


# 客户
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    address = db.Column(db.String(200))  # 地址
    contact = db.Column(db.String(200))  # 联系人
    telephone = db.Column(db.Integer)  # 电话
    remark = db.Column(db.String())  # 备注
    email = db.Column(db.String(200))  # 邮件
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间
    takeout = db.Column(db.String(200), db.ForeignKey('takeout.id'))


# 合作商类型
class PartnerCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    remark = db.Column(db.String())  # 备注
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间
    partners = db.Column(db.String(200), db.ForeignKey('partner.id'))

    def __repr__(self):
        return '{}'.format(self.name)


# 合作商
class Partner(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    address = db.Column(db.String(200))  # 地址
    contact = db.Column(db.String(200))  # 联系人
    telephone = db.Column(db.Integer)  # 电话
    remark = db.Column(db.String)  # 备注
    email = db.Column(db.String(200))  # 邮件
    category = db.relationship('PartnerCategory')  # 类型
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间
    deposit = db.Column(db.String(200), db.ForeignKey('deposit.id'))


# 计量单位
class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间
    goods = db.Column(db.String(200), db.ForeignKey('goods.id'))

    def __repr__(self):
        return '{}'.format(self.name)


# 产品类别
class GoodsCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    remark = db.Column(db.String)  # 备注
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间
    goods = db.Column(db.String(200), db.ForeignKey('goods.id'))

    def __repr__(self):
        return '{}'.format(self.name)


# 产品规格
class Standard(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    remark = db.Column(db.String)  # 备注
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间
    goods = db.Column(db.String(200), db.ForeignKey('goods.id'))

    def __repr__(self):
        return '{}'.format(self.name)


# 产品管理
class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    inside_code = db.Column(db.String(200))  # 内部编号
    external_code = db.Column(db.String(200))  # 外部编号
    # standard_id = db.Column(db.String(200), db.ForeignKey('standard.id'))
    standard = db.relationship('Standard')  # 规格（尺码、长度等）
    # category_id = db.Column(db.String(200), db.ForeignKey('good_category.id'))
    category = db.relationship('GoodsCategory')  # 种类
    # unit_id = db.Column(db.String(200), db.ForeignKey('unit.id'))
    unit = db.relationship('Unit')  # 单位
    weight = db.Column(db.Integer)  # 重量
    price = db.Column(db.Float)  # 价格
    remark = db.Column(db.String)  # 备注
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
    remark = db.Column(db.String)  # 备注
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
    remark = db.Column(db.String)  # 备注
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间
    deposit = db.Column(db.String(200), db.ForeignKey('deposit.id'))
    takeout = db.Column(db.String(200), db.ForeignKey('takeout.id'))
    Damaged = db.Column(db.String(200), db.ForeignKey('damaged.id'))


# 出入库类型
class TypeIO(db.Model):
    __tablename__ = 'type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    remark = db.Column(db.String)  # 备注
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间
    deposit = db.Column(db.String(200), db.ForeignKey('deposit.id'))
    takeout = db.Column(db.String(200), db.ForeignKey('takeout.id'))
    Damaged = db.Column(db.String(200), db.ForeignKey('damaged.id'))

    def __repr__(self):
        return '{}'.format(self.name)


# 入库管理
class Deposit(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 订单号
    # goods_id = db.Column(db.String(200))  # 产品名
    goods = db.relationship('Goods')
    code = db.Column(db.Integer)  # 产品编号
    batch = db.Column(db.Integer)  # 批次
    standard_id = db.Column(db.String(200))  # 规格（尺码、长度等）
    amount = db.Column(db.Integer)  # 数量
    # depot_id = db.Column(db.String(200), db.ForeignKey('depot.id'))  # 仓库
    depot = db.relationship('Depot')
    # type_id = db.Column(db.String(200), db.ForeignKey('type.id'))  # 出入库类型
    type_io = db.relationship('TypeIO')
    # partner_id = db.Column(db.String(200), db.ForeignKey('partner.id'))  # 合作商
    partner = db.relationship('Partner')
    # author_id = db.Column(db.String(200), db.ForeignKey('user.id'))  # 制单人
    author = db.relationship('User')
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 制单时间
    status = db.Column(db.Boolean, default=False)  # 审核状态
    # check_id = db.Column(db.String(200), db.ForeignKey('user.id'))  # 审核人
    check = db.relationship('User')
    check_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 审核时间





# 出库管理
class Takeout(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 订单号
    # goods_id = db.Column(db.String(200))  # 产品名
    goods = db.relationship('Goods')
    code = db.Column(db.Integer)  # 产品编号
    batch = db.Column(db.Integer)  # 批次
    standard_id = db.Column(db.String(200))  # 规格（尺码、长度等）
    amount = db.Column(db.Integer)  # 数量
    # depot_id = db.Column(db.String(200))  # 仓库
    depot = db.relationship('Depot')
    # type_id = db.Column(db.String(200))  # 出入库类型
    type_io = db.relationship('TypeIO')
    # client_id = db.Column(db.String(200))  # 客户
    client = db.relationship('Client')
    express = db.Column(db.String(200))  # 物流单号
    # author_id = db.Column(db.String(200))  # 制单人
    author = db.relationship('User')
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 制单时间
    status = db.Column(db.Boolean, default=False)  # 审核状态
    # check_id = db.Column(db.String(200))  # 审核人
    check = db.relationship('User')
    check_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 审核时间


# 报损管理
class Damaged(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 订单号
    # goods_id = db.Column(db.String(200))  # 产品名
    goods = db.relationship('Goods')
    code = db.Column(db.Integer)  # 产品编号
    batch = db.Column(db.Integer)  # 批次
    standard_id = db.Column(db.String(200))  # 规格（尺码、长度等）
    amount = db.Column(db.Integer)  # 数量
    # depot_id = db.Column(db.String(200))  # 仓库
    depot = db.relationship('Depot')
    # type_id = db.Column(db.String(200))  # 出入库类型
    type_io = db.relationship('TypeIO')
    # author_id = db.Column(db.String(200))  # 制单人
    author = db.relationship('User')
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 制单时间
    status = db.Column(db.Boolean, default=False)  # 审核状态
    # check_id = db.Column(db.String(200))  # 审核人
    check = db.relationship('User')
    check_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 审核时间


