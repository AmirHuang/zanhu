# _*_ coding: utf-8 _*_
# @time     : 2020/04/12
# @Author   : Amir
# @Site     : 
# @File     : urls.py
# @Software : PyCharm


from django.urls import path

from zanhu.messager import views

app_name = 'messager'

urlpatterns = [
    path('', views.MessagesListView.as_view(), name='messages_list'),
    path('send-message/', views.send_message, name='send_message'),
    path('<username>/', views.ConversationListView.as_view(), name='conversation_detail'),
]
