# Create a function that will work with files.
# The function should have 3 arguments:
# 1. File operation type (writing to a file, reading from a file, etc.).
# 2. File path (The path to the file with which the operation will be performed).
# 3. Content (optional argument).
# The function must perform actions with the file. In the case of reading, the content of the file should be displayed to the user.
# Add error handling (try to handle all common input errors).

def ksu_function(file_operation_type: str, file_path: str, content: str = "blablabla") -> None:
    operations = {"write": "w", "read": "r", "update": "a"}
    try:
        op = operations[file_operation_type]
        with open(file_path, op) as f:
            if op in ("w", "a"):
                f.write(content)
            else:
                print(f.read())
    except KeyError:
        print("Wrong operation type!")
    except FileNotFoundError:
        print("File not found!")
    except TypeError:
        print("Wrong content type!")


if __name__ == "__main__":
    ksu_function("write", "tratata.txt", "dghxfjy")
    ksu_function("read", "tratata.txt")
    ksu_function("update", "tratata.txt", content="blablabla")

    ksu_function("delete", "tratata.txt", "dghxfjy")
    ksu_function("read", "tratata456.txt", "dghxfjy")
    ksu_function("update", "tratata456.txt", 678)
