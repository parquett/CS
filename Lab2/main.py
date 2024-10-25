from collections import Counter

ENGLISH_FREQUENCY_TABLE = {
    'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0, 'N': 6.7, 'S': 6.3, 'H': 6.1, 'R': 6.0, 'D': 4.3,
    'L': 4.0, 'C': 2.8, 'U': 2.8, 'M': 2.4, 'W': 2.4, 'F': 2.2, 'G': 2.0, 'Y': 2.0, 'P': 1.9, 'B': 1.5,
    'V': 1.0, 'K': 0.8, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07
}


def display_english_frequency_table():
    print("\nStandard English Frequency Table")
    print("| Character | Frequency (%) |")
    print("|-----------|----------------|")
    for char, freq in sorted(ENGLISH_FREQUENCY_TABLE.items(), key=lambda item: item[1], reverse=True):
        print(f"|     {char}     |      {freq:.2f}      |")
    print()


def frequency_analysis(text):
    text = text.replace(" ", "")
    frequencies = Counter(text)
    total_chars = sum(frequencies.values())
    sorted_frequencies = {char: (count / total_chars) * 100 for char, count in
                          sorted(frequencies.items(), key=lambda item: item[1], reverse=True)}
    return sorted_frequencies


def apply_substitutions(text, substitutions):
    decrypted_text = text
    for original, substitute in substitutions.items():
        decrypted_text = decrypted_text.replace(original, substitute)
    return decrypted_text


def main():
    print("Welcome to the Frequency Analysis Decryption Program")
    encrypted_text = input("Enter the encrypted text:\n").upper()

    # Perform frequency analysis
    freq_analysis = frequency_analysis(encrypted_text)
    print("\nCharacter Frequency Analysis")
    print("| Character | Frequency (%) |")
    print("|-----------|----------------|")
    for char, freq in freq_analysis.items():
        print(f"|     {char}     |      {freq:.2f}      |")

    display_english_frequency_table()

    substitutions = {}

    while True:
        print("\nCurrent Decrypted Text:")
        print(apply_substitutions(encrypted_text, substitutions))

        choice = input("\nWould you like to substitute a character? (y/n): ").strip().lower()
        if choice != 'y':
            break

        original_char = input("Enter the encrypted character to replace: ").strip().upper()
        if original_char not in freq_analysis:
            print("Character not found in the text. Try again.")
            continue

        substitute_char = input(f"Enter the character to replace '{original_char}' with: ").strip().upper()

        substitutions[original_char] = substitute_char

    print("\nFinal Decrypted Text:")
    print(apply_substitutions(encrypted_text, substitutions))
    print("\nThank you for using the program!")


if __name__ == "__main__":
    main()
