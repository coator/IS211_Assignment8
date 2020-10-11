import main
import unittest


class TestGame(unittest.TestCase):

    def test_game_player_types(self):
        """Intitializes game and checks for bad player inputs"""
        g = main.Game(2, )

"""AttributeError: 'NoneType' object has no attribute 'score'"""


"""    def test_game_run(self):
        g = main.Game(player_amount=2)"""

if __name__ == '__main__':
    unittest.main()

