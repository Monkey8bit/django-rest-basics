from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import SchedulerUserModelViewSet


router = DefaultRouter()
router.register("users", SchedulerUserModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls))
]
