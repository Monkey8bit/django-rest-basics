from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView

from .models import SchedulerUser
from .serializers import SchedulerUserModelSerializer, SchedulerUserSerializer


class UserView(ListAPIView, CreateAPIView):
    serializer_class = SchedulerUserModelSerializer
    queryset = SchedulerUser.objects.all()


class SingleUserView(CreateAPIView, UpdateAPIView, RetrieveAPIView):
    serializer_class = SchedulerUserSerializer
    queryset = SchedulerUser.objects.all()
    lookup_field = "id"
