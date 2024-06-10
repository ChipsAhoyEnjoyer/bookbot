def main(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def word_count(string):
    return len(string.split())

def sort_dict(dict):
    return dict["count"]

def character_count(string, *character: str):
    char_count = {x.lower(): 0 for x in character}
    for char in string.lower():
        if char in char_count:
            char_count[char] += 1
    formatted_count = []
    for char in char_count:
        formatted_count.append({"character": char, "count": char_count[char]})
    formatted_count.sort(reverse=True, key=sort_dict)
    return formatted_count

def report(path, word_count: int, character_count):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words were for in this document")
    for dict in character_count:
        print(f"The {dict['character']} character was found {dict['count']} times")
    print("--- End report ---")
    

path = "books/frankenstein.txt"
text = main(path)
book_words = word_count(text)
letter_count = character_count(text, 'a', 'b', 'c', 'd', 'e', 'f', 
                                     'g', 'h', 'i', 'j', 'k', 'l', 
                                     'm', 'n', 'o', 'p', 'q', 'r', 
                                     's', 't', 'u', 'v', 'w', 'x', 
                                     'y', 'z', 'A', 'B', 'C', 'D', 
                                     'E', 'F', 'G', 'H', 'I', 'J', 
                                     'K', 'L', 'M', 'N', 'O', 'P', 
                                     'Q', 'R', 'S', 'T', 'U', 'V', 
                                     'W', 'X', 'Y', 'Z', '1')
final_report = report(path, book_words, letter_count)
