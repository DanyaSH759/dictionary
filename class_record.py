
from Class_sql import *

class Record:
    #класс записи и использования словаря

    def take_data(self):
    #функция по вводу данных и проверки на выход из цикла
        self.word = input('введите слово:')
        self.translate = input('введите перевод:')

    def write_date_eng(self):
        a = sql()
        a.connections()
        sqltext = "INSERT INTO words_eng(word, translate) VALUES (?,?);"
        data_tuple = (self.word, self.translate)
        a.curs.execute(sqltext, data_tuple)
        a.db.commit()
        print('данные вставлены в таблицу')
        a.conn_close()














