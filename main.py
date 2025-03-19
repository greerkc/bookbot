from stats import count_char, count_words
import sys

def get_book_text(book_path: str, book_name: str):
    with open(book_path + book_name) as file:
        book_text = file.read()
        print(book_text)
                
def main():
    if len(sys.argv) != 2: # was 3, but bug in class. Now need to provide path and file in one parameter
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = "./" + sys.argv[1]
    #book_name = sys.argv[2] This is changed due to bug in class test.
    book_name = ""
    
    
    #get_book_text("../bookbot/books/", "frankenstein.txt")
    word_count = count_words(book_path, book_name)
    char_count=count_char(book_path, book_name)
    
    #Print the report...
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}{book_name }...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count ----------")
    # Print the sorted dictionary in a special format
    for char, count in char_count.items():
        print(f"{char}: {count}")
    print("============= END ===============")
    #return sorted_char_dict
    
if __name__ == "__main__":
    main()