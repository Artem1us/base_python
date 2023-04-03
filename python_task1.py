import sys

def check():
    # введення числа
    num_str = input("Введите число: ")
    try:
        # перетворимо введений рядок на число
        num = float(num_str)
        # перевіряємо, чи є num числом
        if isinstance(num, (int, float)):
            # якщо це число, то функція перевіряє, чи є це число парним. Якщо число парне, то функція повертає рядок "Це парне число"
            if num % 2 == 0:
                return "Це парне число"
            # інакше вона повертає рядок "Це непарне число"
            else:
                return "Це непарне число"
    except ValueError:
        # якщо num не є числом, то функція повертає порожній рядок "".
        print("")
        # перериває виконання програми
        sys.exit()

# викликаємо функцію
print(check())
