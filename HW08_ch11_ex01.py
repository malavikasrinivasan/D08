#!/usr/bin/env python3
# HW08_ch11_ex01
# Write a function that reads the words in words.txt and stores them as keys
# in a dictionary (returning the dictionary). It doesn’t matter what the
# values are. Then you can use the in operator as a fast way to check whether
# a string is in the dictionary.
###############################################################################
# Imports


# Body
def read_from_file(filename):
    with open(filename, "r") as f:
        file_contents = f.readlines()
    return file_contents


def store_to_dict():
    file_contents = read_from_file("words.txt")
    words = {word.strip(): idx for idx, word in enumerate(file_contents)}
    return words


###############################################################################
def main():  # DO NOT CHANGE BELOW
    words_dict = store_to_dict()
    if "this" in words_dict:
        print("Yup.")
    if "qwertyuiop" in words_dict:
        print("Hmm.")

if __name__ == '__main__':
    main()
