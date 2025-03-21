field = [['🌊'] * 5 for _ in range(5)]

import random
ship_row = random.randint(0, 4)
ship_col = random.randint(0, 4)

attempts = 0
while True:
    print("\nПоле боя:")
    for row in field:
        print(' '.join(row))

    try:
        guess_row = int(input("Строка (0-4): "))
        guess_col = int(input("Столбец (0-4): "))
    except ValueError:
        print("Вводите только числа!")
        continue

    if guess_row == ship_row and guess_col == ship_col:
        print("🚢 Корабль потоплен!")
        field[guess_row][guess_col] = '💥'  # Попадание
        break
    elif field[guess_row][guess_col] in ['💥', '❌']:
        print("Сюда уже стреляли!")
    else:
        print("Промах!")
        field[guess_row][guess_col] = '❌'  # Промах
        attempts += 1

    if attempts >= 8:
        print("💀 Закончились патроны! Корабль был в", (ship_row, ship_col))
        break

print("Игра окончена!")
