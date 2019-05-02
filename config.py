import os

basedir = os.path.abspath(os.path.dirname(__file__))


# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:168168@127.0.0.1/app'
SQLALCHEMY_TRACK_MODIFICATIONS = True  # 防止SQLAlchemy出现Warning错误
SQLALCHEMY_COMMIT_TEARDOWN = True  # 防止SQLAlchemy出现Warning错误
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')  # 另一个版本的数据库迁移需要的文件
BABEL_DEFAULT_LOCALE = 'zh_CN'