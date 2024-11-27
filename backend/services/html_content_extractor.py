from bs4 import BeautifulSoup
import requests

class HtmlContentExtractor:
    @staticmethod
    def extract(url: str):
        
        response = requests.get(url)
        
        if response.status_code == 200:
            html_content = response.text
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            exit()

        soup = BeautifulSoup(html_content, "html.parser")
        table = soup.find("table", {"class": "h3", "border": "0"})
        
        return table.find_all("tr")