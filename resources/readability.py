# TODO
from cs50 import get_string
import re

# functions to check l, w, s


def main():
    while True:
        text = input("Text: ")
        words = get_words_count(text)
        letters = get_letters_count(text) / words
        sentences = get_sentence_count(text) / words

        calculate_grade(letters, words, sentences)

        break
    
# checking letters between a -z


def get_letters_count(text):
    letters = re.findall('[A-Za-z]', text)
    letters_count = len(letters)
    return letters_count

# checking words defined by space


def get_words_count(text):
    words = text.split(" ")
    words_count = len(words)
    return words_count

# checking length of word and special characters to identify end of sentence


def get_sentence_count(text):
    matches = re.findall('[.!?]', text)
    sentence_count = len(matches)
    return sentence_count

# pass through coleman-liau index to check grade


def calculate_grade(l, w, s):
    grade = round(0.0588 * (l * 100) - 0.296 * (s * 100) - 15.8)

    if grade < 1:
        print("Before Grade 1")
    elif grade >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")


main()