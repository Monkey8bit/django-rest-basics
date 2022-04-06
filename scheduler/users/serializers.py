from rest_framework.serializers import ModelSerializer

from .models import SchedulerUser


class SchedulerUserSerializer(ModelSerializer):
    class Meta:
        model = SchedulerUser
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_superuser",
            "test_user"
        ]
