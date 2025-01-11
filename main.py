def main():
    print("--- Begin report of books/frankenstein.txt ---")
    try:
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            words_count = count_words(file_contents)
            print(f"{words_count} words found in the document")
            print("\n")
            letters_count = count_letters(file_contents)
            for key, val in letters_count.items():
                if key.isalpha():
                    print(f"The {key} character was found {val} times")
            print("--- End report ---")


    except FileNotFoundError:
        print("The file 'frankenstein.txt' was not found. Please check the path.")

"""
This function reads text from  frankenstein.txt and counts the number of words"
"""
def count_words(text):
    word_arr = text.split()
    num_of_words = len(word_arr)
    return num_of_words


""" This function counts the number of letters in the entire book using a dictionary"""
def count_letters(text):
    letter_dict = dict()
    for letter in text:
        c = letter.lower()
        if c in letter_dict:
            letter_dict[c] += 1
        else:
            letter_dict[c] = 1
    return letter_dict
    
    

if __name__ == "__main__":
    main()
