def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_characters(text: str) -> dict:
    result = {}
    for c in text:
        c = c.lower()
        if c in result:
            result[c] += 1
        else: 
            result[c] = 1
    return result

def sort_on(Item):
    return Item["nums"]

def dictonery_sort(chat_dict: dict):
    dict_list = [{"char": k, "nums": chat_dict[k]} for k in chat_dict]
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
