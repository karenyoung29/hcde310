# HW3 Part 2 + Part 3 + Part 4
#
# Instructions: README.md in this folder (same as the assignment on Canvas).

import requests

FIELDS = "id,title,artist_title,artist_display,date_display,place_of_origin,artwork_type_title,medium_display"

# Functions go here (above the code that runs)
def print_artwork(i):
    title = i.get("title") or "Unknown"
    artist = i.get("artist_title") or "Unknown"
    year = i.get("date_display") or "Unknown"
    medium = i.get("medium_display") or "Unknown"
    place = i.get("place_of_origin") or "Unknown"
    kind = i.get("artwork_type_title") or "Unknown"

    print(f"{title} - {artist} ({year})")
    print(f"- {kind}, {medium}, from {place}")

def count_by_artist(artworks):
    """returns a list of titles by that artist, from the list you pass in (an empty list if there are none)"""
    artistCount = {}
    for i in artworks:
        artist = i.get("artist_title") or "Unknown"
        artistCount[artist] = artistCount.get(artist, 0) + 1
    return artistCount

def save_results(artworks, filename):
    with open("results.txt", "a") as f:
         
        for i in artworks:
            title = i.get("title") or "Unknown"
            artist = i.get("artist_title") or "Unknown"
            year = i.get("date_display") or "Unknown"
            f.write(f"{title} - {artist} ({year}) \n")



term = input("Search the Art Institute for: ")

url = "https://api.artic.edu/api/v1/artworks/search"      # TODO: the search URL from step 2
params = {"q" : term, "fields" : FIELDS}   # TODO: q (the search term) and fields (FIELDS)
headers = {"AIC-User-Agent" : "HCDE310 student project"} 
response = requests.get(url, params=params, headers=headers)

# TODO step 3: check response.status_code before you use the data
if response.status_code != 200:
    print(response.status_code, "error", response.reason)
else:
    data = response.json()
    results = data["data"]

    if len(results) == 0:
            print(f'No artwork found for "{term}".')
    else:
        print(f'Found results for "{term}":')
        for work in results:
            print_artwork(work)
        save_results(results, "results.txt")


# TODO steps 4-5: loop over the results and print each one (reuse your HW2 printing code),
#                 print a default for null fields, and print a helpful message if there are no results

