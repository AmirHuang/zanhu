# _*_ coding: utf-8 _*_
# @time     : 2020/04/11
# @Author   : Amir
# @Site     : 
# @File     : forms.py
# @Software : PyCharm

from django import forms

from markdownx.fields import MarkdownxFormField

from zanhu.qa.models import Question


from django import forms
from markdownx.fields import MarkdownxFormField

from zanhu.qa.models import Question


class QuestionForm(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())  # 隐藏
    content = MarkdownxFormField()

    class Meta:
        model = Question
        fields = ["title", "content", "tags", "status"]

