from unittest import TestCase

from game import Game


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

    def test_exception_when_input_is_none(self):
        self.assert_illegal_argument(None)

    def test_exception_when_input_length_is_unmatched(self):
        self.assert_illegal_argument("12")
