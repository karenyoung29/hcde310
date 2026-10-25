# HW3 Part 4 – Save the results

AI Use: Stage 3 (Little helper)

Write a new function, `save_results(artworks, filename)`, that writes one line per artwork (title, artist, date) to a `.txt` file. Call it so every search saves its results. Then run `fetch.py` for real once, with a search you pick, and **commit the `.txt` file it made**: that's your proof the live call works.

You may have the AI write this function (about 10 lines) using the **[Stage 3 helper prompt](https://canvas.uw.edu/courses/1959879/pages/stage-3-little-helper-prompt)** (rules on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)). Copilot autocomplete stays off. With or without AI, write each step in `ai_log.md` **as you go**:

Done early? Add `sort_by_date(artworks)` too (not graded).

---

## 1. Try
*paste your own attempt or plan for the function, even if it doesn't work*
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
        


# TODO steps 4-5: loop over the results and print each one (reuse your HW2 printing code),
#                 print a default for null fields, and print a helpful message if there are no results

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
            title = i.get("title", "Unknown")
            artist = i.get("artist_title", "Unknown")
            year = i.get("year", "Unknown")
            f.write(f"{title} - {artist} ({year}) \n")

save_results(results, "results.txt")

## 2. Chat (AI only)
*paste the whole conversation, your messages and the AI's replies in order, or a share link from the Share button (the link in your address bar only works for you). No AI? Write "No AI used."*

https://claude.ai/share/99337256-5b62-4c0b-936d-62b9f9614219

## 3. Predict, then compare
*before you run the function, write what you think the file will contain for the sample data (`check.py` uses it) or for your search. Then paste what it actually contains. (A wrong prediction gets full credit. Don't edit it after running.)*

Prediction: 
Starry Night - Vincent van Gogh (1889)
Untitled - Unknown (Unknown)

Ran:
Starry Night - Vincent van Gogh (1889)
Untitled - Unknown (Unknown)

## 4. What surprised me
*one or two sentences. Where were you wrong, or what did you learn? For example: "I thought a missing artist would print `none`, but `.get` gave the fallback `unknown`."*

My order of the functions were wrong, and the computer ran into the code calling the function before it read the function code, causing the errors. I completely forgot about that order and the AI reminded me of this rule.

## 5. Change one thing yourself
*once the function works, change one thing about it by hand, no AI. For example: a different line format (date first), a filename based on the search term, or sorted lines. Write what you changed and why, in one or two sentences.*

I changed line 35 from get year to get date_display, since this was a code i copied from HW2, the key names were different so in the .txt file it kept showing the date as unknown and when I updated it to date_display, the code works as intended.
