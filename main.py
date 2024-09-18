"""module for my project"""


def main():
    """this is main function"""
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    words_amount = count_words(book_text)
    chars_amount = char_count(book_text)
    print(raport(chars_amount, words_amount))


def get_book_text(bp):
    """function reading text from books"""
    with open(bp, encoding="utf-8") as f:
        return f.read()


def count_words(text):
    """function counting words in text"""
    words = text.split()
    return len(words)


def char_count(text):
    """This function counts characters"""
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def raport(cc, wa):
    """This function makes a report"""
    raport_list = [{"char": x, "count": cc[x]} for x in cc if x.isalpha()]
    raport_list.sort(reverse=True, key=lambda x: x["count"])
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wa} words found in the document")
    print()
    for letter in raport_list:
        print(f"The '{letter['char']}' character was found {letter['count']} times")
    print("--- End report ---")


main()
