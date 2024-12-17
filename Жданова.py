#Камень ножницы бумага

import random

while True:
    user = input("Камень, ножницы или бумага (Вводите к, н или б): ")
    list_play = ['к', 'н', 'б']
    if user in list_play:
        rand = random.choice(list_play)
        print(rand)

        if rand == 'к' and user == 'н':
            print("Вы проиграли")
        if rand == 'н' and user == 'б':
            print("Вы проиграли")
        if rand == 'б' and user == 'к':
            print("Вы проиграли")
        if rand == 'н' and user == 'к':
            print("Вы выграли")
        if rand == 'к' and user == 'б':
            print("Вы выграли")
        if rand == 'б' and user == 'н':
            print("Вы выграли")
        if rand == 'н' and user == 'н':
            print("Ничья")
        if rand == 'к' and user == 'к':
            print("Ничья")
        if rand == 'б' and user == 'б':
            print("Ничья")
    #Ошибка
    else:
        print("Прилетели пришельцы и забрали это")
        print("Но игра продолжается")
