def encrypt(msg: str) -> str:
    """Implementation to scramble message using three-rail fence method
    :param msg: string
    :return: the encrypted message
    >>> encrypt('Does this implementation work')
    'Dsh pmti ro iileaowketsmentno'

    >>> encrypt('I love rainy days in Eugene')
    'Io i yiEe vrndsnunleaya  ge'
    """
    # write for loops to establish string iteration for characters to be placed into rails
    rail_1 = ""
    rail_2 = ""
    rail_3 = ""
    char_count = 0
    for characters in msg:
        for i in range(0, len(msg), 3):
            rail_1 = rail_1 + msg[i]

        for i in range(1, len(msg), 3):
            rail_2 = rail_2 + msg[i]

        for i in range(2, len(msg), 3):
            rail_3 = rail_3 + msg[i]

        cipher_text = rail_1 + rail_2 + rail_3
        return cipher_text

def decrypt(msg: str) -> str:
    """to unscramble the message encrypted by three-rail fence method
    :param msg: string
    :return: plain text

    >>> decrypt('Le  ufhu ayraekImo tr')
    'Luke I am your father'

    >>> decrypt('T aeigtgoehwtrsei lreeh  tncd')
    'The weather is getting colder'
    
    """
    rail_1 = ""
    rail_2 = ""
    rail_3 = ""
    third_length = round(len(msg)/3)
    char_count = 0

    for characters in msg:
        rail_1 = msg[0, third_length]
        rail_2 = msg[third_length, 2*(third_length)]
        rail_3 = msg[2*(third_length), len(msg)]
        plain_text = rail_1 + rail_2 + rail_3
        return plain_text
    
def main():
    """Main program to run our encryption/decryption process."""

    which = input('Do you wish to encrypt or decrypt a message [E/D]? ')
    if which.upper() == 'E':
        text = input('Enter a line of text to encrypt: ')
        print("Encrypted text:")
        print(encrypt(text))
    elif which.upper() == 'D':
        text = input('Enter encrypted text to decrypt: ')
        print("Decrypted text:")
        print(decrypt(text))
    else:
        raise ValueError("Invalid option, I only know E and D!")

if __name__ == '__main__':
    main()

