import siteparser
import datetime
from configfile import ConfigFile


class SiteTutor:
    """ Class for parsing and getting data from site tutortut.com"""

    URL = 'https://tutortut.com/articles'
    ru_to_eng_months = {
        'января': '01',
        'февраля': '02',
        'марта': '03',
        'апреля': '04',
        'мая': '05',
        'июня': '06',
        'июля': '07',
        'августа': '08',
        'сентября': '09',
        'октября': '10',
        'ноября': '11',
        'декабря': '12'
    }

    def __init__(self):
        self.config = ConfigFile()
        self.config_checkpoint = self.config.get_site_checkpoint(self.URL)
        pass

    def get_new_items(self):
        """ Return list of new articles """

        list_of_new_articles = []

        html = siteparser.SiteParser(self.URL)
        html.parse()

        elements = html.findtag('div', {
            'class': 'articles_list_item'
        })

        for item in elements:
            date_html = item.find('div', {'class': 'articles_list_item-date'})
            date = self.datestring_to_datetime(date_html.text)
            datetime_checkpoint = ''

            if self.config_checkpoint is not None:
                datetime_checkpoint = date.strptime(self.config_checkpoint, '%d.%m.%Y')

            if self.config_checkpoint is None or date > datetime_checkpoint:
                title = item.find('a', {'class': 'articles_list_item-title'})

                list_of_new_articles.append({
                    'title': title.text,
                    'href': title.get('href')
                })

        self.set_checkpoint(elements[0])

        return list_of_new_articles

    def set_checkpoint(self, item):
        """ Set checkpoint in config """
        date_html = item.find('div', {'class': 'articles_list_item-date'})
        date = self.datestring_to_datetime(date_html.text)
        self.config.write_checkpoint(self.URL, date.strftime('%d.%m.%Y'))

    def datestring_to_datetime(self, ru):
        """ Date in string format to datetime """
        s = ru.split(' ')
        month = self.ru_to_eng_months[s[1]]
        return datetime.datetime(int(s[2]), int(month), int(s[0]))
