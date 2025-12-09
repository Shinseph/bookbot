from stats import get_num_words, character_count, sort_character_dict

def main():
    book_path = "books/frankenstein.txt"
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    
    num_words = get_num_words(book_path)
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    
    raw_chars = character_count(book_path)
    sorted_chars = sort_character_dict(raw_chars)
    
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

main()