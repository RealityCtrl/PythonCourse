exit_value = True
while(exit_value):
    print("Enter a integer number to code, enter \"Exit\" to exit")
    input_str = input("Enter a value: ")
    try:
            input_int = int(input_str)
            print(input_int ** 3)
    except ValueError:
        print("not an integer number, please try again\n")
    else:
        print("Thank you please enter another number\n")
    finally:
        if not input_str.isnumeric():
            if input_str.upper() == "EXIT":
                exit_value = False





