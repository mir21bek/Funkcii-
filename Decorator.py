import random



'''
Напишите функцию которая генерирует 100 рандомных чисел в диапазоне от 10 до 50 и возвращает их в листе. 
Напишите ДЕКОРАТОР для этой функции 
которая удалит все дубликаты в первой функции и вернёт всё так же лист.
'''
# def decorator(rand):
#     print(rand)
#     def wrapor():
#         s = set(rand())
#         return list(s)
#     return wrapor

# @decorator
# def rand():
#     l = []
#     for i in range(100):
#         l.append(random.randint(10, 50))

#     return l
# print(rand())


'''
Напишите функцию которая спрашивает у пользователя login и password. 
Напишите декоратор который шифрует эти данные и возвращает вам зашифрованные данные. 
(Можете воспользоваться функцией ord и char, можете загуглить...)
'''

# def shifr():
#     a = input("Login:").upper()
#     encrypted = ""
#     for letter in a:
#         if a ==" ":
#             encrypted +=" "
#         else:
#             encrypted+= (chr(ord(letter)+5))
#     print('Ваш зашифрованный логин ',encrypted)
#     b = input("possword:").upper()
#     encrypted = ""
#     for letter in b:
#         if b ==" ":
#             encrypted +=" "
#         else:
#             encrypted+= (chr(ord(letter)+5))
#     print('Ваш зашифрованный пароль ',encrypted)
# shifr()


'''
Создайте 4 функции: add(), substract(), multiply(), divide() которые будут принимать 
по 2 аргумента и возвращать результат: 
сложения, вычитания, умножения и деления.
'''


# def add(x , y):
#     if operation == '+':
#         return x + y                                            
#     else:    
#         return 'Выберите знак сложения!'
# while True:
#     try: 
#         a = float(input('a = '))
#         operation = input('symbol(+) = ')
#         b = float(input('b = '))
#         print (add(a , b))
#     except ValueError:
#         print ('EXIT')
#         break

    
# def substract(x , y):
#     if operation == '-':
#         return x - y                                            
#     else:    
#         return 'Выберите знак вычитания!'
# while True:
#     try: 
#         a = float(input('a = '))
#         operation = input('symbol(-) = ')
#         b = float(input('b = '))
#         print (substract(a , b))
#     except ValueError:
#         print ('EXIT')
#         break


# def multiply(x , y):
#     if operation == '*':
#         return x + y                                            
#     else:    
#         return 'Выберите знак умножение!'
# while True:
#     try: 
#         a = float(input('a = '))
#         operation = input('symbol(*) = ')
#         b = float(input('b = '))
#         print (multiply(a , b))
#     except ValueError:
#         print ('EXIT')
#         break



# def divide(x , y):
#     if operation == '+':
#         return x + y                                            
#     else:    
#         return 'Выберите знак сложение!'
# while True:
#     try: 
#         a = float(input('a = '))
#         operation = input('symbol(/) = ')
#         b = float(input('b = '))
#         print (divide(a , b))
#     except ValueError:
#         print ('EXIT')
#         break