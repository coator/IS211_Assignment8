"""Pig game"""

import argparse
import random


class CustomErrorExceptions:
    class ErrorPlayerIntInvalid(ValueError):
        pass


class Dice:
    def __init__(self):
        self.roll_amt = 0
        self.roll_list = []
        self.dice_seed_list = []

    def __repr__(self):
        return self.roll_amt

    def Roll(self):
        """generates a new dice for the dice class"""
        result = random.choices((1, 2, 3, 4, 5, 6))
        self.roll_amt += 1
        self.roll_list.append(result[0])
        print('Dice result is {}'.format(result))
        return result[0]


class Player:
    def __init__(self, score=0):
        self.score = score
        print(str(Player))

    def AddScore(self, score_addon):
        self.score = self.score + score_addon


def victory_check(current_player, result):
    if current_player.score + result > 99:
        print("Player {} has won with a score of {}".format(current_player.name, result + current_player.score))
        game_over()


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()


class Factory:
    @staticmethod
    def getPlayerType(player_type):
        if player_type == "human":
            return Player
        elif player_type == "computer":
            return ComputerPlayer


class Game:
    def __init__(self, player1, player2):
        """create a game instance"""
        self.plist = []
        self.turn_count = 1
        self.dice_count = 0
        self.random_seed = 0
        self.player1 = player1
        self.player2 = player2

    def game_state_tracker(self, dice_counter=0, turn_counter=0):
        self.turn_count += turn_counter
        self.dice_count += dice_counter

    def newGame(self):
        pass

    def gamePlay(self):
        while True:
            for player in range(0, 2):
                #TODO: need to pass in player list here or at Game class
                current_player = self.plist[player]
                print("_____________________________")
                print("|Now it is player {}'s turn  |".format(player))
                print("_____________________________")
                victory_check(current_player, result=0)
                self.gameRound(current_player)

    def gameRound(self, current_player):
        score_count, turn_end = 0, False
        dice = Dice()
        while turn_end is False:
            self.game_state_tracker(1, 0)
            result = dice.Roll()
            if result == 1:
                print("Player {},You rolled a 0 and your turn is over".format(current_player))
                return
            else:
                score_count += result
                victory_check(current_player, result=score_count)
                print(
                    "Player {}, it is your turn. Your score is {} points. You currently have a possible score of"
                    " {}".format(
                        current_player.name,
                        current_player.score, current_player.score + score_count))
                player_choice = None
                while player_choice is None:
                    player_choice = input(
                        'Please choose "r" to roll or "h" to hold and end your turn: '.format(current_player.name))
                    if player_choice == 'h':
                        current_player.AddScore(score_count)
                        print('{} ends their turn with {} points.'.format(current_player.name,
                                                                          current_player.score))
                        return
                    if player_choice == 'r':
                        continue
                    else:
                        player_choice = None


def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--playerint", default=2, help="Enter the amount of players in the game", type=int)
    parser.add_argument("--player1", default=Player, help="Enter if player1 will be a robot or a person", type=int)
    parser.add_argument("--player2", default=Player, help="Enter if player2 will be a robot or a person", type=int)
    args = parser.parse_args()
    return args.playerint, args.player1, args.player2


def game_over():
    while True:
        decision = input("play again? (y or n) :")
        if decision == 'y':
            main()
        if decision == 'n':
            print("goodbye!")
            exit()
        else:
            pass


def main():
    args = argparser()
    current = Game(Factory.getPlayerType(args[1]), Factory.getPlayerType(args[2]))
    current.newGame()
    current.gamePlay()


main()
