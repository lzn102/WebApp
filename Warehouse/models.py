from Warehouse import db
import datetime


# 员工
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(10))  # 姓名
    telephone = db.Column(db.Integer)  # 手机
    role = db.Column(db.String(20))  # 职位
    password = db.Column(db.String(50))  # 密码
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间


# 职位
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(10))  # 职位名
    remark = db.Column(db.String)  # 备注
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间


# 部门
class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    superior_category = db.Column(db.String(200))  # 父类别
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间


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


# 合作商
class Partner(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    address = db.Column(db.String(200))  # 地址
    contact = db.Column(db.String(200))  # 联系人
    telephone = db.Column(db.Integer)  # 电话
    remark = db.Column(db.String)  # 备注
    email = db.Column(db.String(200))  # 邮件
    category = db.Column(db.String(200))
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间


# 计量单位
class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间


# 产品类别
class GoodsCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    superior_category = db.Column(db.String(200))  # 父类别
    remark = db.Column(db.String)  # 备注
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间


# 产品规格
class Standard(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    remark = db.Column(db.String)  # 备注
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间


# 产品管理
class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    inside_code = db.Column(db.String(200))  # 内部编号
    external_code = db.Column(db.String(200))  # 外部编号
    standard = db.Column(db.String(200), db.ForeignKey('standard.id'))  # 规格（尺码、长度等）
    category = db.Column(db.String(200), db.ForeignKey('goods_category.id'))  # 种类
    unit = db.Column(db.String(200), db.ForeignKey('unit.id'))  # 单位
    package = db.Column(db.String(200))  # 包装类型（袋装、箱装）
    weight = db.Column(db.Integer)  # 重量
    price = db.Column(db.Float)  # 价格
    remark = db.Column(db.String)  # 备注
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间


# 仓库类型
class DepotCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    remark = db.Column(db.String)  # 备注
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间


# 仓库
class Depot(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    category = db.Column(db.String(200), db.ForeignKey('depot_category.id'))  # 仓库类型
    address = db.Column(db.String(200))  # 地址
    area = db.Column(db.Integer)  # 面积
    contact = db.Column(db.String(200))  # 联系人
    telephone = db.Column(db.Integer)  # 电话
    remark = db.Column(db.String)  # 备注
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间


# 出入库类型
class TypeIO(db.Model):
    __tablename__ = 'type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    remark = db.Column(db.String)  # 备注
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间


# 入库管理
class Deposit(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  #订单号
    goods = db.Column(db.String(200), db.ForeignKey('goods.id'))  # 产品名
    code = db.Column(db.Integer)  # 产品编号
    batch = db.Column(db.Integer)  # 批次
    standard = db.Column(db.String(200), db.ForeignKey('standard.id'))  # 规格（尺码、长度等）
    amount = db.Column(db.Integer)  # 数量
    depot = db.Column(db.String(200), db.ForeignKey('depot.id'))  # 仓库
    type_io = db.Column(db.String(200), db.ForeignKey('type.id'))  # 出入库类型
    partner = db.Column(db.String(200), db.ForeignKey('partner.id'))  # 合作商
    author = db.Column(db.String(200), db.ForeignKey('user.id'))  # 制单人
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 制单时间
    status = db.Column(db.Boolean, default=False)  # 审核状态
    check = db.Column(db.String(200), db.ForeignKey('user.id'))  # 审核人
    check_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 审核时间


# 出库管理
class Takeout(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 订单号
    goods = db.Column(db.String(200), db.ForeignKey('goods.id'))  # 产品名
    code = db.Column(db.Integer)  # 产品编号
    batch = db.Column(db.Integer)  # 批次
    standard = db.Column(db.String(200), db.ForeignKey('standard.id'))  # 规格（尺码、长度等）
    amount = db.Column(db.Integer)  # 数量
    depot = db.Column(db.String(200), db.ForeignKey('depot.id'))  # 仓库
    type_io = db.Column(db.String(200), db.ForeignKey('type.id'))  # 出入库类型
    client = db.Column(db.String(200), db.ForeignKey('client.id'))  # 客户
    express = db.Column(db.String(200))  # 物流单号
    author = db.Column(db.String(200), db.ForeignKey('user.id'))  # 制单人
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 制单时间
    status = db.Column(db.Boolean, default=False)  # 审核状态
    check = db.Column(db.String(200), db.ForeignKey('user.id'))  # 审核人
    check_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 审核时间


# 报损管理
class Damaged(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 订单号
    goods = db.Column(db.String(200), db.ForeignKey('goods.id'))  # 产品名
    code = db.Column(db.Integer)  # 产品编号
    batch = db.Column(db.Integer)  # 批次
    standard = db.Column(db.String(200), db.ForeignKey('standard.id'))  # 规格（尺码、长度等）
    amount = db.Column(db.Integer)  # 数量
    depot = db.Column(db.String(200), db.ForeignKey('depot.id'))  # 存入仓库
    type_io = db.Column(db.String(200), db.ForeignKey('type.id'))  # 出入库（报损）类型
    author = db.Column(db.String(200), db.ForeignKey('user.id'))  # 制单人
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 制单时间
    status = db.Column(db.Boolean, default=False)  # 审核状态
    check = db.Column(db.String(200), db.ForeignKey('user.id'))  # 审核人
    check_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 审核时间

