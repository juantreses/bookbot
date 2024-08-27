def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    print(book)


def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

main()