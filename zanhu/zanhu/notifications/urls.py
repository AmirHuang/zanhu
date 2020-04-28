# _*_ coding: utf-8 _*_
# @time     : 2020/04/16
# @Author   : Amir
# @Site     : 
# @File     : urls.py
# @Software : PyCharm

from django.urls import path

from zanhu.notifications import views

app_name = 'notifications'

urlpatterns = [
    path('', views.NotificationUnreadListView.as_view(), name='unread'),
    path('mark-as-read/<slug>/', views.mark_as_read, name='mark_as_read'),
    path('mark-all-as-read/', views.mark_all_as_read, name='mark_all_read'),
    path('latest-notifications/', views.get_latest_notifications, name='latest_notifications'),
]

