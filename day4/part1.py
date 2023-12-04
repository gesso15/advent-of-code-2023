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
for card in x:
  card_score = -1
  total_card_score = 1
  card_num, card_scratch = card.split(":")
  num = card_num.strip("Card ")
  temp_card_wins, temp_card_vals = card_scratch.split("|")
  card_wins = temp_card_wins.split(" ")
  card_vals = temp_card_vals.split(" ")
  #print(card_num, card_wins, card_vals)
  for w in card_wins:
    if w != '' and w in card_vals:
      card_score += 1
  if card_score == -1:
    total_card_score = 0
  while card_score > 0:
    card_score -= 1
    total_card_score = 2*total_card_score
  total = total + total_card_score
print(total)
