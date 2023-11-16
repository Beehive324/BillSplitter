import math

face_cards = ['Jack', 'Queen', 'King', 'Ace']
ranks = list(range(11, 15))
rank_fcard = {key: value for key, value in zip(face_cards, ranks)}

cards = input().split()  
n = len(cards)
count = 0
for i in range(6):
    cards = input().split()  
    for card in cards:
        if card in face_cards:
            count += rank_fcard[card]  
        elif card.isdigit() and not card.isalpha():  
            count += int(card)
print(count / 6)



