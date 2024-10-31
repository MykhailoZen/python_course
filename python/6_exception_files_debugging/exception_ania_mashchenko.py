# Create a function that will work with files.
# The function should have 3 arguments:
# File operation type (writing to a file, reading from a file, etc.).
# File path (The path to the file with which the operation will be performed).
# Content (optional argument).
# The function must perform actions with the file. In the case of reading, the content of the file should be displayed to the user.
# Add error handling (try to handle all common input errors).

def operations_in_files(file_oper_type: str, file_path: str, content: str = "ABC"):
    """
    Function that will work with files
    :param file_oper_type: writing to a file, reading from a file, etc.
    :param file_path: The path to the file with which the operation will be performed.
    :param content: Content of the file.
    """
    dict_operations = {"write": "w", "read": "r", "append": "a"}
    try:
        op_type = dict_operations[file_oper_type]
        with open(file_path, op_type) as f:
            if op_type == "w" or op_type == "a":
                f.write(content)
            elif op_type == "r":
                print(f.read())
    except KeyError:
        print("Not valid operation type")
    except FileNotFoundError as error1:
        print(error1)
    except TypeError as error2:
        print(error2)
    except Exception as error3:
        print(error3)


if __name__ == "__main__":
    operations_in_files("write", "homework.txt", "one")
    operations_in_files("append", "homework.txt", "two")
    operations_in_files("read", "homework.txt")

    operations_in_files("sgeth", "homework.txt", "two")
    operations_in_files("read", "sdfrgf.txt", "two")
    operations_in_files("write", "homework.txt", True)
    operations_in_files("read", "1.jpeg", "two")
