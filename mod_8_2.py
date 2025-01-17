def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
    return (result, incorrect_data)

def calculate_average(numbers):
    try:
        sum_of_numbers, number_of_incorrect_data = personal_sum(numbers)
        average = sum_of_numbers / (len(numbers) - number_of_incorrect_data)
        return average
    except TypeError:
        return 'В numbers записан некорректный тип данных'
    except ZeroDivisionError:
        return 0

try:
    print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
    print(f'Результат 5: {calculate_average()}')  #
except TypeError as exc:
    print(f'Что-то пошло не так: {exc}')

print('Программа отработала полностью!')