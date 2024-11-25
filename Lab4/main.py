import random

# DES PC-1 Table
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

# DES shift schedule
SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def permute(block, table):
    """Permute the block according to the given table."""
    return [block[i - 1] for i in table]

def left_shift(block, shifts):
    """Perform left circular shift on the block."""
    return block[shifts:] + block[:shifts]

def generate_random_key():
    """Generate a random 64-bit key."""
    return [random.randint(0, 1) for _ in range(64)]


def des_key_schedule(K_plus, round_i):
    """Compute Ci and Di for the given round index."""
    print("\nШаг 1: Применение PC-1 к ключу K+")
    K = permute(K_plus, PC1)
    print("Результат PC-1 (56 бит):", ''.join(map(str, K)))

    # Step 2: Split K into C0 and D0
    C0, D0 = K[:28], K[28:]
    print("\nШаг 2: Разделение на C0 и D0")
    print("C0 (28 бит):", ''.join(map(str, C0)))
    print("D0 (28 бит):", ''.join(map(str, D0)))

    # Step 3: Apply left circular shifts up to the i-th round
    for i in range(round_i):
        shift = SHIFTS[i]
        C0 = left_shift(C0, shift)
        D0 = left_shift(D0, shift)
        print(f"\nШаг {i + 3}: Циклический сдвиг для раунда {i + 1}")
        print(f"Сдвиг: {shift}")
        print("Ci:", ''.join(map(str, C0)))
        print("Di:", ''.join(map(str, D0)))

    return C0, D0

if __name__ == "__main__":
    print("DES Калькулятор Ci и Di")

    K_plus = generate_random_key()
    print("Случайный 64-битный ключ K+:", ''.join(map(str, K_plus)))

    round_i = int(input("Введите номер раунда (1-16): ").strip())
    if not (1 <= round_i <= 16):
        print("Неверный номер раунда. Завершение программы.")
        exit()

    Ci, Di = des_key_schedule(K_plus, round_i)

    print("\nИтог:")
    print(f"Ci (раунд {round_i}):", ''.join(map(str, Ci)))
    print(f"Di (раунд {round_i}):", ''.join(map(str, Di)))
