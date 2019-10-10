plus = int(input('Укажите свою выручку: '))
minus = int(input('Укажите свои издержки: '))
navar = plus - minus
if navar > 0:
    print ('Вы отработали с прибылью!')
    rent = navar / plus
    print(f'Рентабельность работы составляет {rent}')
    people = int(input('Сколько человек работает в фирме? '))
    oneplus = rent / people
    print(f'каждый сотрудника вам заработал по {oneplus}')
else:
    print('Вы отработали в убыток')