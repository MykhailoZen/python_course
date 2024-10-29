# Create a function that will work with files.
# The function should have 3 arguments:
#
# File operation type (writing to a file, reading from a file, etc.).
# File path (The path to the file with which the operation will be performed).
# Content (optional argument).
# The function must perform actions with the file. In the case of reading, the content of the file should be displayed to the user.
# Add error handling (try to handle all common input errors).

def file_function(operation_type: str, file_path: str, content: str) -> None:
    """
    This function performs actions with the files.
    @param operation_type: writing to a file, reading from a file, append content to a file
    @param file_path: The path to the file with which the operation will be performed
    @param content: Text content of the file
    @return: None
    """
    operation_value = {'write': 'w', 'read': 'r', 'append': 'a'}
    try:
        ov = operation_value[operation_type]
        with open(file_path, ov) as file:
            if ov == 'w' or ov == 'a':
                file.write(content)
            else:
                print(file.read())
    except KeyError:
        print(f"The value '{operation_type}' is unacceptable")
    except FileNotFoundError:
        print(f"The file with path '{file_path}' does not exist")
    except TypeError:
        print("The type of the content value is not acceptable")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    file_function("write", "test1.txt", "test example 1 ")
    file_function("append", "test1.txt", "\ntest example 2 ")
    file_function("read", "test1.txt", "test example 3 ")

    file_function("delete", "test1.txt", "test example 1 ")
    file_function("read", "test.txt", "test example 3 ")
    file_function("write", "test1.txt", True)
    file_function("read", "test2.png", "test example 4 ")
