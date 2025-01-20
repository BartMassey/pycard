import random, unittest
from collections.abc import Callable
from typing import Optional

# Returns cards in rank, suit order. Rank order
# is A, 2, 3, .. Q, K.
def fresh_deck() -> list[int]:
    return [c for c in range(52)]

# Rank is 1 for A, 11 for J, 12 for Q, 13 for K
def rank(c: int) -> int:
    return c // 13 + 1

# Suit is 0 for Clubs, 1 for Diamonds, 2 for Hearts, 3 for Spades.
def suit(c: int) -> int:
    return c % 4

def sample(
    ntrials: int,
    ncards: int,
    check: Callable[[list[int]], bool],
    deck: Optional[list[int]] = None,
) -> float:
    if not deck:
        deck = fresh_deck()
    matches = 0
    for _ in range(ntrials):
        drawn: list[int] = random.sample(deck, ncards)
        matches += int(check(drawn))
    return matches / ntrials

# https://www.dataquest.io/blog/unit-tests-python/
class TestCalculations(unittest.TestCase):

    # XXX This test will accidentally fail with very low probability.
    def test_sample(self):
        p = sample(1000, 1, lambda d: rank(d[0]) == 0)
        self.assertTrue(abs(p - 1/13) < 0.1)

if __name__ == '__main__':
    unittest.main()
