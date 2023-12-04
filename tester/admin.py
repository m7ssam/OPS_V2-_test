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

@admin.register(Post)
class Post_import_export(ImportExportModelAdmin,admin.ModelAdmin):
  list_display = Post.displayfields
  search_fields = Post.search_fields


@admin.register(ExampleModel)
class ExampleModel_import_export(ImportExportModelAdmin,admin.ModelAdmin):
  list_display = ExampleModel.displayfields
  search_fields = ExampleModel.search_fields
