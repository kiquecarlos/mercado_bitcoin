# from rest_framework import viewset

from rest_framework import viewsets

from backend.src.helpers.serializers import MmsSerializerResponse

from drf_yasg.utils import swagger_auto_schema

from drf_yasg import openapi

from .actions import index


class MMSController(viewsets.ViewSet):
    from_param_config = openapi.Parameter(
        'from', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=True,
        description="TIMESTAMP FOR START DATE TO SEARCH, MAX DIFF TODAY IS 365 DAYS")

    pair_param_config = openapi.Parameter(
        'pair', in_=openapi.IN_PATH, type=openapi.TYPE_STRING, required=True,
        description="TIMESTAMP FOR START DATE TO SEARCH, MAX DIFF TODAY IS 365 DAYS")

    range_param_config = openapi.Parameter(
        'range', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=True,
        description="MMS RANGE,IS VALUE IN 20 OR 50 OR 200")

    to_param_config = openapi.Parameter(
        'to', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=False,
        description="TIMESTAMP FOR END DATE TO SEARCH, DEFAULT_VALUE=YESTERDAY")

    mms_response = openapi.Response('list MMS', MmsSerializerResponse)

    @swagger_auto_schema(manual_parameters=[
        range_param_config, from_param_config, to_param_config
    ], responses={200: mms_response})
    def index(self, request, pair, *args, **kwargs):
        return index(**locals())
