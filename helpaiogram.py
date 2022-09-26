import aiogram
from googletrans import Translator


"""изучение объекта string """
print('посмотреть все методы:')
k = 0
translator = Translator()
for i in dir(__builtins__):
    if i.isalpha() and i.endswith('Error') == 0:
        print('-------------------------------------------------------------')
        attribut = getattr(__builtins__, i)
        print(k, i)
        # print(attribut.__doc__)
        # print(type(attribut))
        # print(dir(attribut))
        # print(help(i))
        k += 1


# print('!!!!e------------------------------------------------------------')
# print('zip'.__doc__)
# print('!!!!-------------------------------------------------------------')
# print(dir(zip))
# print('!!!!-------------------------------------------------------------')
# print(help(zip))


with open('test.txt', 'w') as f:
    sys.stdout = f
    # help(list)
    # print(list.__doc__)
    # print(type(list))
    # print(dir(list.reverse))
    # help(list.reverse)
    per = list.pop.__doc__
    print(per)
    result = translator.translate(per, dest='ru')
    print(f'\n({result.text})'.replace('\n\n', '\n'))
    # help(test)
    # print(dir(test))
