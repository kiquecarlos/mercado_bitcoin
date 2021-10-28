from rest_framework import serializers

from backend.src.models import MMS


class MmsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MMS
        fields = ["timestamp", "mms_20", "mms_50", "mms_200"]
