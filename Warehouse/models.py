from Warehouse import db
import datetime


# 仓库
# class Store(db.Model):
#     # 单号
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     # 名称
#     name = db.Column(db.String(200))
#     # 编号
#     serial = db.Column(db.String(50))
#     # 规格
#     size = db.Column(db.String(20))
#     # 数量
#     number = db.Column(db.Integer)
#     # 单位
#     unit = db.Column(db.String(5))
#     # 类别
#     category = db.Column(db.String(10))
#     # 合作商
#     partner = db.Column(db.String(50))
#     # 制单人
#     creator = db.Column(db.String(10))
#     # 制单时间
#     create_time = db.Column(db.DateTime, default=datetime.datetime.now)
#     # 审核状态
#     status = db.Column(db.Boolean)
#     # 审核人
#     reviewer = db.Column(db.String(10))
#     # 审核时间
#     review_time = db.Column(db.DateTime, default=datetime.datetime.now)
#
#     def __repr__(self):
#         return '{}'.format(self.name)


# 员工

# 员工
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(10))  # 姓名
    telephone = db.Column(db.Integer)  # 手机
    role = db.Column(db.String(20))  # 身份
    password = db.Column(db.String(50))  # 密码
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间


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
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    superior_category = db.Column(db.String(200))  # 父类别
    remark = db.Column(db.String)  # 备注
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间


# 产品管理
class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    name = db.Column(db.String(200))  # 名称
    inside_code = db.Column(db.String(200))  # 内部编号
    external_code = db.Column(db.String(200))  # 外部编号
    standard = db.Column(db.String(200))  # 规格（尺码、长度等）
    unit = db.Column(db.String(200), db.ForeignKey('unit.id'))  # 单位
    package = db.Column(db.String(200))  # 包装类型（袋装、箱装）
    weight = db.Column(db.Integer)  # 重量
    price = db.Column(db.Float)  # 价格
    remark = db.Column(db.String)  # 备注
    creat_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 创建时间
