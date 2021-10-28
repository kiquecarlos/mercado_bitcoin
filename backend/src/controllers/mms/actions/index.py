from rest_framework.response import Response

from rest_framework import status

from datetime import datetime, timedelta, time

from backend.src.models import MMS

from backend.src.helpers.serializers import MmsSerializer

from backend.src.utils import get_end_moment_day, get_start_moment_day, get_yesterday_timestamp


def index(self, request, pair, *args, **kwargs):

    def is_long_time(timestamp):
        LONG_TIME_DAYS = 365

        initial_date = datetime.combine(
            datetime.fromtimestamp(timestamp),
            time.min
        )

        today_date = datetime.combine(datetime.now(), time.max)

        min_time = today_date - timedelta(days=LONG_TIME_DAYS)

        return initial_date < min_time

    if not pair in ['BRLBTC', 'BRLETH']:
        return Response({
            "status": 404,
            "msg": "Not Found"
        }, status=status.HTTP_404_NOT_FOUND)

    if not request.query_params.get('from'):
        return Response({
            "status": 400,
            "msg": "Field (from) Is Invalid"
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        if is_long_time(int(request.query_params.get('from'))):
            return Response({
                "status": 400,
                "msg": "You Select a old date in (from)"
            }, status=status.HTTP_400_BAD_REQUEST)

    if not request.query_params.get('range') or not int(request.query_params.get('range')) in [20, 50, 200]:
        return Response({
            "status": 400,
            "msg": "Field (range) Is Invalid, possible values is 20,50,200"
        }, status=status.HTTP_400_BAD_REQUEST)

    if request.query_params.get('to') and not str(request.query_params.get('to')).isdigit():
        return Response({
            "status": 400,
            "msg": "Field (to) Is Invalid"
        }, status=status.HTTP_400_BAD_REQUEST)

    to_date = request.query_params.get('to')

    from_date = get_start_moment_day(int(request.query_params.get('from')))

    if not to_date:
        to_date = get_yesterday_timestamp()
    else:
        to_date = get_end_moment_day(int(to_date))

    queryset = MMS.objects.filter(
        timestamp__lte=to_date).filter(timestamp__gte=from_date).filter(pair=pair)

    serializer = MmsSerializer(queryset, many=True)

    dict_range = {
        '20': 'mms_20',
        '50': 'mms_50',
        '200': 'mms_200'
    }

    range_selected = dict_range[str(request.query_params.get('range'))]

    result = list(map(lambda x: {
        'timestamp': x['timestamp'],
        'mms': x[range_selected]
    }, serializer.data))

    return Response(result)
