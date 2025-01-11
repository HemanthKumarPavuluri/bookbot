def main():
    try:
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            print(file_contents)
    except FileNotFoundError:
        print("The file 'frankenstein.txt' was not found. Please check the path.")

if __name__ == "__main__":
    main()
