# this function adds two number
def add(x,y):
    print(x + y)

add(6,7)

# this function multiplies two number
def multiply(x,y):
    print(x * y)

multiply(6,7)

# this function subtracts two number
def sub(x,y):
    print(x - y)

sub(6,7)

# this function divideds two number
def div(x,y):
    print(x / y)

div(6,7)
####################################################
#_________________________________________________

###Start of program
print("Welcome to my cool calc app!")
while(True):
    print("What would you like to do?")
    print("type (a)dd (s)ubtract (m)ultiply (d)ivide (q)uit")

    user_choice = input(" : ")
    #print(user_choice)

    if user_choice == 'a':
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        add(x,y)

    elif user_choice == 's':
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        sub(x,y)

    elif user_choice == 'm':
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        multiply(x,y)

    elif user_choice == 'd': 
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        div(x,y)
     
    elif user_choice == 'q':
        print("Thanks for using my cool calc app!")


    else:
        print("Invalid Input Try Again.")