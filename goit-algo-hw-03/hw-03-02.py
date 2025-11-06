import random


def get_numbers_ticket(min, max, quantity):
    """
    Генерація унікальних випадкових чисел для лотерей
    """

    numbers_set = set()

    # min - мінімальне можливе число у наборі (не менше 1).
    check1 = min >= 1
    # max - максимальне можливе число у наборі (не більше 1000).
    check2 = max <= 1000
    check3 = min < max
    check4 = (max - min) >= quantity

    if all([check1, check2, check3, check4]):
        # починаємо генерацію випадкових чисел за умови що min і max задані корректно
        # відповідно до умови домашнього завдання

        while len(numbers_set) < quantity:
            # Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
            # в циклі врахована імовірність генерації випадкового числа, яке вже є в сеті
            # цикл буде виконуватися до моменту коли розмір сету буде рівний quantity
            numbers_set.add(random.randint(min, max))
            # print(numbers_set)
    else:
        print("умови не виконуються")

    """
    Функція повертає список випадково вибраних, відсортованих чисел. 
    Числа в наборі не повинні повторюватися. 
    Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.
    """
    return list(sorted(numbers_set))


if __name__ == "__main__":
    print("Домашнє завдання №2")
    print("Набір унікальних випадкових чисел для лотерей\n")

    print(f"{get_numbers_ticket(1, 49, 6)=}\n")
    print(f"{get_numbers_ticket(1, 36, 5)=}\n")
    print(f"{get_numbers_ticket(-1, 36, 5)=}\n")
    print(f"{get_numbers_ticket(1, 36000, 5)=}\n")
    print(f"{get_numbers_ticket(100, 36, 5)=}\n")

    print(f"{get_numbers_ticket(-10, 10, 5)=}\n")
    print(f"{get_numbers_ticket(1000, 1200, 10)=}\n")
    print(f"{get_numbers_ticket(10, 4, 5)=}\n")
    print(f"{get_numbers_ticket(10, 14, 6)=}\n")
    print(f"{get_numbers_ticket(10, 14, 5)=}\n")
    print(f"{get_numbers_ticket(10, 14, 4)=}\n")
