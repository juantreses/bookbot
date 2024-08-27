def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    word_count = count_words(book)
    chars_dict = get_chars_dict(book)

    print(f"{chars_dict}")


def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def count_words(text):
    return len(text.split())

def get_chars_dict(text):
    chars_dict = {}
    for char in text.lower():
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

main()