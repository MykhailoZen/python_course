# Create a function that will work with files.
# The function should have 3 arguments:
## File operation type (writing to a file, reading from a file, etc.).
## File path (The path to the file with which the operation will be performed).
## Content (optional argument).
# The function must perform actions with the file. In the case of reading, the content of the file should be displayed to the user.
# Add error handling (try to handle all common input errors).

import os

finally_remove = []

def file_function(file_operation: str, file_path: str, content: str) -> list[str]:
    try:
        if file_operation == 'create':
            f = open(file_path, 'w')
            f.write(content)
            f = open(file_path, 'r')
            print(f'File {file_path} created:\n{f.read()}')
            finally_remove.append(file_path)
        elif file_operation == 'add_string':
            f = open(file_path, 'a')
            f.write(content)
            f = open(file_path, 'r')
            print(f'New string added\nNow the file {file_path} contains\n{f.read()}')
        elif file_operation == 'read':
            f = open(file_path, 'r')
            print(f'The file {file_path} contains\n{f.read()}')
        else:
            print('No action defined')
        return finally_remove
    except FileNotFoundError:
        print (f'The {file_path} file does not exist to perform the {file_operation} file operation')
    except UnicodeDecodeError:
        print("Incorrect file type")
    except Exception as e:
        print(f'Undefined exception {e}')


if __name__ == '__main__':
    try:
        # Create a new file with some content for next operations. Note the file name to delete it in the end
        # Read the file and print the content of the file
        file_function('create', 'file1.txt', 'string1\n')
        # Add a string to the file
        file_function('add_string', 'file1.txt', 'string2\n')
        # Read the file which does not exist
        file_function('read', 'file4.txt', '')
        # Add a new file
        file_function('create', 'file2.txt', '')
    except TypeError:
        print('Incorrect parameters for')

# Cleanup: remove the files
    print(f'Files to remove: {len(finally_remove)}: {finally_remove}')
    for x in finally_remove:
        try:
            os.remove(x)
            print(f'File {x} is deleted')
        except FileNotFoundError:
            print(f'It is impossible to delete file {x} which does not exist.')
