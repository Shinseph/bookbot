from stats import get_num_words, character_count

def main():
    book_path = "books/frankenstein.txt"
    num_words = get_num_words(book_path)
    print(f"Found {num_words} total words.")
    characters = character_count(book_path)
    print(characters)

main()
