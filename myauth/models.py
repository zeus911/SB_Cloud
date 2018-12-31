#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File: auth
# @Author: Clare
# @WeChat: h1837866781
# @Datetime:18-11-18 下午2:10
# @Software: PyCharm
# @license : Copyright(C), Nanyang Institute of Technology
#

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, name, email, phone, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            name=name,
            email=UserManager.normalize_email(email),
            phone=phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, phone, password=None):
        user = self.create_user(name, email, phone, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """重写user类"""
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    created_at = models.DateTimeField(verbose_name='注册日期', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone = models.CharField(verbose_name='联系电话', max_length=100, blank=True, null=True)
    is_delete = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ('email',)

    class Meta:
        ordering = ('-created_at',)

    def __unicode__(self):
        return self.name

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
