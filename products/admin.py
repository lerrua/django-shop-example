#-*- coding:utf-8 -*-

from django.contrib.admin import site

from .models import Product


site.register(Product)
