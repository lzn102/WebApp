from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_babelex import Babel


# 创建应用文件
warehouse = Flask(__name__)
# 国际化语言设置
babel = Babel(warehouse)
# 引入配置文件
warehouse.config.from_object('config')
# 创建数据库模型
db = SQLAlchemy(warehouse)
# 设置表单CSRF的生成秘钥
warehouse.secret_key = 'willy&li'


from Warehouse import views, models, admin

