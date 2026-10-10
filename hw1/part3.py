# HW1 Part 3: Decisions
# Run it:  python3 part3.py
# Your output must match expected/part3.txt exactly.

from artworks import titles, years

cutoff = 1900  # works made before this year are "old"

index = 0
for i in titles:
    if years[index] > cutoff:
        print(i)
    index = index + 1

print()
indexTwo = 0
for k in titles:
    if years[indexTwo] < cutoff:
        print(f"{k}: old")
    else:
        print(f"{k}: modern")
    indexTwo = indexTwo + 1

print()
indexThree = 0
old = 0
new = 0
for k in titles:
    if years[indexThree] < cutoff:
        old = old + 1
    else:
        new = new + 1
    indexThree = indexThree + 1
print("Old:", old)
print("Modern:", new)