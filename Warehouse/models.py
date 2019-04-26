from Warehouse import db
import datetime


# 仓库表
class Store(db.Model):
    # 单号
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 名称
    name = db.Column(db.String(200))
    # 编号
    serial = db.Column(db.String(50))
    # 规格
    size = db.Column(db.String(20))
    # 数量
    number = db.Column(db.Integer)
    # 单位
    unit = db.Column(db.String(5))
    # 类别
    category = db.Column(db.String(10))
    # 合作商
    partner = db.Column(db.String(50))
    # 制单人
    creator = db.Column(db.String(10))
    # 制单时间
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    # 审核状态
    status = db.Column(db.Boolean)
    # 审核人
    reviewer = db.Column(db.String(10))
    # 审核时间
    review_time = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return '{}'.format(self.name)


# 合作商表
class Partner(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return '{}'.format(self.name)


# 员工表
class User(db.Model):
    # 用户ID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 名字
    name = db.Column(db.String(10))
    # 电话
    phone = db.Column(db.Integer)
    # 角色
    role = db.Column(db.String(20))
    # 密码
    password = db.Column(db.String(50))
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return '{}'.format(self.name)

