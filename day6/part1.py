test_case = """Time:      7  15   30
Distance:  9  40  200"""

x = test_case.splitlines()
import bisect

races = list()
for line in x:
  times = list(filter(None, line.split(":").pop(1).split(" ")))
  int_times = [eval(i) for i in times]
  races.append(int_times)
print(races)

# lazy
# https://stackoverflow.com/questions/3196610/searching-a-sorted-list/49281681#49281681
def find_in_sorted_list(elem, sorted_list):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(sorted_list, elem)
    if i != len(sorted_list) and sorted_list[i] >= elem:
        return i
    return -1

total = 1

for i in range(len(races[0])):
  dist = races[1][i]
  time = races[0][i]
  new_rec = dist + 1
  p_dist_count = time - 1
  min_dist = time - 1
  if time%2 == 0:
    max_dist = int((time/2)**2)
  else:
    max_dist = int(((time+1)/2)**2 - ((time+1)/2))
  vals = list()
  for val in range(time//2):
    if val == 0:
      prev_val = 0
    else:
      prev_val = vals[val-1]
    vals.append(prev_val + time - (val*2 +1))
  max_idx = find_in_sorted_list(new_rec, vals)
  count = p_dist_count - max_idx*2
  #print(count)
  #print("vals: ",vals, new_rec, max_idx)
  #print(min_dist, max_dist)
  total = total*count
print(total)

