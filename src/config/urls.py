from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # standard django admin panel
    path("admin/", admin.site.urls),
    # our referral system endpoints
    path("api/v1/", include("referral_system.urls")),
    # djoser 
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("auth/", include("djoser.urls.jwt")),
]