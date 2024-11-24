from bs4 import BeautifulSoup
import requests

class HtmlContentExtractor:
    URL = "https://plan.ue.wroc.pl/l_pozycjaplanu1.php?se=56&gr=135/1"
    
    @staticmethod
    def extract():
        
        response = requests.get(HtmlContentExtractor.URL)
        
        if response.status_code == 200:
            html_content = response.text
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            exit()

        soup = BeautifulSoup(html_content, "html.parser")
        table = soup.find("table", {"class": "h3", "border": "0"})
        
        return table.find_all("tr")