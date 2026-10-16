# HW2 Part 4 – Your first functions
#
# In `part4.py`, turn code you already wrote into functions:
#
# 1. `works_by(artist, artworks)` → returns a list of titles by that artist, from the list you pass in
#    (an empty list if there are none)
# 2. `count_by_artist(artworks)` → returns your counting dictionary from Part 3
# 3. Replace each `TODO` docstring with one line saying what the function takes and what it returns
#
# Don't change the `print` lines at the bottom of `part4.py`. `check.py` uses them.

from artworks import artworks


def works_by(artist, artworks):
    """returns a list of titles by that artist, from the list you pass in (an empty list if there are none)"""
    titles = []
    for i in artworks:
        if i.get("artist", "Unknown") == artist:
            titles.append(i.get("title", "Unknown"))
    return titles



def count_by_artist(artworks):
    """returns a list of titles by that artist, from the list you pass in (an empty list if there are none)"""
    artistCount = {}
    for i in artworks:
        artist = i.get("artist", "Unknown")
        artistCount[artist] = artistCount.get(artist, 0) + 1
    return artistCount


print(works_by("Claude Monet", artworks))
print(works_by("Nobody", artworks))
print(count_by_artist(artworks))
