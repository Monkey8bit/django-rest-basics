from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path("api/users/", include("users.urls", namespace="users")),
    path("api/projects/", include("users_projects.urls", namespace="projects")),
]
