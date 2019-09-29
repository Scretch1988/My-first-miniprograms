# coding=utf-8
import os
import sys
import psutil
import shutil
import random

def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print("Файл ", newfile, " был успешно создан")
            return True
        else:
            print("Возникли проблемы копирования")
            return False

def sys_info():
    print("Вот что я знаю о системе:")
    print("Количество процессоров: ", psutil.cpu_count())
    print("Платформа: ", sys.platform)
    print("Кодировка файловой системы: ", sys.getfilesystemencoding())
    print("Текущая директория: ", os.getcwd())
    print("Текущий пользователь: ", os.getlogin())

def duble_files(dirname):
    file_list = os.listdir(dirname)
    i = 0
    while i < len(file_list):
        duplicate_file(file_list[i])
        i += 1
def del_duplicates(dirname):
    file_list = os.listdir(dirname)
    double_count = 0
    for f in file_list:
        fullname = os.path.join(dirname, f)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
            if not os.path.exists(fullname):
                double_count += 1
                print ("Файл", fullname, "был удален")
    return double_count

def random_delete(dirname):
    file_list = os.listdir(dirname)
    if file_list:
        i = random.randrange(0, len(file_list))
        fullname = os.path.join(dirname, file_list[i])
        if os.path.isfile(fullname):
            os.remove(fullname)
            print("файл", fullname, " был случайно удален")

def main():
    print("Я суперпрограмма Python!!!")
    print("Привет программист!")

    name = input("Ваше имя:")
    print(name, ", добро пожаловать в мир Python!!!")

    answer = ''

    while answer != 'q':
        answer = input("Давай поработаем? (Y/N/q)")
        if answer == "Y":
            print("Отлично!")
            print("Я умею:")
            print(" [1] - выведу список файлов")
            print(" [2] - выведу полезную информацию о системе")
            print(" [3] - выведу список процессов")
            print(" [4] - продублирую файлы в текущей директории")
            print(" [5] - продублирую выбранный файл")
            print(" [6] - удалю дубликаты файлов")
            print(" [7] - удалю случайный файл")
            do = int(input("Введите номер действия: "))

            if do == 1:
                print(os.listdir())

            elif do == 2:
                sys_info()

            elif do == 3:
                print(psutil.pids())

            elif do == 4:
                print("=Дублирование файлов в текущей директории=")
                duble_files('.')

            elif do == 5:
                print("=Дублирование указанного файла=")
                filename = input("Укажите имя файла:")
                duplicate_file(filename)

            elif do == 6:
                print("=Удаление дубликатов в директории=")
                dirname = input("Укажите имя директории:")
                count = del_duplicates(dirname)
                print("--Удалено файлов: ", count)

            elif do == 7:
                print("=Удаление случайного файла=")
                dirname = input("Укажите имя директории:")
                random_delete(dirname)

            else:
                pass
        elif answer == 'N':
            print("До свидания!")

        else:
            print("Неизвестный ответ")

if __name__ == "__main__":
    main()
