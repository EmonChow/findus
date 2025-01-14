"""start_project URL Configuration."""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from . import views

admin.site.site_header = "BacBon Limited"
admin.site.index_title = "Welcome to CheckME"

urlpatterns = [
    path("", views.index),
    path("admin/", admin.site.urls),
    # Authentication module
    path("api/v1/user/", include("authentication.urls.user_urls")),
   
    path("api/v1/permission/", include("authentication.urls.permission_urls")),
    path("api/v1/role/", include("authentication.urls.role_urls")),
    # path('accounts/', include('allauth.urls')),
    # YOUR PATTERNS
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
