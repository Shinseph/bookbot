def get_book_text(book_path):
    with open(book_path) as file:
        file_content = file.read()
    return file_content

def get_num_words(book_path):
    text = get_book_text(book_path)
    words = text.split()
    return len(words)