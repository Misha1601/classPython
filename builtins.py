"""изучение объекта string """
print('посмотреть все методы:')
k = 0
for en,i in enumerate(dir(__builtins__)):
    if i.isalpha() and i.endswith('Error')==0:
        print('-------------------------------------------------------------------')
        print(k, i)
        k += 1
        #print(i.__doc__)
