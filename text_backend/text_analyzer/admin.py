from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ComparisonData


class ComparisonDataAdmin(admin.ModelAdmin):
    list_display = ('label', 'text1', 'text2')


admin.site.register(ComparisonData, ComparisonDataAdmin)
