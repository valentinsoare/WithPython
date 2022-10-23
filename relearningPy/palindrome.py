#!/usr/bin/python


def is_palindrome(given_word):

    if len(given_word) % 2 == 0:
        return False

    list_stack_as_string = ''
    list_to_process = list(given_word.lower())

    for i in range(len(list_to_process)):
        list_stack_as_string += list_to_process.pop()

    if list_stack_as_string == given_word:
        return True
    else:
        return False


def main():
    word = 'radar'
    if is_palindrome(word):
        print(f"{word} is palindrome")
    else:
        print(f"{word} is not a palindrome")


if __name__ == '__main__':
    main()
