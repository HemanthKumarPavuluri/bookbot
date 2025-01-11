def main():
    try:
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            count_words(file_contents)
    except FileNotFoundError:
        print("The file 'frankenstein.txt' was not found. Please check the path.")

def count_words(text):
    num_of_words = len(text.split())
    print(num_of_words)
if __name__ == "__main__":
    main()
