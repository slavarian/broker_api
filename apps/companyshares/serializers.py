from rest_framework import serializers
from companyshares.models import Company , Shares

class CompanyCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = [
            'name',
            'date_create'
        ]

class SharesCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shares
        fields = [
            'name',
            'price',
            'company'
        ]

class CompanySerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()