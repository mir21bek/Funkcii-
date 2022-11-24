'''                     23 - Ноябрь
                        Анонимные Функции.
'''

# names_ages = ['Rustam 19', 'Kairat 26', 'Erlan 18']
# names_ages.sort(key=lambda x: x.split(' ')[-1])
#
#
# l = ['One', 'two', 'tree', '123']
# def find_o(s):
#     for i in s:
#         if 'o' in i and i.islower():
#             return i
#
# def find_oo(s):
#     return 'o' in s
# p = map(find_oo, l)
# # print(list(p))
# for i in p:
#     print(i)
#
# print(list(filter(str.isalpha, l)))
#


# def find_oo(s):
#     return 'o' in s
# p = filter(find_oo, l)  # ['One', 'two', 'tree', '123']
# p = filter((lambda x: 'o' in x), l)  # ['One', 'two', 'tree', '123']
# for i in p:
#     print(i)

# nums = [1,2,3,4,5]
# def sum_nums(n):
#     res = 0
#     for number in n:
#         res += number
#     print(res)
# sum_nums(nums)

# def sum_nums(first, second):
#     return first + second
# from functools import reduce
# res = reduce(sum_nums, nums)
# print(res)

# def get_word_from_user(message):
#     return message

# def write_data_in_file(data):
#     with open('menu.txt', 'w') as f:
#         f.write(data)

# def main():
#     write_data_in_file(get_word_from_user(input()))

# if __name__ == 'main':
#     main()


'''
Написать Функцию которая принимает предложение как аргумент, 
считает количество букв и возвращает
 сколько символов он ввёл. НЕ ИСПОЛЬЗОВАТЬ функцию len()
'''


# def sentens_lenth(sentens):
#     count = 0
#     for i in sentens:
#         count += 1
#     print(count)
# sentens_lenth(input())

'''
Напишите функцию которая принимает 2 Dictionary и добавляет 
втрорую Dictionary к первой.
'''


# d1 = {1: 2, 2: 3}
# d2 = {4: 5, 5: 6}
# print((lambda x: d1) (d1.update(d2)))

'''
Напишите функцию которая спрашивает у вас чтобы вы хотели заказать покушать и выпить. 
А затем записывает это всё в файл на рабочем столе menu.txt
'''
# def get_word_in_user(message):
#     return message
# def write_data_in_file(data):
#     with open('menu.txt', 'w') as f:
#         f.write(data)

# write_data_in_file(input('Что хотите заказать? '))

# '''
# Создайте функцию которая принимает слово и создаёт файл 
# с таким именем в той же директории, где был запущен Ваш .py файл.
# '''
# def create_file(file_name):

#     with open(f'{file_name}', 'w') as file:
#         pass


# create_file(input('Введите название файла'))


'''
Создайте 2 функции где одна функция вложена в другую. 
Главная функция должна выводить на экран текст: "Я главная функция". 
А вложенная функция должна выводить на экран: "Я вложенная функция."
'''

# def main_f(get_main):
#     def second_f():
#         print(f'Я вложенная функция.\n{get_main}')
#     second_f()
# main_f(get_main='Я главная функция!')


'''
Создайте функцию которая принмает тип данных dictionary, но возвращает два 
Tuple в одном из них 
все ключи, в другом только значения
'''

# a = {'name': 'Mirbek', 'age': '27', 'surname': 'Suranchiev'}          
# def dictionary_tuple(a):        
#     print(tuple(a))             
#     print(tuple(a.values()))    
# dictionary_tuple(a)


'''
Напишите программу которая определяет ПРОСТЫЕ ЧИСЛА. 
Простое число - это число которое делится только на себя и на 1.
'''
# def prostoe():
#     a = int(input("Введите число: "))
#     k = 0
#     for i in range(2, a // 2+1):
#         if (a % i == 0):
#             k = k+1
#     if (k <= 0):
#         print("Число простое")
#     else:
#         print("Число не является простым")
# prostoe()