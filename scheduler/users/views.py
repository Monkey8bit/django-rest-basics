from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination

from .models import SchedulerUser
from .serializers import SchedulerUserModelSerializer, SchedulerUserSerializer


class UserLimitOffset(LimitOffsetPagination):
    default_limit = 100


class UserView(ListAPIView):
    serializer_class = SchedulerUserModelSerializer
    queryset = SchedulerUser.objects.all()
    # pagination_class = UserLimitOffset


class SingleUserView(UpdateAPIView, RetrieveAPIView):
    serializer_class = SchedulerUserSerializer
    queryset = SchedulerUser.objects.all()
    lookup_field = "id"
