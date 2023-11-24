from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Mp_list)
class Mp_list_import_export(ImportExportModelAdmin,admin.ModelAdmin):
  list_display = Mp_list.displayfields
  search_fields = Mp_list.search_fields
  list_filter = Mp_list.list_filter
  pass

@admin.register(Title_list)
class Title_list_import_export(ImportExportModelAdmin):
  pass

@admin.register(Job_type)
class Job_type_import_export(ImportExportModelAdmin):
  pass

@admin.register(Contract)
class Contract_import_export(ImportExportModelAdmin):
  pass


# @admin.register(Code)
# class Code_import_export(ImportExportModelAdmin):
#   pass

@admin.register(Code)
class Code_import_export(ImportExportModelAdmin,admin.ModelAdmin):
  list_display = Code.displayfields
  search_fields = Code.search_fields
  list_filter = Code.list_filter
  pass



@admin.register(Mp_Location)
class Mp_Location_import_export(ImportExportModelAdmin):
  pass


@admin.register(Mp_history)
class Mp_history_import_export(ImportExportModelAdmin):
  pass
  