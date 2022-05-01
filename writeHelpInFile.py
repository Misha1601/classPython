"""изучение объекта string """
import sys

print('посмотреть справку класса:')
f = open('info.txt', 'w')
k = 0
sys.stdout = f
help(list)
f.close()
