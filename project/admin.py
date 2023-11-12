from django.contrib import admin
from .models import Name
from import_export.admin import ImportExportModelAdmin

@admin.register(Name)
class Name_import_export(ImportExportModelAdmin):
  pass
  



