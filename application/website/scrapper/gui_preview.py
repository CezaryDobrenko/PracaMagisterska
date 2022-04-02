from bs4 import BeautifulSoup
import cfscrape

class GUIPreview:
    scraper = cfscrape.create_scraper()

    def get_preview(url):
        content = Scrapper.scraper.get(url).content
        soup = BeautifulSoup(content, 'html.parser')
        parsed_soup = Scrapper.parse_soup(soup)
        return parsed_soup

    def parse_soup(soup):
        unwanted_tags = ["script", "style", "link", "head", "svg"]
        unwanted_elements = [('a', 'href'), (None, 'style')]
        for tag in unwanted_tags:
            soup = Scrapper._extract_unwanted_item(soup, tag)
        for element in unwanted_elements:
            marker, attribute = element
            soup = Scrapper._delete_unwanted_attribute(soup, marker, attribute)
        soup = Scrapper._add_attribute_to_element(soup, "img", "style", "max-height: 40%; max-width: 40%;")
        return soup

    def _extract_unwanted_item(soup, item_type):
        for s in soup.select(item_type):
            s.extract()
        return soup

    def _delete_unwanted_attribute(soup, marker, attribute):
        for s in soup.find_all(marker):
            del s[attribute]
        return soup

    def _add_attribute_to_element(soup, marker, attribute, value):
        for s in soup.find_all(marker):
            s[attribute] = value
        return soup