import os
import psutil
import sys

print("Я суперпрограмма Python!!!")
print("Привет программист!")

name = input("Ваше имя: ")
print(name, ", добро пожаловать в мир Python!!!")

answer = input ("Давай поработаем? (Y/N)")
if (answer == 'Y' or 'y'):
    print("Отлично, давай продолжим")
    print("Выбери один из вариантов:")
    print(" [1] - выведу список файлов")
    print(" [2] - выведу полезную информацию о системе")
    print(" [3] - выведу список процессов")
    do = int(input("Введите номер действия"))
    if do == 1:
        print(os.listdir())
    elif do == 2:
        print(os.getcwd(), ", информация о текущей дерритктории")
        print(os.name, ", информация о платформе")
        print(sys.getfilesystemencoding(), ", информацию о кодировке файловой системы")
        print(os.getlogin(), ", логин пользователя")
        print(os.cpu_count(), ", колличество ядер процессора")
    elif do == 3:
        print(psutil.pids())
elif (answer == 'N' or 'n'):
    print("До свидания.")
else:
    print("Неизвестный ответ")
    