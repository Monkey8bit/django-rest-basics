from rest_framework.viewsets import ModelViewSet

from .models import SchedulerUser
from .serializers import SchedulerUserSerializer


class SchedulerUserModelViewSet(ModelViewSet):
    serializer_class = SchedulerUserSerializer
    queryset = SchedulerUser.objects.all()
