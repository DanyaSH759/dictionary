
from Class_sql import *

class Record:
    #класс записи и использования словаря

    def take_data(self):
    #функция по вводу данных и проверка на остановку запист слов
        print('Для остановки записи введите \'stop\'')

        w1 = input('введите слово:')
        if w1 == 'stop':
            pass
        else:
            self.word = w1

        w2 = input('введите перевод:')
        if w2 == 'stop':
            pass
        else:
            self.translate = w2


    def write_date_eng(self):
        #устанавливает соеденение с бд
        a = sql()
        a.connections()
        sqltext = "INSERT INTO words_eng(word, translate) VALUES (?,?);"
        data_tuple = (self.word, self.translate)
        a.curs.execute(sqltext, data_tuple) #загружает полученные слова в указанные выше колонки
        a.db.commit() #передача данных (закрытие транзакции)
        print('данные вставлены в таблицу')
        a.conn_close() #закрытие соеденения














