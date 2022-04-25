import rest_framework.serializers as serializers

from .models import Project, Note
from users.models import SchedulerUser


class ProjectModelSerializer(serializers.ModelSerializer):
    users = serializers.SlugRelatedField(
        many=True,
        queryset=SchedulerUser.objects.all(),
        slug_field="username",
        read_only=False
    )

    class Meta:
        model = Project
        fields = "__all__"


class NoteModelSerializer(serializers.ModelSerializer):
    # project = serializers.SlugRelatedField(slug_field="name", read_only=True)
    user_created = serializers.SlugRelatedField(queryset=SchedulerUser.objects.all(), slug_field="username")

    class Meta:
        model = Note
        fields = "__all__"

