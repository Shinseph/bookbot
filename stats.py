def get_num_words(book_path):
    with open(book_path) as f:
        text = f.read()
    return len(text.split())


def character_count(book_path):
    with open(book_path) as f:
        text = f.read()
    
    count_dict = {}
    for char in text.lower():
        count_dict[char] = count_dict.get(char, 0) + 1
    
    return count_dict

def get_count(item):
    return item["num"]

def sort_character_dict(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():  
            char_list.append({"char": char, "num": count})

    char_list.sort(key=get_count, reverse=True)
    
    return char_list