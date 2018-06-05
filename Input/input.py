exit_value = True
while(exit_value):
    print("Enter a integer number to code, enter \"Exit\" to exit")
    input_str = input("Enter a value: ")
    try:
        if input_str.isdigit():
            input_int = int(input_str)
            print(input_int ** 3)
        else:
            if input_str.upper() == "EXIT":
                exit_value = False
            else:
                print("not an integer number, please try again")
    except ValueError:
        print("not an integer number, please try again")





