from django.contrib import admin
from .models import Lecture, College, Department, LectureComment
# Register your models here.

admin.site.register(Lecture)
admin.site.register(LectureComment)
admin.site.register(College)
admin.site.register(Department)