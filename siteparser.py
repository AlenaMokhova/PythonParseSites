import requests
from bs4 import BeautifulSoup

class SiteParser:
    """ Class for parsing html from site """
    def __init__(self, siteUrl=''):
        self.url = siteUrl
        self.soup = ''

    def parse(self):
        if self.url == '':
            return

        html_text = requests.get(self.url).text
        self.soup = BeautifulSoup(html_text, 'html.parser')

        return

    def findtag(self, tag, attrs):
        return self.soup.find_all(tag, attrs)



