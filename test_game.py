from unittest import TestCase

from game import Game
from game_result import GameResult


class TestGame(TestCase):
    def setUp(self):
        self.game = Game()
        super().setUp()

    def assert_illegal_argument(self, guessNumber):
        try:
            self.game.guess(guessNumber)
            self.fail()
        except TypeError:
            pass

    def test_exception_when_invalid_input(self):
        self.assert_illegal_argument(None)
        self.assert_illegal_argument("12")
        self.assert_illegal_argument("1234")
        self.assert_illegal_argument("12s")
        self.assert_illegal_argument("121")

    def test_return_solve_result_if_matched_number(self):
        self.game.question = "123"
        result: GameResult = self.game.guess("123")

        solved = True
        strikes = 3
        balls = 0

        self.assert_matched_number(balls, result, solved, strikes)

    def test_return_solve_result_if_unmatched_number(self):
        self.game.question = "123"
        result: GameResult = self.game.guess("456")

        solved = False
        strikes = 0
        balls = 0

        self.assert_matched_number(balls, result, solved, strikes)

    def assert_matched_number(self, balls, result, solved, strikes):
        self.assertIsNotNone(result)
        self.assertEqual(solved, result.get_solved())
        self.assertEqual(strikes, result.get_strikes())
        self.assertEqual(balls, result.get_balls())
