class RandomNumberGame:
    from random import randint

    def __init__(self, lower_range=0,upper_range=100):
        self.lower = lower_range
        self.upper = upper_range
        self.correct = self.randint(lower_range, upper_range)

    def playgame(self):
        print("Please guess a number between %d and %d, or Q to quit" %(self.lower, self.upper ))
        correct_answer = False
        while(True != correct_answer):
            selected = self.getInput()
            if(selected == "Q"):
                break
            else:
                correct_answer = self.giveFeedBack(selected)



    def getInput(self):
        guess = 0
        valid_input = False
        while(False == valid_input):
            input_str = input("Enter your guess: ")
            if input_str.isdigit():
                guess = int(input_str)
                break
            elif input_str.isnumeric():
                print("number %f entered is not an integer number, please enter a valid integer number\n" % (float(input_str)))
            else:
                if "Q" == input_str.strip().upper():
                    print("quitting")
                    guess = "Q"
                    break
                else:
                    print("please enter a valid integer number, you entered: ", input_str, "\n")
        return guess

    def giveFeedBack(self, selected):
        if selected == self.correct:
            print("Congratulations that's the correct number\n")
            return True
        elif selected < self.correct:
            print("number entered is too low, please try again\n")
        else:
            print("number entered is too high, please try again\n")
        return False
