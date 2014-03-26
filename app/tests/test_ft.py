#-*- coding:utf-8 -*-
r"""
>>> from django.test.client import Client
>>> from django.contrib.auth.models import User, Permission

>>> from app.models import *

>>> c = Client()

Index-page
===========
>>> r = c.get('/')
>>> r.status_code
200

Registration (Simple)
=====================
sign-in
-------
>>> r = c.get('/accounts/register/')
>>> r.status_code
200
>>> r = c.post('/accounts/register/')
>>> r.status_code
200
>>> r = c.post('/accounts/register/', {'username': 'smith', 'email':'smith@test.eu','password1':'123', 'password2':'123'})
>>> r.status_code
302

check provider-object for new user
>>> u = User.objects.get(username='smith')
>>> u.provider is None
False


"""
