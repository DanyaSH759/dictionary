from Class_sql import *
import random

class Game():
    #класс реализует игру с указанием корректного перевода слов

    def game_eng(self):
        #Основная функция реализации игры
        A = sql()
        A.connections()  #подключение к базе данных
        SELECT = ('''SELECT word,translate FROM words_eng''') #ввод команды ля SQL
        A.curs.execute(SELECT)#передача в базу данных через курсор

        #вытаскивание данных из базы (кортежи) и добавление в список
        full_cur = A.curs.fetchall()
        date = []
        for full in full_cur:
            date.append(full)
        dict_data = dict(date)

        chose_rand = random.sample(sorted(dict_data.items()), 4)#выбор 4 случайных слов из выборки

        #выделение из кортежа слова и перевода
        x_1, x_2 = [], []
        for x in chose_rand:
            x_1.append(x[0])
            x_2.append(x[1])

        #цикл самой игры
        while True:
            rand_x1 = random.sample(x_2, 4)#перемешивание слов перевода
            print('Для остановки игры введите любую букву')
            print('Данны слова. Необходимо восстановить последовательность перевода:')
            print()
            #вывод слов и перевода
            a = 1
            for x in x_1:
                print(f'{a}){x}')
                a += 1
            print()
            a = 1
            for x in rand_x1:
                print(f'{a}){x}')
                a += 1

            #запись ответа с консоли
            chose = []
            try:
                z1 = int(input('\nВведите номер перевода для слова 1:'))
                chose.append(z1)
                z2 = int(input('Введите номер перевода слова 2:'))
                chose.append(z2)
                z3 = int(input('Введите номер перевода слова 3:'))
                chose.append(z3)
                z4 = int(input('Введите номер перевода слова 4:'))
                chose.append(z4)
            except ValueError:
                break

            #цикл для сверки на схожесть ответа и оригинала списка
            answer = []
            for x in chose:
                answer.append(rand_x1[x - 1])
            if answer == x_2:
                print('\nВаши ответы верны')
                break
            else:
                print('\nОтвет некорректный, вот список правильного перевода')
                print({chose_rand})

        A.conn_close()#закрытие соеденение с базой данных
