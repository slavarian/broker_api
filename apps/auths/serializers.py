from rest_framework import serializers
from auths.models import MyUser


class MyUserSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()
    # password = serializers.CharField()


    def create(self, validated_data):
        return MyUser.objects.create(**validated_data)