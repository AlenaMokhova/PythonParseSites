# parseSites module

from sitetutortut import SiteTutor
from tabulate import tabulate

if __name__ == '__main__':
    s = SiteTutor()
    items = s.get_new_items()

    if len(items) == 0:
        print('New articles not found')
    else:
        prepared_items = []

        for item in items:
            prepared_items.append([item['title'], item['href']])

        print("New articles:\r")
        print(tabulate(prepared_items, headers=['Article Title', 'Link']))
