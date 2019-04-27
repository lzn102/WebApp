from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from Warehouse import warehouse, db


migrate = Migrate(warehouse, db)
manager = Manager(warehouse)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

"""

命令行输入创建和迁移数据库 （类似 Django manage.py）

python manage.py db init        创建数据表
python manage.py db migrate     提交修改
python manage.py db upgrade     执行修改
python manage.py db downgrade   回退修改

"""
