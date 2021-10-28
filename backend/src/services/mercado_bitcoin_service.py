from .external_apis import MercadoBitcoinApi


class MercadoBitcoinService:
    @staticmethod
    def __base_get_pair(from_date, to_date, pair='BRLBTC'):
        return MercadoBitcoinApi.get(
            f'{pair}/candle?from={from_date}&to={to_date}&precision=1d')

    @staticmethod
    def get_brlbtc_data(from_date, to_date):
        return MercadoBitcoinService.__base_get_pair(from_date, to_date)

    @staticmethod
    def get_brleth_data(from_date, to_date):
        return MercadoBitcoinService.__base_get_pair(from_date, to_date, 'BRLETH')
