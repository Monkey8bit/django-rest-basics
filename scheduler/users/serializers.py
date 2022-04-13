from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField,
    EmailField,
    BooleanField,
    ValidationError,
)


from .models import SchedulerUser


class SchedulerUserSerializer(Serializer):
    username = CharField(max_length=120)
    first_name = CharField(max_length=60)
    last_name = CharField(max_length=60)
    email = EmailField(max_length=100)
    test_user = BooleanField(default=False)

    def validate(self, attrs):
        email = attrs.get("email")
        record_exist = SchedulerUser.objects.filter(email=email)

        if record_exist:
            raise ValidationError(f"User with email {email} already exists.")

        return super().validate(attrs)

    def create(self, validated_data):
        user = SchedulerUser(**validated_data)
        user.save()
        return user

    def update(self, instance: SchedulerUser, validated_data):
        for _, data in zip(instance.__dict__, validated_data.items()):
            print(instance.__dict__[data[0]], validated_data[data[0]])
            instance.__dict__[data[0]] = validated_data[data[0]]

        instance.save()
        return instance


class SchedulerUserModelSerializer(ModelSerializer):
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
