def get_num_words(book_path: str) -> int:
    with open(book_path) as f:
        text = f.read()
    words = text.split()
    return len(words)


def character_count(book_path: str) -> dict[str, int]:
    with open(book_path) as f:
        text = f.read()

    count_dict = {}
    for char in text.lower():
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    return dict(sorted(count_dict.items()))