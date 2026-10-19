"""Run autoscout24-germany-scraper on Apify and print the results. pip install apify-client"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = {'make': 'BMW',
 'model': '3er',
 'priceTo': 20000,
 'yearFrom': 2016,
 'sortBy': 'newest',
 'maxItems': 20}
run = client.actor("kamerozkan/autoscout24-germany-scraper").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
