from django.contrib import admin
from . import models
# # Register your models here.
@admin.register(models.ReviewModel)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('post_content', 'user_id',)