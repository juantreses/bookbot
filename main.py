def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    word_count = count_words(book)
    chars_dict = get_chars_dict(book)
    sorted_list = char_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def count_words(text):
    return len(text.split())

def sort_on(d):
    return d["num"]

def char_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append({"char": ch, "num": chars_dict[ch]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list

def get_chars_dict(text):
    chars_dict = {}
    for char in text.lower():
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

main()