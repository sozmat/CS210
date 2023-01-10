
def encrypt(msg: str) -> str:
    """To scramble a message using ROT13 method
    :param msg: the text to be encrypted: string
    :return: the encrypted text

    >>> encrypt('Hello my name is Sydney')
    'Uryyb zl anzr vf Flqarl'

    >>> encrypt('I really hope this works')
    'V ernyyl ubcr guvf jbexf'
    
    """
    alphabet_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz -13."
    key = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm -13."
    cipher_text = ""
    for ch in msg:
        idx = alphabet_string.find(ch)
        cipher_text = cipher_text + key[idx]
    return cipher_text

def decrypt(msg: str) -> str:
    """To unscramble a message encrypted by ROT13 method
    :param msg: the encrypted text
    :return: the original message, string  

    >>> decrypt('Vg vf nyzbfg jrrx svir')
    'It is almost week five'

    >>> decrypt('Vg vf fcbbxl frnfba')
    'It is spooky season'

    """
    alphabet_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ."
    key = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm ."
    plain_text = ""
    for ch in msg:
        idx = key.find(ch)
        plain_text = plain_text + alphabet_string[idx]
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
