import unittest
from lab1.task21.src.main import can_defend


class TestCanDefend(unittest.TestCase):

    '''Тест из примера 1'''
    def test_case_1(self):
        N = 6
        M = 2
        trump_suit = 'C'
        hand_cards = ['KD', 'KC', 'AD', '7C', 'AH', '9C']
        attack_cards = ['6D', '6C']
        result = can_defend(N, M, trump_suit, hand_cards, attack_cards)
        self.assertEqual(result, "YES")

    '''Тест из примера 2'''
    def test_case_2(self):
        N = 4
        M = 1
        trump_suit = 'D'
        hand_cards = ['9S', 'KC', 'AH', '7D']
        attack_cards = ['8D']
        result = can_defend(N, M, trump_suit, hand_cards, attack_cards)
        self.assertEqual(result, "NO")

    '''Игрок может покрыть все атакующие карты'''
    def test_case_3(self):
        N = 5
        M = 3
        trump_suit = 'S'
        hand_cards = ['6H', '7C', '9S', 'KH', 'QS']
        attack_cards = ['6S', '7S', '8S']
        result = can_defend(N, M, trump_suit, hand_cards, attack_cards)
        self.assertEqual(result, "NO")

    def test_case_4(self):
        N = 4
        M = 4
        trump_suit = 'D'
        hand_cards = ['6S', '7C', '9H', 'KH']
        attack_cards = ['6S', '7D', '8D', 'KD']
        result = can_defend(N, M, trump_suit, hand_cards, attack_cards)
        self.assertEqual(result, "NO")

    def test_case_5(self):
        N = 6
        M = 2
        trump_suit = 'S'
        hand_cards = ['6S', '7S', '9H', 'KH', 'QS', 'AH']
        attack_cards = ['6H', '7H']
        result = can_defend(N, M, trump_suit, hand_cards, attack_cards)
        self.assertEqual(result, "YES")


if __name__ == "__main__":
    unittest.main()
