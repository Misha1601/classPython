"""импортируемый модуль, дает перевод оригинальной справки"""
# import sys
# import googletrans
from googletrans import Translator
import json


def helpm():
    "общий перевод"
    # tr = 'Mikä on nimesi'
    tr = str(help(str.isalnum))
    translator = Translator()
    result = translator.translate(tr, dest='ru')
    print(f'\n({result.text})'.replace('\n\n', '\n'))


def dirm(modul):
    "просмотр количества методов"
    pass


def docm(molul):
    "описание метода или класса"
    pass


def main():
    print('hello')
    tr = help(str.isalnum)
    print(json.dumps(help(str.isalnum), sort_keys=True, indent=4))
    for i in tr:
        print(i)
        print('-----------------------------------------------')


if __name__ == '__main__':
    main()
    # helpm()
