import scrapy


class PopulationSpider(scrapy.Spider):
    name = "population"
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "ROBOTSTXT_OBEY": False,
    }

    def parse(self, response):
        rows = response.css("table.datatable tbody tr")

        for row in rows:
            cols = row.css("td")

            yield {
                "country": self.get_text(cols[1]),
                "population_2024": self.get_text(cols[2]),
                "yearly_change": self.get_text(cols[3]),
                "net_change": self.get_text(cols[4]),
                "density": self.get_text(cols[5]),
                "land_area": self.get_text(cols[6]),
            }

    def get_text(self, selector):
        text = selector.css("a::text").get() or selector.css("::text").get()
        return text.strip() if text else ""
