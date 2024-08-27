def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    word_count = count_words(book)

    print(f"The book has {word_count} words.")


def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def count_words(text):
    return len(text.split())

main()