test_case = """Time:      7  15   30
Distance:  9  40  200"""

x = test_case.splitlines()
import bisect

races = list()
for line in x:
  t_vals = int(line.split(":").pop(1).replace(" ",""))
  races.append(t_vals)

# lazy
# https://stackoverflow.com/questions/3196610/searching-a-sorted-list/49281681#49281681
def find_in_sorted_list(elem, sorted_list):
    'Locate the leftmost value equal to or greater than x'
    i = bisect.bisect_left(sorted_list, elem)
    if i != len(sorted_list) and sorted_list[i] >= elem:
        return i
    return -1

total = 1

for i in range(1):
  dist = races[1]
  time = races[0]
  vals = list()
  for val in range(time//2):
    if val == 0:
      prev_val = 0
    else:
      prev_val = vals[val-1]
    vals.append(prev_val + time - (val*2 +1))
  max_idx = find_in_sorted_list(dist + 1, vals)
  count = time - 1 - max_idx*2
  total = total*count
print(total)

