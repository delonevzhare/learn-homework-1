"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    """
    Замените pass на ваш код
    """
def hello_user():
    while True:
        try:
            answer = input('Как дела?')
            if answer == "Хорошо":
                print('Рад слышать!')
                break
            else:
                print("Чо приуныл, давай еще разок!")
        except KeyboardInterrupt:
            print("Пока!")
            break

hello_user()
    
if __name__ == "__main__":
    hello_user()
