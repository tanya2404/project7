# -*- coding: utf-8 -*-
from random import  randint
f_in = open("dictionary.txt", "r", encoding="utf-8")
rus = []
eng = []
for line in f_in:
    a = line.split()
    rus.append(a[0])
    eng.append(a[1])
while 1:
    random_list = []
    i = 0
    while i < 5:
        numer_str = randint(0, len(rus)-1)
        if numer_str not in random_list:
            random_list.append(numer_str)
            i+=1
    vibor = randint(0, len(random_list)-1)

    print('Переведите слово:', eng[random_list[vibor]])

    for i in range(0, len(random_list)):
        print(i+1,')', rus[random_list[i]])
    answer = int(input("Выберете верный номер:"))

    if answer-1 == vibor:
        print("Молодец, держи подарочек")
    else:
        print("Как жаль, кто-то остался без подарка(((")






