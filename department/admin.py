from django.contrib import admin
from .models import Teacher, Course, Audience


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'audience', 'full_time')
    search_fields = ('name', 'position', 'audience__number')
    list_filter = ('audience', 'full_time')
    list_editable = ('full_time',)
    ordering = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Audience)
class AudienceAdmin(admin.ModelAdmin):
    list_display = ('number',)
    search_fields = ('number',)
    ordering = ('number',)
