# _*_ coding: utf-8 _*_
# @time     : 2020/04/13
# @Author   : Amir
# @Site     : 
# @File     : test.py
# @Software : PyCharm


import os
import sys
import django
from channels.routing import get_default_application

# application加入查找路径中
app_path = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir))
print(app_path)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.pardir)
print(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
# sys.path.append(os.path.join(app_path, 'zanhu'))  # ../zanhu/zanhu

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
# django.setup()
# application = get_default_application()
