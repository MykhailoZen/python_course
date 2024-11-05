def work_with_files(mode, path, content=""):
    try:
        if mode == "r":
            with open(path, "r") as file:
                print(file.read())
        elif mode == "w":
            with open(path, "w") as file:
                file.write(content)
        elif mode == "a":
            with open(path, "a") as file:
                file.write("\n" + content)
        else:
            raise NameError("Wrong_argument")
    except FileNotFoundError:
        print("File does not exist")
    except NameError:
        print("Wrong argument: only \"r, w, a\" are acceptable")



work_with_files("a", "my_file.txt", "privet")
work_with_files("r", "my_file.txt")



