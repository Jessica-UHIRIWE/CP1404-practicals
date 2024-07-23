"""
Word Occurrences
Estimate: 30 minutes
Actual:   42 minutes
"""


def count_word_occurrences(text):
    words = text.split()
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


def main():
    text = input("Enter a string: ")

    word_counts = count_word_occurrences(text)

    # Find the maximum length of the words for formatting
    max_length = max(len(word) for word in word_counts)

    # Print the words and their counts, formatted
    for word, count in sorted(word_counts.items()):
        print(f"{word:>{max_length}} : {count}")


main()
