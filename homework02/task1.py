# На вход подается число n. Написать скрипт в любой парадигме,
# который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.

def print_table(n):
    print('\n'.join([f'1 * {num} = {num}' for num in range(1, n + 1)]))


print_table(10)
