import collections
from random import choice


card=collections.namedtuple('card',['rank','suit'])  #namedtuple builds bundle classes with attributes only and no methods
class FrenchDeck:
    ranks=[str(n) for n in range(2,11)]+list('JKQA')
    suits='spade,diamond,club,heart'.split(',')


    def __init__(self) -> None:
        self.cards=[card(rank,suit) for suit in self.suits
                    for rank in self.ranks]
    
    def __len__(self):
        return len(self.cards)
        
    def __getitem__(self,position):
        return self.cards[position]
    
    
    

beer_card=card('7','hearts')
print(beer_card)

deck=FrenchDeck()
print(len(deck))

print(choice(deck))
print(deck[12::13])

for card in reversed(deck):
    print(card)

suit_values=dict(spade=3,heart=2,diamond=1,club=0)
def spades_high(card):
    rank_value=FrenchDeck.ranks.index(card.rank)
    return rank_value + len(suit_values) + suit_values[card.suit]


for card in sorted(deck,key=spades_high):
    print(card)