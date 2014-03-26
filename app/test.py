#-*- coding:utf-8 -*-
"""
$Id$
"""
from django.utils import unittest
from django.test.simple import doctest, DocTestRunner, doctestOutputChecker

from tests import test_ft


def load_tests(loader, tests, ignore):
    res = unittest.TestSuite()
    
    res.addTest(doctest.DocTestSuite(test_ft,
                                     checker=doctestOutputChecker,
                                     runner=DocTestRunner,
                                     globs={'getLast': getLast}))
    
    return res
    
def getLast(cls):
    obj = cls.objects.all().order_by('-id')[0]
    return obj
