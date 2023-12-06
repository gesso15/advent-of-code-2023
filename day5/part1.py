test_case = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

x = test_case.splitlines()
print(x)
seeds = list()
seedtosoil = list()
soiltofert = list()
ferttowater = list()
watertolight = list()
lighttotemp = list()
temptohumid = list()
humidtoloc = list()
maps = [seeds, seedtosoil, soiltofert, ferttowater, watertolight, lighttotemp, temptohumid, humidtoloc]

map_idx = 0
for line in x:
  if line == "":
    map_idx += 1
    continue
  if map_idx == 0:
    temp_line = line.split(":")
    maps[map_idx] = temp_line
  else:
    maps[map_idx].append(line)
for map in maps:
  map.pop(0)
seeds = maps.pop(0)
for idx in range(len(maps)):
  for idx2 in range(len(maps[idx])):
    temp_map = maps[idx][idx2].split(" ")
    temp_map_i = list()
    for v in temp_map:
      temp_map_i.append(int(v))
    maps[idx][idx2] = temp_map_i
seeds = seeds[0].split(" ")
seeds.pop(0)

def use_map(num, mapl):
  out_num = None
  for map in mapl:
    source_l = list()
    dest_l = list()
    for itr in range(map[2]):
      source_l = map[1]+itr
      dest_l = map[0]+itr
      if num == source_l:
        return dest_l
  return num

print(seeds, maps)

seed_list = list()
for seed in seeds:
  val = seed
  for map in maps:
    val = use_map(int(val), map)
  seed_list.append(val)
print(seed_list)
print(min(seed_list))

