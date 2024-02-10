import random
import sys

class Decidenumber:
    def __init__(self):
        self.min = 0
        self.max = 100

    def inputMinMax(self):
        while True:
            try:
                sys.stdout.buffer.write(b'Guess the number game. Enter minimam number:\n')
                sys.stdout.flush()
                self.min = int(sys.stdin.buffer.readline().strip())
                sys.stdout.buffer.write(b'Enter maximum number:\n')
                sys.stdout.flush() 
                self.max = int(sys.stdin.buffer.readline().strip()) 
                if self.min < self.max:
                    break
                else:
                    sys.stdout.buffer.write(b"Make the value greater than the minimum value\n")
            except ValueError:
                sys.stdout.buffer.write(b"You can enter only number\n")
        return random.randint(self.min,self.max)
        
class Gameplay:
    def __init__(self):
        self.game_number = Decidenumber().inputMinMax()

    def userInput(self):
        while True:
            sys.stdout.buffer.write(b'Enter your choice:\n')
            sys.stdout.flush()
            guess = sys.stdin.buffer.readline().strip() 
            try:
                guess = int(guess)
                return guess
            except ValueError:
                sys.stdout.buffer.write(b"You can enter only number\n")
        
    def outputMessage(self,messege):
        sys.stdout.buffer.write(messege)
        
    def judgeTheGame(self,guess):
        if self.game_number == guess:
            return True
        elif guess < self.game_number:
            self.outputMessage(b"Guess a bigger number\n")
            return False
        else:
            self.outputMessage(b"Guess a smaller number\n")
            return False

    def play(self):
        for i in range(7):
            guess = self.userInput()
            if self.judgeTheGame(guess):
                sys.stdout.buffer.write(b"You win the game!\n")
                break
        else:
            lose_message = f"You lose. The number is {self.game_number}.\n".encode("utf-8")
            sys.stdout.buffer.write(lose_message)

if __name__ == "__main__":
    Gameplay().play()
