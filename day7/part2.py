test_case = """32T3K 765
T55J5 684
KTJJT 220
KK677 28
QQQJA 483"""

x = test_case.splitlines()

hands = list()
for line in x:
  cards, bids = line.split(" ")
  hands.append([list(cards), int(bids)])
print(hands)

# Sort a list of hands in to their relevant hand types
# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456
def type_hands(hand_list):
  five_ok, four_ok, fh, three_ok, tp, op, hc = list(), list(), list(), list(), list(), list(), list()
  for hand in hand_list:
    hand_d = dict()
    for card in hand[0]:
        if card in hand_d:
          hand_d[card] += 1
        else:
          hand_d[card] = 1
    try:
      jcount = hand_d["J"]
    except:
      jcount = 0
    if jcount > 0 and jcount < 5:
      del hand_d["J"]
      hand_d[max(hand_d, key=hand_d.get)] += jcount
    print(hand_d)
    print(hand[0])
    set_hand = hand_d
    #print(set_hand)
    if len(set_hand) == 1: # all same value
      five_ok.append(hand)
    elif len(set_hand) == 2: # 4 of a kind or full house
      for c, v in hand_d.items():
        if v == 4:
          if "J" in hand_d.keys():
            five_ok.append(hand)
            break
          else:
            four_ok.append(hand)
            break
        if v == 3:
          fh.append(hand)
          break
    elif len(set_hand) == 3: # 3 of a kind or two pair
      twos = 0
      for c, v in hand_d.items():
        if v == 3:
          print(hand_d.keys())
          if "J" in hand_d.keys():
            four_ok.append(hand)
            break
          else:
            three_ok.append(hand)
            break
        if v == 2:
          twos +=1
          if twos == 2:
            tp.append(hand)
            break
    elif len(set_hand) == 4: # one pair
      op.append(hand)
    else:                    # high card
      hc.append(hand)
  return([five_ok, four_ok, fh, three_ok, tp, op, hc])

typed_hands = (type_hands(hands))

print(typed_hands)

card_rank = {"A":"A", "K":"B", "Q":"C", "J":"N", "T":"E", "9":"F", "8":"G", "7":"H", "6":"I", "5":"J", "4":"K", "3":"L", "2":"M"}
def rank(val):
  temp_string = ""
  for key in val[0]:
    temp_string = temp_string + card_rank[key]
  return temp_string

for type in typed_hands:
  if len(type) <= 1:
    continue
  type.sort(key=rank)

print(typed_hands)
def flatten_hands(hands):
  flat_hands = list()
  for type in hands:
    flat_hands += type
  return flat_hands

flat_hands = flatten_hands(typed_hands)
flat_hands.reverse()

total = 0
idx = 1
for hand in flat_hands:
  total += hand[1] * idx
  idx += 1

print(total)
