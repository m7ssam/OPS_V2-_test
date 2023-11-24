from django.contrib import admin
from .models import Department, Governorate
from import_export.admin import ImportExportModelAdmin

admin.site.site_header = "OPS"
admin.site.site_title = "OPS"
admin.site.index_title = "OPS Admin Control panal"

@admin.register(Department)
class Department_import_export(ImportExportModelAdmin):
  pass


@admin.register(Governorate)
class Governorate_import_export(ImportExportModelAdmin,admin.ModelAdmin):
  list_display = Governorate.displayfields
  pass