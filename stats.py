def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(items):
    return items["num"]

def get_sorted_list(dict):
    chars_list = []
    for char in dict:
        chars_list.append({"char": char, "num": dict[char]})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

