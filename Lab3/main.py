def create_playfair_matrix(key):
    alphabet = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    key = "".join(sorted(set(key), key=key.index))  # Удаляем повторяющиеся символы
    matrix = []
    used = set(key)

    # Добавляем символы ключа в матрицу
    for letter in key:
        matrix.append(letter)

    # Заполняем оставшиеся ячейки матрицы алфавитом
    for letter in alphabet:
        if letter not in used:
            matrix.append(letter)
            used.add(letter)

    return [matrix[i:i + 6] for i in range(0, len(matrix), 6)]

def find_position(matrix, letter):
    for row in range(6):
        for col in range(6):
            if matrix[row][col] == letter:
                return row, col
    return None

def prepare_text(text, fill_char='Ь'):
    text = text.upper().replace(" ", "")  # Удаляем пробелы
    text = "".join([char for char in text if 'А' <= char <= 'Я'])

    # Добавляем символ-заполнитель для одинаковых букв в паре
    prepared_text = ""
    i = 0
    while i < len(text):
        prepared_text += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            prepared_text += fill_char
        elif i + 1 < len(text):
            prepared_text += text[i + 1]
        i += 2

    # Если длина нечетная, добавляем символ-заполнитель
    if len(prepared_text) % 2 != 0:
        prepared_text += fill_char

    return prepared_text

def encrypt_pair(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return matrix[row1][(col1 + 1) % 6] + matrix[row2][(col2 + 1) % 6]
    elif col1 == col2:
        return matrix[(row1 + 1) % 6][col1] + matrix[(row2 + 1) % 6][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_pair(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return matrix[row1][(col1 - 1) % 6] + matrix[row2][(col2 - 1) % 6]
    elif col1 == col2:
        return matrix[(row1 - 1) % 6][col1] + matrix[(row2 - 1) % 6][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def encrypt_text(matrix, text):
    text = prepare_text(text)
    encrypted = ""
    for i in range(0, len(text), 2):
        encrypted += encrypt_pair(matrix, text[i], text[i + 1])
    return encrypted

def decrypt_text(matrix, text):
    decrypted = ""
    for i in range(0, len(text), 2):
        decrypted += decrypt_pair(matrix, text[i], text[i + 1])
    return decrypted

def main():
    print("Алгоритм Плейфера для русского языка")
    operation = input("Выберите операцию (шифр / дешифр): ").strip().lower()

    while True:
        key = input("Введите ключ (не менее 7 символов): ").strip().upper()
        if len(key) >= 7 and all('А' <= char <= 'Я' for char in key):
            break
        print("Ключ должен содержать только буквы русского алфавита и быть не менее 7 символов.")

    matrix = create_playfair_matrix(key)
    print("Матрица Плейфера:")
    for row in matrix:
        print(" ".join(row))

    if operation == "шифр":
        message = input("Введите сообщение для шифрования: ").strip().upper()
        encrypted_message = encrypt_text(matrix, message)
        print(f"Зашифрованное сообщение: {encrypted_message}")
    elif operation == "дешифр":
        cryptogram = input("Введите криптограмму для дешифрования: ").strip().upper()
        decrypted_message = decrypt_text(matrix, cryptogram)
        print(f"Расшифрованное сообщение: {decrypted_message}")
    else:
        print("Неверная операция")

if __name__ == "__main__":
    main()
