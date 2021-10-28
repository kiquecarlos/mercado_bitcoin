import cloudscraper

from backend.src.configs import base_url_mercado_bitcoin


class MercadoBitcoinApi:

    @staticmethod
    def get(url, **kwargs):
        scraper = cloudscraper.create_scraper()
        return scraper.get(f'{base_url_mercado_bitcoin}/{url}', **kwargs)
