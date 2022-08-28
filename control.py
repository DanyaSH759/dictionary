from class_record import *
from Class_sql import *

def record_words():
    # Функция для создания цикла записи слов словарь
    rec = Record()
    rec.take_data()
    rec.write_date_eng()

def show():
    sh = sql()
    sh.show_eng_words()

if __name__ == '__main__':
    print('Словарь активирован')
    print('Список доступных комманд:'
          '\nВведите \'start\' что бы начать запись слов в словарь'
          '\nВведите / что бы повторно активировать режим записи слов'
          '\nВведите \'show\' что просмотреть все слова в словаре'
          '\nВведите \'ex_all\' что бы закрыть словарь')

    while True:
        z = input('>>>')
        if z == 'start' or z == '/':
            record_words()

        elif z == 'show':
            show()

        elif z == 'exit' or z == 'ex_all':
            break


