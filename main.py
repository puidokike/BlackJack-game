import random


class Card:
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank

    @property
    def points(self):
        point_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
                'K': 10, 'A': 11}
        return point_map[self.rank]

    def __repr__(self):
        return f'{self.suite}{self.rank}'


class Deck:
    suites = ['♦', '♥', '♣', '♠']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    cards = []
    for suite in suites:
        for rank in ranks:
            cards.append(Card(suite, rank))

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def take_out(self):
        taken_card = self.cards.pop()
        return taken_card

    def __repr__(self):
        return str(self.cards)


class Player:
    def __init__(self, deck):
        self.deck = deck
        self.cards = []

    @property
    def qty_of_aces(self):
        ace = 0
        for card in self.cards:
            if card.rank == 'A':
                ace += 1
        return ace

    @property
    def points(self):
        initial_points = 0
        for card in self.cards:
            initial_points += card.points
            if initial_points > 21:
                if self.qty_of_aces:
                    for i in range(self.qty_of_aces):
                        initial_points -= 10
                        if initial_points <= 21:
                            break
        else:
            return initial_points

    def check_gt_21(self):
        if self.points > 21:
            return True
        else:
            return False

    def draw(self):
        self.cards.append(self.deck.take_out())

    def __repr__(self):
        return self.cards


class Dealer(Player):
    def __init__(self, deck, player):
        self.deck = deck
        self.player = player
        self.cards = []

    def make_decision(self):
        if self.player.points < 21:
            if self.player.points > self.points:
                self.draw()
            else:
                pass

    def deal(self):
        self.player.draw()
        self.draw()
        self.player.draw()
        self.draw()


class Game:
    deck = Deck()
    player = Player(deck=deck)
    dealer = Dealer(deck=deck, player=player)

    def show_table(self, hidden_dealer_card):
        if hidden_dealer_card:
            print(f"Dealer's cards: [??, {self.dealer.cards[1]}]")
        else:
            print(f"Dealer's cards: {self.dealer.cards}, {self.dealer.points} points")
        print(f"Player's cards: {self.player.cards}, {self.player.points} points")

    def play(self):
        self.deck.shuffle_deck()
        self.dealer.deal()
        self.show_table(hidden_dealer_card=True)

        while True:
            decision = input("Hit? (y/n): ")
            if decision == 'y':
                self.player.draw()
                self.show_table(hidden_dealer_card=True)
                if self.player.points > 21:
                    print('You Lost :(')
                    return
                elif self.player.points == 21:
                    print('Black Jack! You win!')
                    break
            else:
                break

        while True:
            self.dealer.make_decision()
            self.show_table(hidden_dealer_card=False)
            if self.dealer.points > 21:
                print('You win!')
            elif self.dealer.points > self.player.points:
                print('You lost!')
            elif self.dealer.points == self.player.points:
                print('Tie!')
            return


if __name__ == "__main__":
    game = Game()
    game.play()






