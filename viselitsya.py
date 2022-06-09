from random import choice
start = """
----|
|
|
|
|
__________
"""
a1 = """
----|
|   0
|   |
|
|
__________
"""
a2 = """
----|
|   0
|  /|
|
|
__________
"""
a3 = r"""
----|
|   0
|  /|\
|
|
__________
"""
a4 = r"""
----|
|   0
|  /|\
|  / 
|
__________
"""
a5 = r"""
----|
|   0
|  /|\
|  / \
|
__________
"""

list_ = [a1,a2,a3,a4,a5]

words = ['книга','ноутбук',"доска", "ручка", "каска", "мяч", "весна", "кофе","машина","муравей"]
some_word = choice(words)
znak = '*' * len(some_word)
print(znak)

count = 5
correct_letters = []
print('Угодайте буквы, которые стоят вместо "*"')
print(start)
ind = -1

while count > 0:
    count -= 1
    print(f'У вас осталось {count+1} попыток')

    bukva = input("Введите одну букву: ")
    res = ""

    if bukva in some_word:
        correct_letters.append(bukva)
        
        for x in some_word:
            if x in correct_letters:
                res += x
            else:
                res += "*"
        print(res)
        count += 1
        if res == some_word:
            print('ПОБЕДА, вы все угодали')
            break
    else:
        ind += 1
        print(list_[ind])
    if count == 0:
        print('Вы проиграли')
    