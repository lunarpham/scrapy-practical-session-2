# World Population Crawler

A simple Scrapy spider that crawls population data from [Worldometers](https://www.worldometers.info/world-population/population-by-country/) and saves it to a CSV file.

## How to run

```bash
scrapy crawl population -o population.csv
```

The output file `population.csv` will be created in the project root.

## Data collected

| Column | Description |
|--------|-------------|
| country | Country/dependency name |
| population_2024 | Population (2024) |
| yearly_change | Yearly change (%) |
| net_change | Net change |
| density | Density (P/Km²) |
| land_area | Land area (Km²) |
