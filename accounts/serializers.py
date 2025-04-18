from rest_framework.serializers import ModelSerializer
from accounts.models import CustomUser
from rest_framework.serializers import CharField


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ["id", "name","mobile","email","password", "is_staff"]


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)  # hashes the password
        user.save()
        return user