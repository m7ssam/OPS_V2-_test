from django.contrib import admin
from .models import User_id
from import_export.admin import ImportExportModelAdmin

@admin.register(User_id)
class User_id_import_export(ImportExportModelAdmin):
  pass
  