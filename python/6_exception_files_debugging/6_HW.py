def files_operations (operation_type, file_path, file_content = ''):
    try:
        if operation_type == 'r':
            with open(file_path, 'r') as reader:
                print(reader.read())
        elif operation_type == 'rb':
            with open(file_path, 'rb') as reader:
                print(reader.read())
        elif operation_type == 'w':
            with open(file_path, 'w') as writer:
                writer.write(file_content)
        elif operation_type == 'wb':
            with open(file_path, 'wb') as writer:
                writer.write(bytes(file_content, 'utf-8'))
        elif operation_type == 'a':
            with open(file_path, 'a') as appender:
                appender.write(file_content)
        else:
            raise RuntimeError ('Incorrect operation type is provided')
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        print('Operation with file is finished successfully')
    finally:
        print('No more actions are expected within current execution')

files_operations('r', '6_hw_text.txt', '\nadd a comment.')
