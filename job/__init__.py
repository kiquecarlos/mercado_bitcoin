from datetime import datetime
from time import sleep

from backend.src.utils import get_start_moment_day, sub_days

from backend.src.helpers import get_mms_from_mercado_bitcoin

from backend.src.models import MMS

from backend.src.services import sender_email

from backend.src.configs.email import STRING_CONNECTION, PORT, EMAIL, PASSWORD, EMAIL_TO_SEND


def insert_new_date_mercadobitcoin():
    try:
        today_timestamp = int(datetime.today().timestamp())

        start_moment_today = int(get_start_moment_day(today_timestamp))

        if(MMS.objects.filter(timestamp=start_moment_today).count() == 0):
            from_date = int(sub_days(start_moment_today, 200))

            calc_data = get_mms_from_mercado_bitcoin(
                from_date-1, start_moment_today+1)

            data_to_save = list(filter(lambda x: x['timestamp'] == start_moment_today,
                                       calc_data))
            MMS.objects.bulk_create([
                MMS(pair=mms['pair'],
                    timestamp=mms['timestamp'],
                    mms_20=mms['mms_20'],
                    mms_50=mms['mms_50'],
                    mms_200=mms['mms_200']
                    ) for mms in (data_to_save)
            ])
    except:
        pass


def check_less_day():
    if STRING_CONNECTION != '' and PORT != '' and EMAIL != '' and PASSWORD != '' and EMAIL_TO_SEND != '':
        today_timestamp = int(datetime.today().timestamp())

        start_moment_today = int(get_start_moment_day(today_timestamp))

        last_year_day = int(sub_days(start_moment_today, 365))

        if MMS.objects.filter(timestamp__gte=last_year_day).filter(
                timestamp__lte=start_moment_today).count() < 730:
            sender_email(EMAIL_TO_SEND, "Falha na Sincronização MMS",
                         "Ocorreu uma Falha de Sincronização no MMS favor verificar base de dados dos últimos dias")


print('START JOB')
while(True):
    insert_new_date_mercadobitcoin()

    check_less_day()

    WAITING_MINUTES = 60
    sleep(WAITING_MINUTES*60)
