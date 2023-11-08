from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("project/", include("project.urls")),
    path("report/", include("report.urls")),
    path("users/", include("users.urls")),
    path("manpower/", include("manpower.urls")),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)