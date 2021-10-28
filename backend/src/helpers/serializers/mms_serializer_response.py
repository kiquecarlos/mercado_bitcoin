from rest_framework import serializers

from backend.src.models import MMS


class MmsSerializerResponse(serializers.ModelSerializer):
    mms = serializers.FloatField()

    class Meta:
        model = MMS
        fields = ["timestamp", 'mms']
