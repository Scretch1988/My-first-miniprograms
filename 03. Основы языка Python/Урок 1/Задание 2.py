print('Здравствуйте! Вы обратились в переводчик кучи секунд в нормальное время')
seconds = int(input('Введите любое количество секунд для перевода: '))
hour = int(seconds / 60 // 60)
minutes = int(seconds / 60 % 60)
seconds = int(seconds - hour * 3600 - minutes * 60)
print(f'Это переводится как {hour}:{minutes}:{seconds}')