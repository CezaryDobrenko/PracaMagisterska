from bs4 import BeautifulSoup
import cfscrape
import re
import html_to_json

class Scrapper:
    scrapper: object
    url: str
    selectors: list
    content: str
    soup: list

    def __init__(self, url):
        self.scraper = cfscrape.create_scraper()
        self.url = url
        content = self.__download_content(url)
        self.content = content
        self.soup = BeautifulSoup(content, 'html.parser')

    def __download_content(self, url):
        return self.scraper.get(url).content

    def __remove_html_tags(self, results, replace=''):
        parsed_results = []
        for result in results:
            parsed_result = re.sub(re.compile('<.*?>') , replace, str(result))
            parsed_results.append(parsed_result)
        return parsed_results

    def __parse_to_json(self, results):
        parsed_results = []
        for result in results:
            stringify_result = str(result)
            json_unparsed = str(html_to_json.convert(stringify_result))
            json_parsed = json_unparsed.replace('\'', '\"')
            parsed_results.append(json_parsed)
        return parsed_results

    def scrape_website(self, selector_type, selector_value, is_simplified):
        if selector_type == "tag":
            results = self.soup.findAll(selector_value)
        else:
            results = self.soup.find_all(True,{selector_type:selector_value})
        if is_simplified:
            parsed_results = self.__parse_to_json(results)
        else:
            parsed_results = self.__remove_html_tags(results, replace=" ")
        return parsed_results

    def get_content(self):
        return self.content

    def get_soup(self):
        return self.soup