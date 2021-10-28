from .base_models import MainModel
from django.db import models

from datetime import datetime


from backend.src.choices import PAIR_TYPE


class MMS(MainModel):
    pair = models.CharField('PAIR', max_length=10, choices=PAIR_TYPE)
    timestamp = models.BigIntegerField()
    mms_20 = models.FloatField(null=True, blank=True)
    mms_50 = models.FloatField(null=True, blank=True)
    mms_200 = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{datetime.fromtimestamp(self.timestamp)} | mms20:({self.mms_20}) - mms50:({self.mms_50}) - mms200:({self.mms_200})'
