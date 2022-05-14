from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name='token_obtain'),
    path("api/token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("api/users/", include("users.urls", namespace="users")),
    path("api/projects/", include("users_projects.urls", namespace="projects")),
]
