#date: 15 jan 2025


run = input("enter 'y' to use addition calculator and enter 'n' to terminate:-   ").lower()
print("enter zero '0' to get the final result")
while run=="y":
    total=0
    while True:
        user=int(input("enter the no. you want to add:-   "))
        if user<0:
            print("enter a positive no.")
            continue
        if user==0:
            print(f'total is {total}')
            break
        total+=user
    run = input("enter 'y' to use addition calculator and enter 'n' to terminate:-   ").lower()


