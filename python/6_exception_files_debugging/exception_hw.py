# Practice:
# Create a function that will work with files.
# The function should have 3 arguments:
#
# File operation type (writing to a file, reading from a file, etc.).
# File path (The path to the file with which the operation will be performed).
# Content (optional argument).
# The function must perform actions with the file. In the case of reading, the content of the file should be displayed to the user.
# Add error handling (try to handle all common input errors).

# file: input("Enter operation type (R or W)")

def file_modifier(operation: str, path: str, content: str = "") -> None:
    mode_dict = {"write": "w", "read": "r", "append": "a"}
    try:
        op = mode_dict[operation]
        with open(path, op) as breed_file:
            if op == "w" or op == "a":  # if op in ("w", "a"):
                breed_file.write(content)
            elif op == "r":
                print(breed_file.read())
    except KeyError:
        print("Incorrect key, please use: write/read/append")
    except FileNotFoundError:
        print("File path is incorrect")
    except UnicodeDecodeError:
        print("File type does not support Unicode type")
    except TypeError as e:
        print(f"Unexpected error: {e}")
    except Exception as a:
        print(a)


if __name__ == "__main__":
    file_modifier("write", "dog_breeds.txt", "Write Bichon Frise\n")
    file_modifier("append", "dog_breeds.txt", "Append Bichon Frise\n")
    file_modifier("read", "dog_breeds.txt", "Bichon Frise")

    file_modifier("del", "dog_breeds.txt", "Bichon Frise")
    file_modifier("read", "dog_breed.txt", "Bichon Frise")
    file_modifier("read", "img.png", "Bichon Frise")
    file_modifier("write", "dog_breeds.txt", True)
