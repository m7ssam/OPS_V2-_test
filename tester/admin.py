from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(T1)
class T1_import_export(ImportExportModelAdmin,admin.ModelAdmin):
  list_display = T1.displayfields
  search_fields = T1.search_fields

@admin.register(T2)
class T2_import_export(ImportExportModelAdmin,admin.ModelAdmin):
  list_display = T2.displayfields
  search_fields = T2.search_fields
