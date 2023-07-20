import scrapy


class ScrapySpiderSpider(scrapy.Spider):
    name = "scrapy_spider"
    allowed_domains = ["store.steampowered.com"]
    url = "https://store.steampowered.com/search/?category1=998&filter=topsellers&ndl=1&page=%s"

    page = 1
    start_urls = [url % page]
    games_found = 0

    def parse(self, response, **kwargs):
        games = response.xpath("//a[contains(@class, 'search_result_row') and not(@style)]")

        for game in games:
            yield scrapy.Request(game.attrib['href'], callback=self.parse_tags)

        if self.games_found < 1000:
            self.page += 1
            yield scrapy.Request(self.url % self.page, callback=self.parse)

    def parse_tags(self, response):
        if self.games_found < 1000:
            yield {
                'Game_Name': response.css("div.apphub_AppName::text").get(),
                'Game_url': response.url,
                'Tags': [tag.css("a::text").get().strip() for tag in response.css("a.app_tag")]
            }
            self.games_found += 1
