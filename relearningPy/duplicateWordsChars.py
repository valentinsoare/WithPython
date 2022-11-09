#!/usr/bin/python

import string
import collections


def header(message_to_print):
    some_leet_speak = {'u': '|_|', 's': '$', 'a': '@', 'o': '0', 'e': '3', 'n': '/\/', 'h': '[-]', 'd': '[)'}

    processed_message = ' *** '
    list_with_keys_for_message = some_leet_speak.keys()

    for i in message_to_print:
        if i in list_with_keys_for_message:
            processed_message += ' ' + some_leet_speak[i]
        else:
            processed_message += ' ' + i

    processed_message += ' *** '
    length_of_message = len(processed_message)

    print(f"\n{' ' * int(length_of_message * 0.25)}\033[1m|{'-' * int(length_of_message * 1.5)}|\033[0m")
    print(f"{' ' * int(length_of_message * 0.5)}\033[1;31m|{processed_message}|\033[0m")
    print(f"{' ' * int(length_of_message * 0.25)}\033[1m|{'-' * int(length_of_message * 1.5)}|\033[0m")


def load_text():
    given_text = """The IEM Rio Major is fast approaching, and you can show your support–team stickers, player autographs, and the Rio 2022 Viewer Pass are all available for purchase now! 50% of the proceeds go to the players, teams, and organizations taking part in the Major.
                    Viewer Pass, Stickers, and more
                    Pick up a Rio 2022 Viewer Pass and you’ll get an upgradable Rio 2022 Event Coin, access to the Pick’em Challenge, team graffiti, Steam.tv flair, and exclusive access to Rio 2022 Souvenir Packages.
                    Every time you upgrade your coin, you’ll receive a Souvenir Token that can redeemed for a Souvenir Package of the match of your choice. Souvenirs feature gold stickers of the teams and map of the match you selected.
                    You can earn up to three Souvenir Tokens by playing the Pick’em Challenge, but you can start with more–purchase the ‘Viewer Pass +3’ and you’ll get three Souvenir Tokens right away. And of course, you can purchase as many Souvenir Tokens as you’d like once you’ve activated your Pass.
                    Looking for your favorite Team or Player? Check out the Team and Player Autograph capsules, featuring paper, glitter, holo, and gold stickers. And shortly after the Grand Final concludes, Champions Autograph Capsules (feature autographs of players on the winning team) will be available for purchase.
                    Something Spooky in Today’s Update
                    Today’s update features several community map updates, including a special Halloween version of Ember. Jump into a Danger Zone match and give it a try, if you dare!"""

    list_with_text = list(map(lambda i: i.lower(), given_text.split()))
    return list_with_text


def prepared_text(given_list_with_txt):
    chars_to_remove = string.punctuation + '’' + '‘'
    length_of_list_with_words = len(given_list_with_txt)

    for i in range(length_of_list_with_words):
        for j in chars_to_remove:
            if j in given_list_with_txt[i]:
                given_list_with_txt[i] = given_list_with_txt[i].replace(j, '').strip()

    return given_list_with_txt


def counting_duplicate_words(given_text_as_list):
    dict_with_count_words = collections.Counter(given_text_as_list)
    list_with_uniq_words = list(dict_with_count_words.keys())

    return dict_with_count_words, list_with_uniq_words


def printing_counting_duplicate_words(words_counting):
    print(f"\n{' ' * 25}{'Words':<20}{'Counter':<15}{'Percentage'}")
    sorted_by_count = sorted(words_counting.items(), key=lambda i: i[1], reverse=True)
    number_of_words = sum(words_counting.values())

    count = 0
    for word, counter in sorted_by_count:
        print(f"{' ' * 20}{count + 1:>3}. {word:<20}{counter:<15}{(counter/number_of_words) * 100:.2f}%")
        count += 1


def printing_uniq_words(uniq_words):
    uniq_words = sorted(uniq_words)

    print(f"\n{' ' * 19} * Uniq words in alphabetical order: ")
    print(f"{' ' * 22}", end="")

    for i in range(len(uniq_words)):
        if (i + 1) % 10 == 0:
            print(f"{uniq_words[i]}\n{' ' * 22}", end="")
        elif i == len(uniq_words) - 1:
            print(f"{uniq_words[i]}", end=" ")
        else:
            print(f"{uniq_words[i]}, ", end=" ")


def prepare_chars(given_text_list_words_uniq):
    list_with_letters = []

    for i in given_text_list_words_uniq:
        for j in list(i):
            list_with_letters.append(j)

    return list_with_letters


def counting_chars(list_with_chars):
    dict_with_number_of_chars = collections.Counter(list_with_chars)
    return dict_with_number_of_chars


def check_all_alphabet_letters(given_counter):
    list_with_letters = given_counter.keys()
    all_letters_from_alphabet = string.ascii_lowercase

    letters_that_are_not_in_text = set(all_letters_from_alphabet).difference(list_with_letters)

    return letters_that_are_not_in_text


def printing_chars(given_list_count):
    our_punctuation = string.punctuation + '’' + '‘' + '–'
    print(f"\n\n{' ' * 25} {'Letter':<20} {'Number of appearances':<15}")
    count = 0
    sorted_by_count = list(sorted(given_list_count.items(), key=lambda k: k[1], reverse=True))

    for i, j in sorted_by_count:
        if i not in our_punctuation:
            print(f"{' ' * 20} {count + 1:>3}. {i:<21}{j}")
            count += 1


def printing_letters_that_are_not_present(list_of_letters_not_present):
    print(f"\n{' ' * 19} * Letters from alphabet that are not in text:", end=" ")
    list_of_letters_not_present = list(list_of_letters_not_present)

    for i in range(len(list_of_letters_not_present)):
        print(f"{list_of_letters_not_present[i]}", end=" ")

    print("\n")


def main():
    header('Duplicate Words, Counting Chars')

    list_with_text = load_text()
    processed_text_without_punctuation = prepared_text(list_with_text)

    counting_words_dict, list_uniq_words = counting_duplicate_words(processed_text_without_punctuation)
    printing_counting_duplicate_words(counting_words_dict)
    printing_uniq_words(list_uniq_words)

    list_with_chars = prepare_chars(list_uniq_words)
    counter_chars = counting_chars(list_with_chars)
    printing_chars(counter_chars)

    letters_from_alphabet_not_in_text = check_all_alphabet_letters(counter_chars)
    printing_letters_that_are_not_present(letters_from_alphabet_not_in_text)


if __name__ == '__main__':
    main()
