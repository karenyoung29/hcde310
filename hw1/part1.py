# HW1 Part 1: Strings
# Run it:  python3 part1.py
# Your output must match expected/part1.txt exactly.

from artworks import titles, artists, years

title = titles[0]
artist = artists[0]
year = years[0]

print(f"{title} ({year}) by {artist}")

print(title.upper(), len(title))

print("Bed" in title)