print("Я суперпрограмма Python!!!")
print("Привет программист!")

name = input("Ваше имя: ")
print(name, ", добро пожаловать в мир Python!!!")

answer = input ("Давай поработаем? (Y/N))")
if answer == 'Y':
    print("Отлично, давай продолжим")
    print("Выбери один из вариантов:")
    print(" [1] - выведу список файлов")
    print(" [2] - выведу полезную информацию о системе")
    do = int(input ("Введите номер действия"))
    if do == 1:
        pass
    elif do == 2:
        pass
elif answer == 'N':
    print("До свидания.")
else:
    print("Неизвестный ответ")
    