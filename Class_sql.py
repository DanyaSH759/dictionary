import sqlite3

class sql:
#Класс по взаимодействию с базой данных

    def connections(self):
        #функция открытия соеденения с базой данных

        self.db = sqlite3.connect('data.db') #соеденение с базой
        self.curs = self.db.cursor() #создание курсора для работы с базой

    def conn_close(self):
        #закрытие подкючения к базе и закрытие программы
        self.db.close()

    def show_eng_words(self):

        self.connections()
        cur = self.curs.execute('''SELECT * FROM words_eng''')
        full_cur = cur.fetchall()
        for full in full_cur:
            print(full)


