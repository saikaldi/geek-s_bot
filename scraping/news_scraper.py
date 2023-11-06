from parsel import Selector
import requests

class NewsScraper:
    URL = 'https://www.prnewswire.com/news-releases/health-latest-news/health-latest-news-list/'
    LINK_XPATH = '//div[@class="row newsCards"]/div/a/@href'
    PLUS_URL = 'https://www.prnewswire.com'
    DATE_XPATH = '//h3/small/text()'
    def parse_data(self):
        html = requests.get(url=self.URL).text
        tree = Selector(text=html)
        links = tree.xpath(self.LINK_XPATH).extract()
        dates = tree.xpath(self.DATE_XPATH).extract()
        # print(links)
        for link in links:
            print(self.PLUS_URL+link)

        return links[:5]



if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.parse_data()

