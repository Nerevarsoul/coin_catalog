# -*- coding: UTF-8  -*-
from __future__ import unicode_literals

from django import template


register = template.Library()


@register.filter
def add_str(arg1, arg2):
    """concatenate arg1 & arg2"""
    return "{}{}".format(arg2, arg1)


@register.filter
def get_attr(obj, attr):
    """call attr for obj"""
    return getattr(obj, attr)


@register.filter
def get_set(obj, attr):
    """call method call for relatedmanager"""
    obj_set = getattr(obj, attr)
    return obj_set.all()


@register.filter
def change_last_letter(word, letter):
    """change last letter for word"""
    return word[:-1].lower() + letter
