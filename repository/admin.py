from django.contrib import admin
from repository import models
# Register your models here.

admin.site.register(models.Teacher)
admin.site.register(models.Course)
admin.site.register(models.Teacher2Course)
admin.site.register(models.Grade)
admin.site.register(models.Course2Teacher2Grade)
admin.site.register(models.Pic)
