def encrypt(msg: str) -> str:
    """Scrambles a message using odd-even transposition cipher
        parameter: the message user would like to encrypt, type str
        return: the encrypted message, type str

        >>> encrypt('1234')
        '2413'

        >>> encrypt('Hello my name is Sydney')
        'el ynm sSdeHlom aei yny'

        """
    even_chars = ""
    odd_chars = ""
    char_count = 0
    for ch in msg:
        if char_count % 2 == 0:
            even_chars = even_chars + ch
        else:
            odd_chars = odd_chars + ch
        char_count = char_count + 1
    cipher_text = odd_chars + even_chars
    return cipher_text 

def decrypt(msg: str) -> str:
    """Decrypts a message encrypted that used an odd-even transposition cipher
        parameter: the message user would like to decrypt, type str
        return: the original message, type str

        >>> decrypt('102')
        '012'

        >>> decrypt(' aeadgnmdRxsIhv  o ae oa')
        'I have a dog named Roxas'
        
        """
    half_length = len(msg) // 2
    even_chars = msg[half_length:]
    odd_chars = msg[:half_length]
    plain_text = ""

    for i in range(half_length):
        plain_text = plain_text + even_chars[i]
        plain_text = plain_text + odd_chars[i]

    if len(odd_chars) < len(even_chars):            # in case there is uneven amount of letters in string
        plain_text = plain_text + even_chars[-1]

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


