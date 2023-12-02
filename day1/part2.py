star_two_test_case = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

x = star_two_test_case.splitlines()

nums = list(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])
total = 0

for line in x:
  print(line)
  spelled = dict()
  for val, num in enumerate(nums):
    try:
      spelled[line.index(num)]=val+1
      spelled[line.rfind(num)]=val+1
    except:
      pass
  print(spelled)

  temp_first_val = "0"
  temp_second_val = "0"
  temp_idx = 0
  while temp_first_val == "0":
    if line[temp_idx].isdigit():
      temp_first_val = line[temp_idx]
      break
    try:
      if temp_idx > min(list(spelled.keys())):
        temp_first_val = str(spelled[min(list(spelled.keys()))])
        break
    except:
      pass
    temp_idx+=1
  
  temp_idx = len(line)-1
  while temp_second_val == "0":
    if line[temp_idx].isdigit():
      temp_second_val = line[temp_idx]
      break
    try:
      if temp_idx < max(list(spelled.keys()))+1:
        temp_second_val = str(spelled[max(list(spelled.keys()))])
        break
    except:
      pass
    temp_idx-=1
  temp = temp_first_val + temp_second_val
  print(temp)
  total = total + int(temp)
print(total)
