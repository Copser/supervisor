# blog/admin.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Post, ApplyFormModel

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    """TODO: register model into admin with a small customization for the model, we are including
    some fieldsets, so we will separate jobs categories from jobs title, description and created_at field
    return: TODO
    """
    fieldsets = [
        ('Job General Information',
         {'fields': ['title', 'description', 'tag', 'created_at'],
           'classes': ['collapse']}),
    ]


@admin.register(ApplyFormModel)
class ApplyAdmin(admin.ModelAdmin):
    """TODO: register apply_to form
    return: TODO
    """
    pass


admin.site.register(Post, PostAdmin)
