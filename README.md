# AutoScout24 Scraper - Gebrauchtwagen Scraper & Price Monitor

Used car listings from autoscout24.de by make, model, price, mileage, year, fuel and ZIP radius: price, first registration, km, power, dealer and location in one row. New-listings and price-drop monitor for dealers, car buyers and market analysts.

**[Run it on Apify Store](https://apify.com/kamerozkan/autoscout24-germany-scraper)**: no servers, no proxies to manage, results as JSON, CSV or Excel, or straight into your app through the API.

## Why use it

- Runs in the cloud on [Apify](https://apify.com/kamerozkan/autoscout24-germany-scraper); start it from the browser, the API, a schedule, or tools like Make, n8n and Zapier.
- Pay only for results. The current price and plan discounts are always on the [Store page](https://apify.com/kamerozkan/autoscout24-germany-scraper).
- Cap the cost of any run with the maximum cost per run setting.

## Quick start

1. Open the [Actor page](https://apify.com/kamerozkan/autoscout24-germany-scraper) and click **Try for free**.
2. Paste an input like the one below and click **Start**.
3. Download the dataset or read it over the API.

```json
{
  "make": "BMW",
  "model": "3er",
  "priceTo": 20000,
  "yearFrom": 2016,
  "sortBy": "newest",
  "maxItems": 20
}
```

## Use it from code

Python ([examples/python_example.py](examples/python_example.py)), Node.js ([examples/node_example.js](examples/node_example.js)) and cURL ([examples/curl.sh](examples/curl.sh)) examples are in the `examples` folder. All of them need an [Apify API token](https://console.apify.com/settings/integrations).

## Sample output

Real rows from a recent run, with any contact details masked. Full sample: [sample-output.json](sample-output.json).

```json
[
  {
    "listingId": "01e7aa49-a869-4a71-b521-120124985aa9",
    "url": "https://www.autoscout24.de/angebote/volkswagen-golf-vii-variant-comfortline-bmt-92kw-shz-pdc-benzin-weiss-cat_ma74gr100101ge7va132mt420tr562-01e7aa49-a869-4a71-b521-120124985aa9",
    "title": "Volkswagen Golf Variant 1.4 TSI",
    "make": "Volkswagen",
    "model": "Golf",
    "modelGroup": "Golf",
    "variant": "Variant",
    "version": "VII Variant Comfortline BMT 92kW-SHZ-PDC",
    "highlights": null,
    "offerType": "used",
    "price": 8900,
    "currency": "EUR",
    "priceLabel": "good-price",
    "previousListedPrice": null,
    "mileageKm": 118031,
    "firstRegistration": "2016-03",
    "fuel": "Benzin",
    "transmission": "Schaltgetriebe",
    "powerKw": 92,
    "powerHp": 125,
    "engineCcm": 1395,
    "fuelConsumption": "5,3 l/100 km (komb.)",
    "co2Emission": "123 g/km (komb.)",
    "isDamaged": false,
    "availableNow": true,
    "imageCount": 18,
    "images": [
      "https://prod.pictures.autoscout24.net/listing-images/01e7aa49-a869-4a71-b521-120124985aa9_e95b0e65-d3b8-4eda-98dd-e12071112b15.jpg/250x188.webp",
      "https://prod.pictures.autoscout24.net/listing-images/01e7aa49-a869-4a71-b521-120124985aa9_8b053484-e292-4cc9-9759-5376bacebf97.jpg/250x188.webp",
      "https://prod.pictures.autoscout24.net/listing-images/01e7aa49-a869-4a71-b521-120124985aa9_cbb22c7a-eeb2-4733-972c-005826febb18.jpg/250x188.webp",
      "https://prod.pictures.autoscout24.net/listing-images/01e7aa49-a869-4a71-b521-120124985aa9_e81f0108-9082-45d7-826a-3080621b8db3.jpg/250x188.webp",
      "https://prod.pictures.autoscout24.net/listing-images/01e7aa49-a869-4a71-b521-120124985aa9_f9bb5771-35c2-456d-a79f-2ae95bf6cf4e.jpg/250x188.webp",
      "https://prod.pictures.autoscout24.net/listing-images/01e7aa49-a869-4a71-b521-120124985aa9_39d49b0a-753c-4be9-8d91-45a7d9dcb39a.jpg/250x188.webp",
      "https://prod.pictures.autoscout24.net/listing-images/01e7aa49-a869-4a71-b521-120124985aa9_609231c2-db50-4254-a4af-97ae0790bfd3.jpg/250x188.webp",
      "https://prod.pictures.autoscout24.net/listing-images/01e7aa49-a869-4a71-b521-120124985aa9_0aa55761-25bb-41f2-b954-5b284064a414.jpg/250x188.webp",
      "https://prod.pictures.autoscout24.net/listing-images/01e7aa49-a869-4a71-b521-120124985aa9_463c44eb-3237-4da0-9861-8906f06740ff.jpg/250x188.webp",
      "https://prod.pictures.autoscout24.net/listing-images/01e7aa49-a869-4a71-b521-120124985aa9_a3939e3f-2222-484b-8799-afb15fbb2995.jpg/250x188.webp",
      "https://prod.pictures.autoscout24.net/listing-images/01e7aa49-a869-4a71-b521-120124985aa9_cf867ec6-d33b-41e3-bca2-17a8517fe71a.jpg/250x188.webp",
      "https://prod.pictures.autoscout24.net/listing-images/01e7aa49-a869-4a71-b521-120124985aa9_c56537fe-86b9-4fec-bdd8-b61992d8d5ba.jpg/250x188.webp",
      "https://prod.pictures.autoscout24.net/listing-images/01e7aa49-a869-4a71-b521-120124985aa9_e4d1e243-211f-486d-b353-fdcd94986dc1.jpg/250x188.webp",
      "https://prod.pictures.autoscou
```

## Support

Found a problem or need a field? Open an issue on the [Actor's Issues tab](https://apify.com/kamerozkan/autoscout24-germany-scraper/issues) and include your run link.

---
This repository holds usage examples and sample data. The Actor itself runs on Apify.
