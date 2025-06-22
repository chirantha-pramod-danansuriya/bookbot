from stats import count_characters, dictonery_sort, get_num_words
import sys

def get_book_text(filepath: str) -> str:
    with open(file=filepath) as file:
        return file.read()
    
def main():
    path = str()
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    text = get_book_text(path)
    word_count = get_num_words(text)
    character_count_dic = count_characters(text=text)
    char_list = dictonery_sort(character_count_dic)
    
    # Printing output

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for chars in char_list:
        if chars["char"].isalpha():
            print(f"{chars['char']}: {chars['nums']}")

main()