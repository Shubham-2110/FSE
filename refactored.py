from random import choice, randrange
from string import ascii_lowercase
from turtle import *

class TypingGame:
    def __init__(self):
        self.targets = []
        self.letters = []
        self.score = 0
        self.speed = 1
        self.frequency = 20

    def inside(self, point):
        return -200 < point.x < 200 and -200 < point.y < 200

    def draw(self):
        clear()
        for target, letter in zip(self.targets, self.letters):
            goto(target.x, target.y)
            write(letter, align='center', font=('Consolas', 20, 'normal'))
        update()

    def create_target(self):
        if randrange(self.frequency) == 0:
            x = randrange(-150, 150)
            target = vector(x, 200)
            self.targets.append(target)
            letter = choice(ascii_lowercase)
            self.letters.append(letter)

    def move_targets(self):
        for target in self.targets:
            target.y -= self.speed

    def check_targets(self):
        for target in self.targets[:]:
            if not self.inside(target):
                idx = self.targets.index(target)
                del self.targets[idx]
                del self.letters[idx]
                self.score -= 1

    def handle_key_press(self, key):
        if key in self.letters:
            self.score += 1
            idx = self.letters.index(key)
            del self.targets[idx]
            del self.letters[idx]
        else:
            self.score -= 1

        print('Score:', self.score)

    def setup_game(self):
        setup(420, 420, 370, 0)
        hideturtle()
        up()
        tracer(False)
        listen()
        for letter in ascii_lowercase:
            onkey(lambda letter=letter: self.handle_key_press(letter), letter)

    def start_game(self):
        self.setup_game()
        while True:
            self.create_target()
            self.move_targets()
            self.draw()
            self.check_targets()
            ontimer(self.start_game, 100)

def main():
    game = TypingGame()
    game.start_game()
    done()

if __name__ == "__main__":
    main()