#
# # *args and **kwargs
#
# def add(string: str, *num: int, adding: str) -> int:
#     """
#     Add function that can add 2 or more numbers
#     """
#     if adding == "add":
#         return sum(num)
#     elif adding == "sub":
#         return num[0] - num[1]
#     elif adding == "mul":
#         return num[0] * num[1]
#     elif adding == "div":
#         return num[0] / num[1]
#     else:
#         return "Invalid operation"
#
# print(add("add", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, adding="add"))
#
# # * and / in function arguments
#
# def func(name : str, / , age : int, * , address : str ) -> None :
#     print(f"Name: {name}, Age: {age}, Address: {address}")
#
# func("ram", age= 22 , address="ktm")
#
# # chat bot mini project
#
##import sys
# from datetime import datetime
#
# def chat_bot(txt : str) -> str :
#     lowerd : str =txt.lower()
#     if lowerd in ["hi", "hello", "hey"]:
#         return "Hello there! How can I help you?"
#     elif lowerd in ["time", "current time", "what time is it"]:
#         return f"The current time is {datetime.now().strftime('%H:%M:%S')}"
#     elif lowerd in ["exit", "quit", "bye"]:
#         sys.exit()
#     else:
#         return "I am a simple chat bot. I can only tell you the current time. If you want to exit, type 'exit'."
#
# while True:
#     x=input("Enter your message: ")
#     if x == "exit":
#         sys.exit()
#     bot_response : str = chat_bot(x)
#     print(f'Bot: {bot_response}')

## error handling try and except block

# total=0
# while True:
#     user_input= input("Enter a number: ")
#     if user_input == "0":
#         print(f"Total: {total}")
#         sys.exit()
#     try:
#         total += int(user_input)
#     except Exception as e:
#         print(f'error occured: {e}')


#else and finally block
#
# age = input("Enter a number: ")
# try:
#     result :float = 1 / int(age)
# except ZeroDivisionError:
#     print("You can't divide by zero")
# except ValueError:
#     print("Please enter a valid number")
# else:
#     print(f'this block wil be executed if there is no error')
#
# finally:
#     print("this block will always be executed ")
#
# # raise an exception
#
# age = input("Enter a number: ")
# try:
#     if int(age) < 0:
#         raise ValueError("age can't be negative")
# except Exception as e:
#     print(f"error occured: {e}")
#
# #unknown error
#
# while True:
#     user_input = input("Enter a number: ")
#     try:
#         num :float = float(user_input)
#     except Exception as e:
#         print(f'type of error occured: {type(e)}')
#         print(f"error occured: {e}")
#
# # letters only project
#
# import string
#
# def is_letter_only(txt : str) -> None:
#     aplhabet : str = string.ascii_letters + " "
#     for char in txt:
#         if char not in aplhabet:
#             raise ValueError("Invalid character found")
#
#         print(f'{char} is a letter only string')
#
# def main() -> None:
#     while True:
#         try:
#             user_input = input("Enter a string: ")
#             is_letter_only(user_input)
#         except Exception as e:
#             print(f"error occured: {e}   {type(e)}")
#
#
#
# user=input("Enter a number: ")
# try:
#     calc=1/int(user)
#     print(calc)
# except ZeroDivisionError:
#     print("You can't divide by zero")
# except ValueError:
#     print("Please enter a valid number")

# def change_name() -> None:
#     name = "satyam"
#
#     def change_again() -> None:
#         nonlocal name
#         name = "maddeshiya"
#     change_again()
#     print(name)
#
# change_name()

# #list comprehension
# name = ["Ram", "shyam", "hari", "gita"]
# name_lc = [i for i in name if i.startswith("h", 0)]
# print(name_lc)


