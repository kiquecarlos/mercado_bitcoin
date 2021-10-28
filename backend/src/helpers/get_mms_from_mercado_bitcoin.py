from backend.src.services import MercadoBitcoinService
from backend.src.helpers import calc_list_mms


def get_mms_from_mercado_bitcoin(start_date, end_date, need_print=False):

    if need_print:
        print('Sincronizando com Mercado Bitcoin (BRLBTC)')

    brlbtc_data = MercadoBitcoinService.get_brlbtc_data(
        from_date=start_date, to_date=end_date)

    if need_print:
        print('OK!\n')
        print('Sincronizando com Mercado Bitcoin (BRLETH)')

    brleth_data = MercadoBitcoinService.get_brleth_data(
        from_date=start_date, to_date=end_date)

    if need_print:
        print('OK!\n')
        print('Calculando MMS BRLBTC')

    brlbtc_mms = calc_list_mms(brlbtc_data.json()['candles'], 'BRLBTC')

    if need_print:
        print('OK!\n')
        print('Calculando MMS BRLETH')

    brleth_mms = calc_list_mms(brleth_data.json()['candles'], 'BRLETH')

    result = brlbtc_mms + brleth_mms

    if need_print:
        print('OK!\n')

    return result
