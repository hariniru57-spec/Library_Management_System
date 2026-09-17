from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("library_app.urls")),
    path("api/", include("library_app.api_urls")),
]
