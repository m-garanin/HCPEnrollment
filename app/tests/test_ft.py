#-*- coding:utf-8 -*-
r"""
>>> from django.test.client import Client
>>> from django.contrib.auth.models import User, Permission

>>> from app.models import Provider

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


>>> r = c.post(section_url % 'A', {'npi': '123','new_provider': True})
>>> r.status_code
302


section B
---------
>>> r = c.get(section_url % 'B')
>>> r.status_code
200

>>> r = c.post(section_url % 'B', {'enrolled_in_another_program': True})
>>> r.status_code
302

>>> p = getLast(Provider)
>>> p.enrolled_in_another_program
True


section C
---------
>>> r = c.get(section_url % 'C')
>>> r.status_code
200

>>> r = c.post(section_url % 'C', {'type_of_entity': 10, 'other_description': 'notes123'})
>>> r.status_code
302

>>> p = getLast(Provider)
>>> p.other_description
u'notes123'


section D
---------
>>> r = c.get(section_url % 'D')
>>> r.status_code
200

>>> r = c.post(section_url % 'D', {'legal_name': 'LName'})
>>> r.status_code
302

>>> p = getLast(Provider)
>>> p.legal_name
u'LName'

section E
---------
>>> r = c.get(section_url % 'E')
>>> r.status_code
200

>>> r.content
'...ARIZONA...'


section F
---------
>>> r = c.get(section_url % 'F')
>>> r.status_code
200


section G
---------
>>> r = c.get(section_url % 'G')
>>> r.status_code
200


section H
---------
>>> r = c.get(section_url % 'H')
>>> r.status_code
200


section I
---------
>>> r = c.get(section_url % 'I')
>>> r.status_code
200


section J
---------
>>> r = c.get(section_url % 'J')
>>> r.status_code
200


section K 
---------
>>> r = c.get(section_url % 'K')
>>> r.status_code
200


section L
---------
>>> r = c.get(section_url % 'L')
>>> r.status_code
200

section M
---------
>>> r = c.get(section_url % 'M')
>>> r.status_code
200


"""
