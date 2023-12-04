test_case = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

x = test_case.splitlines()
#print(x)
input = list()

total = 0
cards = dict()
for card in x:
  card_score = 0
  card_num, card_scratch = card.split(":")
  num = int(card_num.strip("Card "))
  temp_card_wins, temp_card_vals = card_scratch.split("|")
  card_wins = temp_card_wins.split(" ")
  card_vals = temp_card_vals.split(" ")
  for w in card_wins:
    if w != '' and w in card_vals:
      card_score += 1
  cards[num] = dict()
  cards[num]["count"] = 1
  cards[num]["wins"] = list()
  while card_score > 0:
    cards[num]["wins"].append(num + card_score)
    card_score -= 1
print(cards)

def process_cards(deck, total):
  for c in range(len(deck)+1):
    if c == 0:
      continue
    for w in deck[c]["wins"]:
      deck[w]["count"] = deck[w]["count"] + deck[c]["count"]*1
    total = total + deck[c]["count"]
  return total

total = process_cards(cards, total)
print(cards)
print(total)
