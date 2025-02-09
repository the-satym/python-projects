import sys
def welcome_message():
    print("Welcome to the grocery list app")
    print("-"*34)
    print("enter 1 to add an item\n"
          "enter 2 to remove an item\n"
          "enter 3 to view the list\n"
          "enter 4 to exit")
    print("-"*34)

def add_item(item: str, groceries: list[str]) -> str:
    groceries.append(item)
    print(f'{item} added to the list')

def remove_item(item: str, groceries: list[str]) -> str:
    if item in groceries:
        groceries.remove(item)
        print(f'{item} removed from the list')
    else:
        print(f'{item} not found in the list')

def groceries_list(groceries: list[str]) -> str:
    print ("_________Grocery list_________")
    for i, item in enumerate(groceries,1):
        print(f'{i}. {item}')
    print('-'*34)

def is_option(option: int) -> bool:
    if option in [1,2,3,4]:
        return True

def main() -> None:
    groceries: list[str] = []
    welcome_message()
    while True:
        try:
            option=int(input("choose an option:   "))
            if not is_option(option):
                print("Invalid option")
                continue
            if option == 1:
                item = input("enter the item to add in the list:   ")
                add_item(item, groceries)
            elif option == 2:
                item=input("enter the item to remove from the list:   ")
                remove_item(item, groceries)
            elif option == 3:
                groceries_list(groceries)
            elif option == 4:
                print("shutting down the app")
                sys.exit()
        except ValueError:
            print("invalid input! please enter a number")
            continue

if __name__ == '__main__':
    main()







