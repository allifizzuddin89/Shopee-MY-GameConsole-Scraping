import scrapy
from scrapy import Request
import json

# Using proxy if unsuccessful and errors
# Register here at https://www.scraperapi.com/?fp_ref=allif-izzuddin-bin-abdullah73
# You might want to choose free account
# Scraperapi proxy API key details will be provided after the registration
# Follow the instruction in the scraperapi website to setup the proxy
# Paste the API key inside creds.py module

# Uncomment below if using proxy
# from creds import API
# from scraper_api import ScraperAPIClient
# client = ScraperAPIClient(API)

# Logging
import logging
from scrapy.utils.log import configure_logging
logging.getLogger('__main__').setLevel(logging.DEBUG)
configure_logging(install_root_handler = False) 
logging.basicConfig(
    filename="logfile.txt", 
    format='%(asctime)s - %(levelname)s - %(message)s', 
    filemode='w',
    level = logging.ERROR,
)
class MainSpider(scrapy.Spider):
    name = 'main'
    # allowed_domains = ['x']
    # start_urls = ['http://x/']

    # Scraping for game console list in Shopee MY

    url = 'https://shopee.com.my/api/v4/recommend/recommend?bundle=category_landing_page&cat_level=1&catid=11001085&limit=60&offset={}'

    headers = {
        "authority": "shopee.com.my",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,ms;q=0.8,id;q=0.7",
        "cache-control": "no-cache",
        "dnt": "1",
        "if-none-match-": "55b03-35710a471c4d1149d44cfd8efa937505",
        "pragma": "no-cache",
        "referer": "https://shopee.com.my/Gaming-Consoles-cat.11001085?page=0&sortBy=pop",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42",
        "x-api-source": "pc",
        "x-requested-with": "XMLHttpRequest",
        "x-shopee-language": "en"
    }

    cookies = {
        "__LOCALE__null": "MY",
        "SPC_F": "4yyr34qq4wkEtFKE27R94tgqsNmVmnnq",
        "REC_T_ID": "9f294993-0cc6-11ed-8673-2cea7fac73f8",
        "csrftoken": "nRBsmNywRWNAZgiei8oVB4xQwekE9Omg",
        "_QPWSDCXHZQA": "2ced2645-2481-4b1f-d766-dcd4b322c478",
        "language": "en",
        "G_ENABLED_IDPS": "google",
        "SPC_CLIENTID": "NHl5cjM0cXE0d2tFeffyooousrejdajx",
        "SPC_U": "-",
        "SPC_EC": "-",
        "SPC_IA": "-1",
        "SPC_T_ID": "yjf6vJdvbU3Bv/hF5exVuEkBiLWhaJIVstqrsTqWc9XJX95VcI+N6MmEgk2wqCrnQZxzjajrLuwJsd9S6wbAnFhKD10FxfEkz+Ig0oKoRT4=",
        "SPC_T_IV": "/KtcL1So3DLzbIrubiEcJQ==",
        "SPC_R_T_ID": "yjf6vJdvbU3Bv/hF5exVuEkBiLWhaJIVstqrsTqWc9XJX95VcI+N6MmEgk2wqCrnQZxzjajrLuwJsd9S6wbAnFhKD10FxfEkz+Ig0oKoRT4=",
        "SPC_R_T_IV": "/KtcL1So3DLzbIrubiEcJQ==",
        "SPC_SI": "lr1sYwAAAAB6S0F3SENpMUyamAAAAAAAY3llTHY0MnU=",
        "shopee_webUnique_ccd": "uBeydK%2BHx1X0EFo6Ey%2FESw%3D%3D%7CwReKgl%2BzrwaHNae%2FFwFtNjYrgOH7x0%2B5QxLub51Yh8yRct4U9QmOhrukyCbgD%2Bkpe8ueGbXXT%2BBS3%2FGfcOUiGX0JCYEZ8tWEQuY4%7C1K8Lorz7W75cgk5m%7C06%7C3",
        "ds": "347008a18c18952762149899d359d9eb"
    }

    def start_requests(self):
        # Comment below if using proxy

        url = 'https://shopee.com.my/api/v4/recommend/recommend?bundle=category_landing_page&cat_level=1&catid=11001085&limit=60&offset=0'
        request = Request(
        url=url,
        method='GET',
        dont_filter=True,
        headers=self.headers,
        cookies=self.cookies
        # callback=self.parse
        )
        yield request

        # for i in range(0,481):
        #     request = Request(
        #     url=self.url.format(i),
        #     method='GET',
        #     dont_filter=True,
        #     headers=self.headers,
        #     cookies=self.cookies
        #     # callback=self.parse
        #     )
        #     print('\n')
        #     print('i')
        #     print('\n')
        #     i+=60
        #     yield request
        # Uncomment below if using proxy
        # for i in range(1,61):
        #     yield scrapy.Request(client.scrapyGet(url=self.url.format(i), headers=self.headers), dont_filter=True)

    def parse(self, response):
        # Load json
        # inspect_response(response, self)
        raw_data = response.body
        data = json.loads(raw_data)
        total = data['data']['sections'][0]['data']['item']
        print('\n\n Has {} DATA\n\n'.format(len(total)))
        for i in range(len(total)):                    
            try:
                item = {
                    'Name': data['data']['sections'][0]['data']['item'][i]['name'],
                    'Price Max (RM)': data['data']['sections'][0]['data']['item'][i]['price_max'],
                    'Price Min (RM)': data['data']['sections'][0]['data']['item'][i]['price_min'],
                    'Rating': data['data']['sections'][0]['data']['item'][i]['item_rating']['rating_star'],
                    'Sold Unit' : data['data']['sections'][0]['data']['item'][i]['historical_sold'],
                    'Shop Name': data['data']['sections'][0]['data']['item'][i]['shop_name'],
                    'Status Stock' : data['data']['sections'][0]['data']['item'][i]['stock']
                }
                yield item
            except Exception:
                item = {
                    'Name': data['data']['sections'][0]['data']['item'][i]['name'],
                    'Price Max (RM)': data['data']['sections'][0]['data']['item'][i]['price_max'],
                    'Price Min (RM)': data['data']['sections'][0]['data']['item'][i]['price_min'],
                    'Rating': data['data']['sections'][0]['data']['item'][i]['item_rating']['rating_star'],
                    'Sold Unit' : data['data']['sections'][0]['data']['item'][i]['historical_sold'],
                    'Shop Name': data['data']['sections'][0]['data']['item'][i]['shop_name'],
                    'Status Stock' : 'Sold Out',
                }
                yield item