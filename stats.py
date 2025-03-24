def get_num_words(num_words):
    counter = 0
    for num_word in num_words:
        counter += 1
    return counter

def get_each_char(file_content):
    dict_chars = {}
    lowered_chars = file_content.lower()

    for lowered_char in lowered_chars:        
        if lowered_char in dict_chars:
            dict_chars[lowered_char] += 1
        else:
            dict_chars[lowered_char] = 1

    return dict_chars

def sort_on(num_char):
    ordered_list = [{"char": char, "count": count}
    for char, count in num_char.items() if char.isalpha()]
    ordered_list.sort(key=lambda x: x["count"], reverse=True)
    
    return ordered_list