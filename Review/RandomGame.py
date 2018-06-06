class RandomNumberGame:
    from random import randint
    from math import sqrt;
    from itertools import count, islice

    hint = "-2"
    iseven = False
    prime = False
    square = False
    correct = -9999
    quit = ["Q", "Quit", "Exit"]
    quit_ID = "Q"

    def __init__(self, lower_range=0, upper_range=100):
        self.lower = lower_range
        self.upper = upper_range
        self.setup_game()

    def play_game(self):
        print("Please guess a number between %d and %d, Q to quit or -2 for a hint" % (self.lower, self.upper))
        self.game_logic()

    def setup_game(self):
        self.generate_random()
        self.generate_hints()

    def generate_random(self):
        self.correct = self.randint(self.lower, self.upper)

    def generate_hints(self):
        if (self.correct % 2) == 0:
            self.iseven = True
        if self.is_prime(self.correct):
            self.prime = True
        if self.sqrt(self.correct).is_integer():
            self.square = True

    def is_prime(self, n):
        return n > 1 and all(n % i for i in self.islice(self.count(2), int(self.sqrt(n) - 1)))

    def game_logic(self):
        correct_answer = False
        while not correct_answer:
            selected = self.get_input()
            if selected == self.quit_ID:
                break
            elif selected == -2:
                self.give_hint()
            else:
                correct_answer = self.give_feedback(selected)

    def get_input(self):
        guess = 0
        valid_input = False
        while not valid_input:
            input_str = input("Enter your guess: ")
            if input_str.isdigit() or input_str == self.hint:
                guess = int(input_str)
                break
            elif input_str.isnumeric():
                print("number %f entered is not an integer number, please enter a valid integer number\n" % (
                    float(input_str)))
            else:
                if input_str.strip().upper() in self.quit:
                    print("quitting")
                    guess = self.quit_ID
                    break
                else:
                    print("please enter a valid integer number, you entered: ", input_str, "\n")
        return guess

    def give_hint(self):
        if self.iseven:
            print("Number is even")
        else:
            print("Number is odd")
        if self.prime:
            print("Number is a prime number")
        else:
            print("Number is not a prime number")
        if self.square:
            print("Number is a square number")
        else:
            print("Number is not a square number")
        print("\n")

    def give_feedback(self, selected):
        if selected == self.correct:
            print("Congratulations that's the correct number\n")
            return True
        elif selected < self.correct:
            print("number entered is too low, please try again\n")
        else:
            print("number entered is too high, please try again\n")
        return False

    def __str__(self):
        return "Game State:\ngenerated number: %d\nis prime: %s\nis even: %s\nis square: %s\n" \
               % (self.correct, self.prime, self.iseven, self.square)
