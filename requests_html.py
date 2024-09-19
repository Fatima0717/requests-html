import requests
from bs4 import BeautifulSoup

def fetch_page(url: str, user_agent: str = 'Mozilla/5.0') -> str:
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def parse_html(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, 'html.parser')

def main():
    url = 'https://example.org'
    html = fetch_page(url)
    soup = parse_html(html)
    # Process `soup` as needed

if __name__ == '__main__':
    main()
