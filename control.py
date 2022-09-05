from class_record import *

from Game import *

def record_words():
    # Функция для создания цикла записи слов в словарь
    try:
        rec = Record()
        rec.take_data()
        rec.write_date_eng()
    except AttributeError:
        pass

def show():
    #функция отображает все слова записанные в таблице
    sh = sql()
    sh.show_eng_words()

def start_game():
    #функция по запуску игры
    game = Game()
    game.game_eng()

if __name__ == '__main__':
    print('Словарь активирован')
    print('Список доступных комманд:'
          '\nВведите \'start\' что бы начать запись слов в словарь'
          '\nВведите / что бы повторно активировать режим записи слов'
          '\nВведите \'show\' что просмотреть все слова в словаре'
          '\nВведите \'exit\' что бы закрыть словарь'
          '\nВведите \'game\' что бы начать игру')

    while True:
        console = [{'script': 'd.py'}]
        z = input('>>>')
        if z == 'start' or z == '/':
            record_words()

        elif z == 'show':
            show()

        elif z == 'game':
            start_game()

        elif z == 'exit':
            break


