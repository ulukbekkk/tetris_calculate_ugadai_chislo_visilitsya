i = 0
while i <= 0:
    number = input('Введите первое число: ')
    numbers = input('Введите второе число: ')
    # float_ = float(number)
    # float_s = float(numbers)
    if number.isalpha() or numbers.isalpha() :#or float_.isfloat() and float_s.isfloat():
        print('Вы ввели не цифру, Введите повторно')
        
    else:
        number1 = float(number)
        number2 = float(numbers)
        vvod_znak = input('Выберите операцию из следующих (+) (-) (*) (/) (%) (**) (//) : ')
        znak_list = ['+', '-', '*', '/', '%', '**', '//']
        if vvod_znak in znak_list[0]:
            print(number1 + number2)

        elif vvod_znak in znak_list[1]:
            print(number1 - number2)

        elif vvod_znak in znak_list[2]:
            print(number1 * number2)

        elif vvod_znak in znak_list[3]:
            print(number1  / number2)

        elif vvod_znak in znak_list[4]:
            print(number1 % number2)

        elif vvod_znak in znak_list[5]:
            print(number1 ** number2)

        elif vvod_znak in znak_list[6]:
            print(number1 // number2)

        else:
            print('Вы ввели не существуюший знак')
        i = 1

