# HW3 Part 1 – Read the response first

AI Use: Stage 2 (Tutor)

Open `sample_response.json` (a saved Art Institute of Chicago search). In `notes.md`:

---

## 1. The total number of results is at `data["pagination"]["total"]`. What's the path to the first artwork's title?
data["data"][0]["title"]

## 2. Find 3 more fields you'd want to show a user, and their paths
Artist: data["data"][0]["artist_title"]
Origin: data["data"][0]["place_of_origin"]
Type of Art: data["data"][0]["artwork_type_title"]

## 3. Which fields are `null` for some works?
artist_title

## 4. Predict
*open `fetch.py` and read it, but don't change anything yet. What do you think will happen when you run it?*
I think it will import the necessary packages needed for what the code is intended to do. It currently only initializes variables and the functions are TODO, so I don't think anything will happen yet. 

## 5. Run it
*run `python3 fetch.py`. When it asks for a search term, type a word (like `cat`) and press Enter. What actually happened? Read the traceback bottom line first: what went wrong, and which line of your file caused it?*
It gives an exception that it is an invalid URL since it is missing https:// to make it a valid URL. Line 16 in the fetch.py document caused the error and various lines in the request package.    