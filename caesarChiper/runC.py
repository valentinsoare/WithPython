#!/usr/bin/python

import string


def encrypt_rule(encrypt_by_rotation):
    list_default = list(string.ascii_lowercase)
    list_to_follow = []

    for i in range(len(list_default)):
        list_to_follow += list_default[(i + encrypt_by_rotation) % 26]

    return list_to_follow


def encrypt(given_message, rotated_list):
    given_message = list(given_message.lower())
    encrypted_message = []

    for i in given_message:
        letter = ord(i) - ord('a')
        if letter not in range(0, 26):
            encrypted_message += " "
        else:
            encrypted_message += rotated_list[letter]

    return ''.join(encrypted_message)


def decrypt(encrypted_message, rotation_value):
    all_letters = list(string.ascii_lowercase)
    after_decrypt = []

    for i in encrypted_message:
        if i == ' ':
            after_decrypt += " "
        for j in range(len(all_letters)):
            if i == all_letters[j]:
                letter = (j - rotation_value) % 26
                after_decrypt += all_letters[letter]

    return ''.join(after_decrypt)


def main():
    rotated_list = encrypt_rule(encrypt_by_rotation=8)

    message_after_encryption = encrypt("Lux si opulenta aici pe grupul asta. Numai d-astia care fac roboti.", rotated_list)
    print(f'Message after encryption: {message_after_encryption}')

    decrypted_message = decrypt(message_after_encryption, rotation_value=8)
    print(f'Message after decryption: {decrypted_message}')


if __name__ == '__main__':
    main()
