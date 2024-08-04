import os
from collections import Counter
import string

def main():
    path_to_file = os.path.join(os.path.dirname(__file__), "books/frankenstein.txt")
    with open(path_to_file, encoding='utf-8') as f:
        book_text = f.read()
    
    lowered_string = book_text.lower()
    words = lowered_string.split()
    word_count = len(words)
    
    letter_counts = Counter(c for c in lowered_string if c in string.ascii_lowercase)

    print(f"Total words found in the document: {word_count}")
    for letter, count in sorted(letter_counts.items()):
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

if __name__ == '__main__':
    main()
