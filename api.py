from woocommerce import API
import pprint

wcapi = API(
    url="http://localhost:8888/demosite",
    consumer_key="ck_da962047c4fca89c37e8228586c58e019ee8d9da",
    consumer_secret="cs_f3f479e364e09ebc61bd9942ae5f7f3c7b4eaa1a",
    version="wc/v3"
)

r = wcapi.get("products")
pprint.pprint(r.json())