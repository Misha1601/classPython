import sys
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


# class test():
#     def __init__(self, an, b, ver):
#         self.an = an
#         self.b = b
#         self.ver = ver
#         print(an + b + ver)

#     def sm(self, an, b, ver):
#         print(an + b + ver)
#         return an + b + ver

#     def hi(self, k):
#         print(str(k))

#     def sr(self, no):
#         if no > 5:
#             print('число больше 5')
#         else:
#             print('число меньше 5')

# print('!!!!-------------------------------------------------------------')
# print('zip'.__doc__)
# print('!!!!-------------------------------------------------------------')
# print(dir(zip))
# print('!!!!-------------------------------------------------------------')
# print(help(zip))


# ty = test(1, 1, 1)
# ty.sm(1, 1, 1)
# numb = int(input("введите число: "))
# ty.sr(numb)

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
