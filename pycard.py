import random, unittest
from collections.abc import Callable, Generator
from typing import Optional

# Returns cards in rank, suit order. Rank order
# is A, 2, 3, .. Q, K.
def fresh_deck() -> list[int]:
    return [c for c in range(52)]

# Rank is 1 for A, 11 for J, 12 for Q, 13 for K
def rank(c: int) -> int:
    return c // 4 + 1

# Suit is 0 for Clubs, 1 for Diamonds, 2 for Hearts, 3 for Spades.
def suit(c: int) -> int:
    return c % 4

def card(rank: int, suit: int) -> int:
    return (rank - 1) * 4 + suit

def contains_rank(cards: list[int], for_rank: int) -> bool:
    return any(rank(c) == for_rank for c in cards)

def remove_card(deck: list[int], card: int) -> bool:
    index = deck.index(card)
    if index == -1:
        return False
    last = deck.pop()
    deck[index] = last
    return True

def sample(
    ntrials: int,
    ncards: int,
    check: Callable[[list[int]], bool],
    deck: Optional[list[int]] = None,
) -> float:
    if not deck:
        deck = fresh_deck()
    nmatches = 0
    for _ in range(ntrials):
        drawn: list[int] = random.sample(deck, ncards)
        nmatches += int(check(drawn))
    return nmatches / ntrials

def draws(
    deck: list[int],
    ncards: int,
    start: int = 0,
) -> Generator[list[int]]:
    ndeck = len(deck)

    assert ncards >= 0
    assert ndeck - ncards >= 0
    if ncards == 0:
        yield []
        return None

    for i in range(start, ndeck - ncards + 1):
        first = deck[i]
        for rest in draws(deck, ncards - 1, start=i + 1):
            yield [first] + rest

def sample_all(
    ncards: int,
    check: Callable[[list[int]], bool],
    deck: Optional[list[int]] = None,
) -> tuple[int, int]:
    if not deck:
        deck = fresh_deck()
    nmatches = 0
    ntrials = 0
    for drawn in draws(deck, ncards):
        nmatches += int(check(drawn))
        ntrials += 1
    return nmatches, ntrials

# https://www.dataquest.io/blog/unit-tests-python/
class TestCalculations(unittest.TestCase):

    def test_rank(self):
        deck = fresh_deck()
        for r in range(1, 14):
            for i in range(4 * (r - 1), 4 * (r - 1) + 4):
                self.assertEqual(rank(deck[i]), r)
            self.assertEqual(sum(int(rank(c) == r) for c in deck), 4)

    def test_suit(self):
        deck = fresh_deck()
        for s in range(4):
            for i in range(s, 52, 4):
                self.assertEqual(suit(deck[i]), s)
            self.assertEqual(sum(int(suit(c) == s) for c in deck), 13)

    # XXX This test will accidentally fail with very low probability.
    def test_sample(self):
        p = sample(1000, 1, lambda d: rank(d[0]) == 0)
        self.assertTrue(abs(p - 1/13) < 0.1)

    def test_draws(self):
        deck = [0, 1, 2, 3]
        got = [d for d in draws(deck, 2)]
        expected = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
        self.assertEqual(got, expected)

if __name__ == '__main__':
    unittest.main()
