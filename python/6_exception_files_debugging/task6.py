def doc_function(operation_type: str, file_path: str, content: str = None):
    """
    The function must perform actions with the file. In the case of reading, the content of the file should be displayed
    to the user.

    @param operation_type: File operation type (writing to a file, reading from a file, etc.).
    @param file_path: File path (The path to the file with which the operation will be performed).
    @param content: Content (optional argument).
    """

    try:
        with open(file_path, operation_type) as file:
            if operation_type == 'r':
                print(file.read())
            elif operation_type == 'w' or operation_type == 'a':
                file.write(content)
            else:
                print("No such operation type")
    except FileNotFoundError as error:
        print(f"[FileNotFoundError: My error description] {error}")
    except ValueError as error:
        print(f"[ValueError: My error description] {error}")
    except TypeError as error:
        print(f"[TypeError: My error description] {error}")
    except Exception as error:
        print(error)


print("Read 'test.txt' file:")
doc_function('r', './test.txt')
print("\nHandle 'FileNotFoundError':")
doc_function('r', './test1.txt')
print("\n'New line' overwrite 'test.txt'")
doc_function('w', './test.txt', 'New line')
doc_function('r', './test.txt')
print("\nNew line added to the end of the 'test.txt'")
doc_function('a', './test.txt', '\nNew line 2')
doc_function('r', './test.txt')
print("\nHandle 'ValueError':")
doc_function('s', './test.txt')
print("\nHandle 'ValueError':")
doc_function('r', './test.jpg')
print("\nHandle 'TypeError':")
doc_function('a', './test.txt', True)
