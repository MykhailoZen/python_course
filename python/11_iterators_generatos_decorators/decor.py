# Create a decorator that logs the time taken by a function to execute.
import datetime

def time_decorator(func):
    def wrapper():
        start_time = datetime.datetime.now()
        func()
        end_time = datetime.datetime.now()
        print(f"{func.__name__} worked {(end_time-start_time).total_seconds():8.3f} seconds")
    return wrapper


@time_decorator
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "Admin" and password == "1234":
        print("Welcome!")
    else:
        print("Access denied!")


login()
