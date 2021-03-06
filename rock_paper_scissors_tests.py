import inspect

import sys

from assertions import assert_equals
from rock_paper_scissors import WINNER_HAND_1, WINNER_HAND_2, DRAW, SCISSORS, PAPER, ROCK, rock_paper_scissors
from test_runner import run_tests


def test_rock_blunts_scissors():
    assert_equals(WINNER_HAND_1, rock_paper_scissors(ROCK, SCISSORS))


def test_scissors_blunted_by_rock():
    assert_equals(WINNER_HAND_2, rock_paper_scissors(SCISSORS, ROCK))


def test_paper_wraps_rock():
    assert_equals(WINNER_HAND_1, rock_paper_scissors(PAPER, ROCK))


def test_rock_is_wrapped_by_paper():
    assert_equals(WINNER_HAND_2, rock_paper_scissors(ROCK, PAPER))


def test_rock_draws_with_rock():
    assert_equals(DRAW, rock_paper_scissors(ROCK, ROCK))


if __name__ == '__main__':
    run_tests(sys.modules[__name__])
