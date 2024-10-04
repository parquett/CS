def caesar_cipher(text, key, operation):
    # Ensure key is between 1 and 25
    if not (1 <= key <= 25):
        raise ValueError("Key must be between 1 and 25.")

    # Convert text to uppercase and remove spaces
    text = text.upper().replace(" ", "")

    # Define the alphabet without using built-in encodings
    alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    n = len(alphabet)

    # Encryption or decryption
    result = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            if operation == 'encrypt':
                new_index = (index + key) % n
            elif operation == 'decrypt':
                new_index = (index - key) % n
            else:
                raise ValueError("Operation must be 'encrypt' or 'decrypt'.")
            result += alphabet[new_index]
        else:
            # Ignore non-alphabetic characters
            raise ValueError("Only alphabetic characters are allowed.")

    return result


def caesar_cipher_with_permutation(text, key1, key2, operation):
    # Ensure key1 is between 1 and 25
    if not (1 <= key1 <= 25):
        raise ValueError("Key1 must be between 1 and 25.")

    # Validate key2
    key2 = key2.upper()
    if len(key2) < 7 or not key2.isalpha():
        raise ValueError("Key2 must contain only Latin letters and be at least 7 characters long.")

    # Generate the new alphabet with the permutation key
    alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    print(alphabet)
    permutation = []

    # Add characters from key2, ensuring no duplicates
    for char in key2:
        if char not in permutation:
            permutation.append(char)

    # Add remaining characters of the alphabet
    for char in alphabet:
        if char not in permutation:
            permutation.append(char)

    n = len(permutation)

    # Convert text to uppercase and remove spaces
    text = text.upper().replace(" ", "")

    # Encryption or decryption
    result = ""
    for char in text:
        if char in permutation:
            index = permutation.index(char)
            if operation == 'encrypt':
                new_index = (index + key1) % n
            elif operation == 'decrypt':
                new_index = (index - key1) % n
            else:
                raise ValueError("Operation must be 'encrypt' or 'decrypt'.")
            result += permutation[new_index]
        else:
            # Ignore non-alphabetic characters
            raise ValueError("Only alphabetic characters are allowed.")

    print(permutation)
    return result


#task 1.1
operation = input("Enter operation (encrypt/decrypt): ").strip().lower()
key = int(input("Enter key (1-25): "))
message = input("Enter your message: ")

result = caesar_cipher(message, key, operation)
print(f"Result: {result}")

#task 1.2
# operation = input("Enter operation (encrypt/decrypt): ").strip().lower()
# key1 = int(input("Enter key1 (1-25): "))
# key2 = input("Enter key2 (at least 7 characters): ")
# message = input("Enter your message: ")
#
# result = caesar_cipher_with_permutation(message, key1, key2, operation)
# print(f"Result: {result}")

