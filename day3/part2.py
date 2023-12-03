test_case = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

x = test_case.splitlines()
print(x)
input = list()
nums = list()
chars = list()
chars_2 = list()

for line in x:
  temp_list = list()
  temp_nums = list()
  temp_chars = list()
  temp_chars_2 = list()
  for i in line:
    temp_chars_2.append(0)
    temp_list.append(i)
    if i == "*":
      temp_chars.append(1)
    else:
      temp_chars.append(0)
    if i.isdigit():
      temp_nums.append(i)
    else:
      temp_nums.append(None)
  input.append(temp_list)
  nums.append(temp_nums)
  chars.append(temp_chars)
  chars_2.append(temp_chars_2)

stars = 1
totals = dict()
y = 0
for ys in chars:
  x = 0
  for xs in ys:
    if xs:
      totals[stars] = list()
      try:
        chars_2[y-1][x-1] = stars
        chars_2[y-1][x] = stars
        chars_2[y-1][x+1] = stars
        chars_2[y][x-1] = stars
        chars_2[y][x+1] = stars
        chars_2[y+1][x-1] = stars
        chars_2[y+1][x] = stars
        chars_2[y+1][x+1] = stars
      except:
        pass
      stars += 1
    x = x+1
  y = y+1

y = 0
for ys in nums:
  x = 0
  temp_val = ""
  val_bool = False
  for xs in ys:
    if chars_2[y][x]:
      val_bool = chars_2[y][x]
    if xs:
      temp_val = temp_val + xs
      try:
        if nums[y][x+1] is None:
          if val_bool:
            try:
              totals[val_bool].append(int(temp_val))
              #print(temp_val)
            except:
              pass
          #print(temp_val)
      except:
        # This is really fucking gross
        if val_bool:
          try:
            totals[val_bool].append(int(temp_val))
            #print(temp_val)
          except:
            pass
    else:
      val_bool = False
      temp_val = ""
    x = x+1
  y = y+1

print(chars_2)
print(chars)
print(nums)
#print(totals)
total = 0
for k, v in totals.items():
  if len(v) == 2:
    ratio = v[0]*v[1]
    total = total + ratio
print(total)
