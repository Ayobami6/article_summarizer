import requests
from bs4 import BeautifulSoup


# Scraping class
class ScrapingService:
    """ Scraping Service class
    """

    def scrape_content(self, url: str) -> str:
        """ Scrapes the body content of a blog article from
        the url
        """
        # Use request to get the html content from the url
        response = requests.get(url)
        # Use bs to parse the html content
        soup = BeautifulSoup(response.content, "html.parser")
        # find the body content
        body = soup.find("body")
        # Remove footer content
        footer = body.find("footer")
        if footer:
            footer.extract()
        content = body.get_text().strip()
        content = content.replace("\n", " ")
        content = content.replace("\t", " ")
        content = content.replace("\r", " ")
        content = content.replace("  ", " ")
        # content_length = len(content)
        return content


# new_service = ScrapingService()

# content = new_service.scrape_content(
#     "https://www.devart.com/dbforge/mysql/how-to-install-mysql-on-ubuntu/")

# print(content)
# # print(content_length)
