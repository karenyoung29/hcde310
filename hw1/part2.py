# HW1 Part 2: Lists and loops
# Run it:  python3 part2.py
# Your output must match expected/part2.txt exactly.

from artworks import titles

count = 1
for i in titles:
    print(f"{count}. {i}")
    count = count + 1

countTwo = 0
for j in titles:
    countTwo = countTwo + 1
print("Titles:", countTwo)

countThree = 0
for k in titles:
    if "a" in k.lower():
        countThree = countThree + 1
print(f'Titles with an "a": {countThree}')

longest = ""
for b in titles:
    if len(b) > len(longest):
        longest = b
print("Longest:", longest)
