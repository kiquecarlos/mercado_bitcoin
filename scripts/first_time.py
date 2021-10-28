from tqdm import tqdm
from datetime import datetime, timedelta

from backend.src.models import MMS
from backend.src.services import MercadoBitcoinService
from backend.src.utils import destruct_dict

from backend.src.helpers import get_mms_from_mercado_bitcoin


def main():

    def data_save(data):
        MMS.objects.bulk_create([
            MMS(pair=mms['pair'],
                timestamp=mms['timestamp'],
                mms_20=mms['mms_20'],
                mms_50=mms['mms_50'],
                mms_200=mms['mms_200']
                ) for mms in tqdm(data)
        ])

    def factory_date_to_request():
        DIFF_DAYS = 365

        today_date = datetime.today()

        diff_date = today_date - timedelta(days=DIFF_DAYS)

        return {
            'start_date': int(diff_date.timestamp()),
            'end_date': int(today_date.timestamp())
        }

    date_to_request = factory_date_to_request()

    start_date, end_date = destruct_dict(
        date_to_request, 'start_date', 'end_date')

    dict_to_db = get_mms_from_mercado_bitcoin(start_date, end_date, True)

    print('Salvando Dados no Banco')
    data_save(dict_to_db)


main()
