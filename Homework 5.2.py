a = int(input("Введите переменную а: "))
b = int(input("Введите переменную b: "))
c = int(input("Введите переменную c: "))

if a > b and a > c:
    max = a
elif b > a and b > c:
    max = b
else:
    max = c

print(max)
