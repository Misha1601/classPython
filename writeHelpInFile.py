"""изучение объекта string """
import sys
from bs4 import BeautifulSoup

print('посмотреть справку класса:')

with open('info.txt', 'w') as f:
    k = 0
    sys.stdout = f
    print(dir(BeautifulSoup.text))
    help(BeautifulSoup.text)
# f.close()
