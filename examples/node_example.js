// Run autoscout24-germany-scraper on Apify and print the results. npm install apify-client
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const input = {
  "make": "BMW",
  "model": "3er",
  "priceTo": 20000,
  "yearFrom": 2016,
  "sortBy": "newest",
  "maxItems": 20
};
const run = await client.actor('kamerozkan/autoscout24-germany-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
