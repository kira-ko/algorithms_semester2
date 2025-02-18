import time

def can_defend(N, M, trump_suit, hand_cards, attack_cards):
    # Функция для преобразования карты в пару (ранг, масть)
    def parse_card(card):
        return card[0], card[1]

    hand_cards = [parse_card(card) for card in hand_cards]
    attack_cards = [parse_card(card) for card in attack_cards]

    # Разделяем карты на козырные и некозырные
    trump_cards = [card for card in hand_cards if card[1] == trump_suit]
    non_trump_cards = [card for card in hand_cards if card[1] != trump_suit]

    # Сортируем карты по старшинству (по рангу)
    rank_order = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    rank_to_value = {rank: idx for idx, rank in enumerate(rank_order)}

    def card_value(card):
        rank, suit = card
        return rank_to_value[rank]

    trump_cards.sort(key=card_value)
    non_trump_cards.sort(key=card_value)

    # Для каждой атакующей карты проверяем, можем ли мы ее отбить
    for attack_card in attack_cards:
        attack_rank, attack_suit = attack_card

        covered = False

        if attack_suit == trump_suit:
            # Если атакующая карта — козырная, она может быть покрыта только старшим козырем
            for i, card in enumerate(trump_cards):
                hand_rank, hand_suit = card
                if card_value(card) > card_value(attack_card):
                    trump_cards.pop(i)
                    covered = True
                    break
        else:
            # Если атакующая карта не козырная
            # 1. Попробуем покрыть картой той же масти, если старше
            for i, card in enumerate(non_trump_cards):
                hand_rank, hand_suit = card
                if attack_suit == hand_suit and card_value(card) > card_value(attack_card):
                    non_trump_cards.pop(i)
                    covered = True
                    break

            if not covered:
                # 2. Попробуем покрыть козырной картой
                for i, card in enumerate(trump_cards):
                    hand_rank, hand_suit = card
                    if card_value(card) > card_value(attack_card):
                        trump_cards.pop(i)
                        covered = True
                        break

        if not covered:
            return "NO"  # Если не нашли, чем покрыть, возвращаем "NO"

    return "YES"  # Если все карты отбиты


if __name__ == "__main__":
    start_time = time.time()

    with open("../txtf/input.txt", "r") as file:
        N, M, trump_suit = file.readline().split()
        N, M = int(N), int(M)
        hand_cards = file.readline().split()
        attack_cards = file.readline().split()

    result = can_defend(N, M, trump_suit, hand_cards, attack_cards)

    with open("../txtf/output.txt", "w") as file:
        file.write(result + "\n")

    end_time = time.time()
    print(f'Время выполнения: {end_time - start_time} секунд')