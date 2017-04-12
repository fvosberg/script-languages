#!/usr/local/bin/python3.6

import random

class ConsolePlayer(object):
    def guess(self):
        return int(input("Ganze Zahl eingeben: "))

    def inform(self, result):
        if result == Game.guessTooLow:
            print("Zahl ist zu klein")
        elif result == Game.guessTooHigh:
            print("Zahl ist zu groß")
        elif result == Game.guessRight:
            print("Richtig")

class AutoGuesser(object):
    def __init__(self):
        self.min = 0
        self.max = 100

    def guess(self):
        self.lastGuess = (self.max + self.min) // 2
        return self.lastGuess

    def inform(self, result):
        if result == Game.guessTooHigh:
            self.max = self.lastGuess
        elif result == Game.guessTooLow:
            self.min = self.lastGuess


class Game(object):
    guessTooLow = -1
    guessRight = 0
    guessTooHigh = 1
    noGuessesLeft = -2

    def __init__(self, maxGuesses, player=ConsolePlayer()):
        self.maxGuesses = maxGuesses
        random.seed()
        self.secret = random.randint(0, 100)
        self.currentRound = 0
        self.player = player
        print(self.secret)

    def guess(self, eingabe):
        if not self.guess_left():
            return Game.noGuessesLeft
        self.currentRound += 1
        if eingabe < self.secret:
            return Game.guessTooLow
        elif eingabe > self.secret:
            return Game.guessTooHigh
        elif eingabe == self.secret:
            return Game.guessRight

    def guess_left(self):
        return self.currentRound < self.maxGuesses

    def run(self):
        eingabe = 0

        while self.guess_left():
            res = self.guess(self.player.guess())

            self.player.inform(res)
            if res == Game.guessRight:
                print("Sie haben", self.currentRound, "Versuche benötigt")
                break
        else:
            print("Leider verloren; keine Versuche übrig")


#game = Game(10)
game = Game(10, player=AutoGuesser())
game.run()
