from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.PostModel)
class PostAdimin(admin.ModelAdmin):
    list_display = ('content', 'user_id', )