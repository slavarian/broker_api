from companyshares.models import Company

from typing import Optional

from rest_framework.request import Request
from rest_framework.response import Response as JsonResponse
from rest_framework.viewsets import ViewSet


from companyshares.models import Company , Shares
from companyshares.serializers import (
    CompanyCreateSerializer , 
    SharesCreateSerializer ,
    CompanySerializers
)


class CompanyViewSet(ViewSet):
  
    queryset = Company.objects.all()

    def list(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> JsonResponse:
        serializer: CompanySerializers = \
            CompanySerializers(
                instance=self.queryset,
                many=True
            )
        return self.json_response(serializer.data)

    def retrieve(
        self,
        request: Request,
        pk: Optional[int] = None
    ) -> JsonResponse:
        company = self.get_object(self.queryset, pk)
        serializer: CompanyCreateSerializer = \
            CompanyCreateSerializer(instance=company)

        return self.json_response(serializer.data)

    def create(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> JsonResponse:
        serializer: CompanyCreateSerializer = \
            CompanyCreateSerializer(
                data=request.data
            )
        serializer.is_valid(
            raise_exception=True
        )
        company: Company = serializer.save()

        return self.json_response(f'{company.name} is created. ID: {company.id}')

    def update(
        self,
        request: Request,
        pk: str
    ) -> JsonResponse:
        company = self.get_object(self.queryset, pk)
        serializer: CompanyCreateSerializer = \
            CompanyCreateSerializer(
                instance=company,
                data=request.data
            )
        if not serializer.is_valid():
            return self.json_response(
                f'{company.name} wasn\'t updated', 'Warning'
            )
        serializer.save()
        return self.json_response(f'{company.name} was updated')
    

class SharesViewSet(ViewSet):
  
    queryset = Shares.objects.all()

    def list(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> JsonResponse:
        serializer: SharesCreateSerializer = \
            SharesCreateSerializer(
                instance=self.queryset,
                many=True
            )
        return self.json_response(serializer.data)

    def retrieve(
        self,
        request: Request,
        pk: Optional[int] = None
    ) -> JsonResponse:
        shares = self.get_object(self.queryset, pk)
        serializer: SharesCreateSerializer = \
            SharesCreateSerializer(instance=shares)

        return self.json_response(serializer.data)

    def create(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> JsonResponse:
        serializer: SharesCreateSerializer = \
            SharesCreateSerializer(
                data=request.data
            )
        serializer.is_valid(
            raise_exception=True
        )
        shares: Company = serializer.save()

        return self.json_response(f'{shares.name} is created. ID: {shares.id}')

    def update(
        self,
        request: Request,
        pk: str
    ) -> JsonResponse:
        shares = self.get_object(self.queryset, pk)
        serializer: SharesCreateSerializer = \
            SharesCreateSerializer(
                instance=shares,
                data=request.data
            )
        if not serializer.is_valid():
            return self.json_response(
                f'{shares.name} wasn\'t updated', 'Warning'
            )
        serializer.save()
        return self.json_response(f'{shares.name} was updated')