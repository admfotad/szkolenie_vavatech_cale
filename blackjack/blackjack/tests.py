from nose.tools import assert_equal, assert_true, assert_false
from blackjack.hand import Hand, Card


def test_hard_hand():
    hand = Hand([
        Card('7', 'H'),
        Card('2', 'D'),
        Card('K', 'S'),
    ])
    assert_equal(hand.value, 19)
    assert_false(hand.soft)
    assert_false(hand.blackjack)


def test_soft_hand():
    hand = Hand([
        Card('A', 'H'),
        Card('5', 'D'),
    ])
    assert_equal(hand.value, 16)
    assert_true(hand.soft)
    assert_false(hand.blackjack)


def test_blackjack():
    hand = Hand([
        Card('A', 'H'),
        Card('Q', 'D'),
    ])
    assert_equal(hand.value, 21)
    assert_true(hand.soft)
    assert_true(hand.blackjack)
