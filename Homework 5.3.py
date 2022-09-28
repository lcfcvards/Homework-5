number = int(input("Введите число: "))

if not 100 <= number <= 999:
    print("Ошибка")
    exit()

first_number = number % 10
second_number = number % 100 // 10
third_number = number // 100

final_number = first_number * 100 + second_number * 10 + third_number

print(final_number)
