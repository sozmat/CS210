
from typing import Callable
import p4_1
import p4_2
import p4_3


def encrypt(msg: str, func: Callable[[str], str]) -> str:
    """Will implement the chosen encryption function with the inputed text
    parameter: the message to be encrypted and the function to carry out decryption
    return: the implementation of chosen encryption function

    >>> encrypt("Hello my fellow friend", p4_1.encrypt)
    'el yflo redHlom elwfin'

    >>> encrypt("I wonder how they encrypt in Mandarin", p4_2.encrypt)
    'Ioeh eertnaan nrotyny  nrwd wh cpiMdi'

    >>> encrypt("This term has flown by so fast", p4_3.encrypt)
    'Guvf grez unf sybja ol fb snfg'

    """
    encrypt_func = func(msg)
    return encrypt_func


def decrypt(msg: str, func: Callable[[str], str]) -> str:
    """Will decrypt the inputed text with chosen decryption function
    parameter: the message to be decrypted and the function to carry out decryption
    return: the implementation of chosen decryption function

    >>> decrypt('upi ra sdlcosPmknbedi eiiu', p4_1.decrypt)
    'Pumpkin bread is delicious'

    >>> decrypt('14253',p4_2.decrypt)
    '12345'

    >> decrypt('Jung n ybiryl qnl gbqnl',p4_3.decrypt)
    'What a lovely day today'
    
    """
    decrypt_func = func(msg)
    return decrypt_func


def main():
    """Main program to run our encryption/decryption process."""
    cipher = input('Which cipher do you wish to use? ' +
                   '[1=odd/even, 2=three-rail, 3=rot13]? ')
    if cipher == '1':
        encrypt_func = p4_1.encrypt
        decrypt_func = p4_1.decrypt
    elif cipher == '2':
        encrypt_func = p4_2.encrypt
        decrypt_func = p4_2.decrypt
    elif cipher == '3':
        encrypt_func = p4_3.encrypt
        decrypt_func = p4_3.decrypt
    else:
        raise ValueError("Unknown cipher, valid inputs are 1, 2, or 3")

    # Now get the string to encrypt or decrypt
    which = input('Do you wish to encrypt or decrypt a message [E/D]? ')
    if which.upper() == 'E':
        text = input('Enter a line of text to encrypt: ')
        print("Encrypted text:")
        print(encrypt(text, encrypt_func))
    elif which.upper() == 'D':
        text = input('Enter encrypted text to decrypt: ')
        print("Decrypted text:")
        print(encrypt(text, decrypt_func))
    else:
        raise ValueError("Invalid option, I only know E and D!")


if __name__ == '__main__':
    main()
