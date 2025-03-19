def count_words(book_path: str, book_name: str):
    with open(book_path + book_name) as file:
        book_text = file.read()
        num_words = len(book_text.split())
        return num_words
        #print(f"{num_words} words found in the document")

def count_char(book_path: str, book_name: str):
    char_dict = {}
    with open(book_path + book_name) as file:
        book_text = file.read()
        for char in book_text.lower():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    #print(f"{len(book_text)} characters found in the document")
    #print(char_dict)
    sorted_char_dict = dict(sorted(char_dict.items(), key=lambda x: x[1], reverse=True))
    #print(sorted_char_dict)  # Print the sorted dictionary
    return sorted_char_dict

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict[1]




