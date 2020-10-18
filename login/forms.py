#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : linjie
from django import forms

class UserForm(forms.Form):
    '''表单模型'''
    username = forms.CharField(label='用户名',max_length=128)
    pwd = forms.CharField(label='密码', max_length=256,widget=forms.PasswordInput)#widget=forms.PasswordInput用于指定该字段在form表单里表现为<input type='password' />，也就是密码输入框。
