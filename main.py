def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letter(text)
    display = reorganise(num_letters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for letter in display:
        print(f"The '{letter['letters']}' character was found {letter['count']} times")
    print("--- End report ---")

#Converting dictionnary in to a list of dict   
def reorganise(dict):
    list_of_dict = [{"letters": key, "count": value} for key, value in dict.items()]
    sorted_list = sorted(list_of_dict, key=lambda x: x["count"], reverse=True)
    return sorted_list

#counting words in book
def get_num_words(text):
    words = text.split()
    return len(words)

#reading the book
def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_letter(text):
    num_letter = {}
    for word in text:
        word = word.lower()
        # Check if the character is a letter
        if word.isalpha():
            # Update the count for this letter in the dictionary
            if word in num_letter:
                num_letter[word] +=1
            else:
                num_letter[word] = 1
    return num_letter

main()