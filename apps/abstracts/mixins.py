# Python
from typing import Any

# DRF
from rest_framework.response import Response as JsonResponse
from rest_framework.validators import ValidationError

# Django
from django.db.models import query

class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ObjectMixin:
    
    def get_object(self, queryset, obj_id):
        obj = queryset.filter(id=obj_id).first()
        if obj is None:
            raise CustomError(f'Object {obj_id} not found')
        return obj

class ResponseMixin:

    STATUS_SUCCESS = 'Success'
    STATUS_WARNING = 'Warning'
    STATUS_ERROR = 'Error'
    STATUSES = (STATUS_SUCCESS, STATUS_WARNING, STATUS_ERROR)

    def json_response(self, data, status=STATUS_SUCCESS):
        if status not in self.STATUSES:
            raise CustomError('FATAL ERROR')

        response_data = {
            'status': status,
            'results': data
        }

        return JsonResponse(response_data)