from stats import get_num_words

def main():
    book_path = "./books/frankenstein.txt"
    num_words = get_num_words(book_path)
    print(f"Found {num_words} total words.")

main()
