DRAW = 0
WINNER_HAND_1 = 1
WINNER_HAND_2 = 2


class Hand:
    def decide_winner(self, hand2):
        if self == hand2:
            return DRAW
        if self.wins_against == hand2:
            return WINNER_HAND_1
        else:
            return WINNER_HAND_2


SCISSORS = Hand()
PAPER = Hand()
ROCK = Hand()
SCISSORS.wins_against = PAPER
PAPER.wins_against = ROCK
ROCK.wins_against = SCISSORS

def rock_paper_scissors(hand1, hand2):
    return hand1.decide_winner(hand2)