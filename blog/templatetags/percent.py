__author__ = 'zhangxun'
# -*- coding:utf-8 -*-

from django import template

register = template.Library()
def percent(value):
    return value + "%"

register.filter(percent)