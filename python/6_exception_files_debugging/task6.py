def doc_function(operation_mode: str, file_path: str, content: str = None):
    """
    The function must perform actions with the file. In the case of reading, the content of the file should be displayed
    to the user.

    @param operation_mode: File operation type (writing to a file, reading from a file, etc.).
    @param file_path: File path (The path to the file with which the operation will be performed).
    @param content: Content (optional argument).
    """
    operations = {"write": "w", "read": "r", "update": "a"}
    try:
        with open(file_path, operations[operation_mode]) as file:
            if operations[operation_mode] == 'r':
                print(file.read())
            elif operations[operation_mode] == 'w' or operations[operation_mode] == 'a':
                file.write(content)
            else:
                print("No such operation type")
    except FileNotFoundError as error:
        print(f"[FileNotFoundError: My error description] {error}")
    except ValueError as error:
        print(f"[ValueError: My error description] {error}")
    except TypeError as error:
        print(f"[TypeError: My error description] {error}")
    except KeyError as error:
        print(f"[KeyError: My error description] {error}")
    except Exception as error:
         print(error)


if __name__ == "__main__":
    print("Read 'test.txt' file:")
    doc_function('read', './test.txt')
    print("\n'New line' overwrite 'test.txt'")
    doc_function('write', './test.txt', 'New line')
    doc_function('read', './test.txt')
    print("\nNew line 2 added to the end of the 'test.txt'")
    doc_function('update', './test.txt', '\nNew line 2')
    doc_function('read', './test.txt')

    print("\nHandle 'FileNotFoundError':")
    doc_function('read', './test1.txt')
    print("\nHandle 'KeyError':")
    doc_function('save', './test.txt')
    print("\nHandle 'ValueError':")
    doc_function('read', './test.jpg')
    print("\nHandle 'TypeError':")
    doc_function('update', './test.txt', True)
