from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("username", "password")

    def create(self, validated_data):
        # Fix issue with password in plain text (create == save() in django)
        user = super().create(validated_data)
        user.set_password(validated_data['password'])  # encrypt password
        user.save()
        return user

    def validate(self, data):
        return super().validate(data)

    # remove password from response
    def to_representation(self, instance):
        result = super().to_representation(instance)
        result.pop('password')
        return result
