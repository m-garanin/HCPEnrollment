#-*- coding:utf-8 -*-
r"""
>>> from django.test.client import Client
>>> from django.contrib.auth.models import User, Permission

>>> from app.models import *

>>> c = Client()

Index-page
==================================
>>> r = c.get('/')
>>> r.status_code
200


Registration (Simple)
==================================
sign-up
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
>>> user = User.objects.get(username='smith')
>>> user.provider is None
False

sign-in
-------
>>> c.login(username=user.username, password='123')
True


Profile
===================================
>>> section_url = '/section/%s/edit/'

>>> r = c.get('/users/smith/')
>>> r.status_code
301


section A
---------
>>> r = c.get(section_url % 'A')
>>> r.status_code
200
>>> r.content
'...Sec A...Sec B...'


>>> r = c.post(section_url % 'A', {'new_provider': True})
>>> r.status_code
302



section B
---------
>>> r = c.get(section_url % 'B')
>>> r.status_code
200


"""
