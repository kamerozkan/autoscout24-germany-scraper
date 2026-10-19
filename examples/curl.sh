#!/usr/bin/env bash
# Run autoscout24-germany-scraper synchronously and get the dataset items back. Needs APIFY_TOKEN.
curl -s -X POST "https://api.apify.com/v2/acts/kamerozkan~autoscout24-germany-scraper/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"make": "BMW", "model": "3er", "priceTo": 20000, "yearFrom": 2016, "sortBy": "newest", "maxItems": 20}'
