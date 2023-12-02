test_case = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

x = test_case.splitlines()
print(x)
total = 0
for line in x:
  print(line)
  line = line.strip("abcdefghijklmnopqrstuvwxyz")
  print(line)
  temp = line[0] + line[-1]
  print(temp)
  total = total + int(temp)
print(total)
