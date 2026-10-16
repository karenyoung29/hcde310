# HW2 Part 3 – Counting with a dictionary
#
# In `part3.py`:
#
# 1. Build a dictionary counting works per artist, and print it: `{'Vincent van Gogh': 1, ...}`. A
#    work with no artist counts under `'Unknown'`.
# 2. Print the artist with the most works: `Most works: Claude Monet (2)`
#
# (This is the letter-counting pattern from Class 3, applied to art.)

from artworks import artworks

artistCount = {}
for i in artworks:
    artist = i.get("artist", "Unknown")
    artistCount[artist] = artistCount.get(artist,0) + 1
print(artistCount)

mostArtist = None
maxWork = -1

for j in artistCount:
    if artistCount[j] > maxWork:
        maxWork = artistCount[j]
        mostArtist = j
print(f"Most works: {mostArtist} ({maxWork})")