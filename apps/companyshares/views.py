from companyshares.models import Company

from typing import Optional

from rest_framework.request import Request
from rest_framework.response import Response as JsonResponse
from rest_framework.viewsets import ViewSet
from rest_framework import filters , viewsets 
from rest_framework.response import Response

from companyshares.models import Company , Shares
from companyshares.serializers import (
    CompanyCreateSerializer , 
    SharesCreateSerializer ,
    CompanySerializers
)

from abstracts.mixins import (
    ObjectMixin,
    ResponseMixin
)


class CompanyViewSet(ResponseMixin, ObjectMixin,ViewSet):
  
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
    

class SharesViewSet(ResponseMixin, ObjectMixin,viewsets.ModelViewSet):
  
    queryset = Shares.objects.all()
    serializer_class = SharesCreateSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price']

    def list(self, request, *args, **kwargs):
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')

        queryset = self.queryset
        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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
        raise_exception=True)
        shares: Company = serializer.save()

        return self.json_response(f'created. ID: {shares.id}')
     
          
              

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
    


# проверка на наличии акций

# share = Shares.objects.get(pk=id)
# if share.is_available:
#     share.reduce_quantity(id)
#     if not share.is_available:
#         return self.json_response(f'"Акции больше недоступны для покупки.')