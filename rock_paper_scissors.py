import inspect

import sys

from assertions import assert_equals

WINNER_HAND_1 = 1

WINNER_HAND_2 = 2

class Scissors:
    pass

class Paper:
    pass

class Rock:
    pass

SCISSORS = Scissors()
PAPER = Paper()
ROCK = Rock()


def rock_paper_scissors(hand1, hand2):
    if hand1 == ROCK and hand2 == PAPER:
        winning_hand = WINNER_HAND_2
    if hand1 == PAPER and hand2 == ROCK:
        winning_hand = WINNER_HAND_1
    if hand1 == SCISSORS and hand2 == ROCK:
        winning_hand = WINNER_HAND_2
    if hand1 == ROCK and hand2 == SCISSORS:
        winning_hand = WINNER_HAND_1
    return winning_hand


def test_rock_blunts_scissors():
    assert_equals(WINNER_HAND_1, rock_paper_scissors(ROCK, SCISSORS))


def test_scissors_blunted_by_rock():
    assert_equals(WINNER_HAND_2, rock_paper_scissors(SCISSORS, ROCK))


def test_paper_wraps_rock():
    assert_equals(WINNER_HAND_1, rock_paper_scissors(PAPER, ROCK))


def test_rock_is_wrapped_by_paper():
    assert_equals(WINNER_HAND_2, rock_paper_scissors(ROCK, PAPER))


def main():
    tests = [fn for (name, fn) in inspect.getmembers(sys.modules[__name__]) if
             name.startswith('test') and inspect.isfunction(fn)]
    for test in tests:
        test()


if __name__ == '__main__':
    main()
