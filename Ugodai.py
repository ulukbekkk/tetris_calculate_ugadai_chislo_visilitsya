from random import randint
print('------------------------------------------------')
name = input('Введите имя, дружище: \n')
print('________________________________________________')

while True:
    random_number = randint(1,51)
    game = input(f'\nХотите играть {name}? Ответитьте (Да) или (Нет): \n')
    if game == 'нет' or game == "Нет":
        print('Игра закончилась...')
        break
    elif game == 'Да' or game == 'да':
        print('Начинаем играть ( ͡° ͜ʖ ͡°)')
    elif game != 'Да' or game != 'да' or game != 'Нет' or game != 'нет':
        print('---------------------------------------------------------')
        print(f'\nВы ввели {game} --> вместо (Да) ил (Нет) ☹')
        print('_________________________________________________________')
        continue
    print(f'У вас всего 5 попыток ۞')
    n = 5
    while n > 0:
        number = int(input('Введите число от 1 до 50 : '))
        if number < random_number:
            print('----------------------------------')
            print(f'Надо было выбрать число по больше')
            print(f'У вас осталось {n-1} попыток')
            if n == 1:
                print('Вы проиграли ¯\_(ツ)_/¯')
                print(f'Загаданное число было {random_number}')
            n -=1
            continue
        elif number > random_number:
            print('----------------------------------')
            print(f'Надо было выбрать число по меньше ')
            print(f'У вас осталось {n-1} попыток')
            if n == 1:
                print('Вы проиграли ¯\_(ツ)_/¯')
                print(f'Загаданное число было {random_number}')
            n -= 1
            continue
        elif number == random_number:
            print(f'Вы угодали число, поздравляю вас {name} загаданное число было --> {random_number}')
            break
        elif number.isalpha():
            print(f'Вы ввели букву')
            print(f'У вас осталось {n-1} попыток')
            continue
        
     

