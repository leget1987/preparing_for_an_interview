# 2. Написать программу, которая запрашивает у пользователя ввод числа.
# На введенное число она отвечает сообщением, целое оно или дробное.
# Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
# Если они совпадают, программа должна возвращать значение True, иначе False.

def check_number(number):
    try:
        result = float(number)
        if int(number) == result:
            print(f'{number} - это целое число')
        else:
            print(f'{number} - это дробное число')
            whole, fractional = number.split('.')
            if whole == fractional:
                return True
            else:
                return False
    except ValueError:
        print('Ввели не число')


user_number = input('Введите число: ')
print(check_number(user_number))
