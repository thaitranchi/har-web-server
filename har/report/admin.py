from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'creation_time', 'update_time')
    search_fields = ('name', 'user__username')
