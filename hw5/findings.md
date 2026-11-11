# HW5 findings

## 1. Drawing: one search for "Monet"
image.jpeg

## 2. Two questions about the code
1. Does Exception take all exceptions into account?
2. What does .strip do?

## 3. Checks (4 or more, at least 2 as pytest tests)
| # | Check | Pass or fail |
|---|---|---|
| 1 | Checks if home page was found | pass |
| 2 | Checks if results are displayed correctly | pass |
| 3 | Checks if it can catch an empty string error without crashing | pass |
| 4 | Checks if a search for a value that does not exist returns a message | pass |

## 4. AI review
What it found that I missed: api.py line 8 - searches the full text for any mention of the input, so it is not just the artist title.
What it got wrong: None
Answers to my two questions, in my own words: Exception catches the most common errors, but not errors that involve exiting, like when I hit Ctrl + C to exit the python terminal. .strip() removes extra spaces at the beginning and end of the string in the entry.

## 5. My fix
What was wrong: The search functions searches for the instances of the input and not just artist title.
What I changed: Focused the search to filter only through artist_title 
How I checked it works: "Cat" now returns no artworks since there is no artist named Cat and before it would return artworks of cats
Commit before: params = {"q": artist, "fields": FIELDS, "limit": 10}  
Commit after: params = {"query[match][artist_title]": artist, "fields": FIELDS, "limit": 10}

## 6. Can we ship it? (100–150 words)
Yes or no, and why: 
Yes. The app is able to run basic functions, such as searching the artist and returning the artworks associated with that artist. The app is also able to catch errors, like an empty input by the consumer and return an helpful message that prompts the user to try again. There is even pytests that this app passed, checking that the functions work with different situations and this app is functional.

One thing my HW4 does better: Added a format to the results list of {title} - {artist} ({year})
One thing the AI's app does better: Cleaner code among the .py files and handles unknown in the HTML files.

AI use goes in `ai_use.md` (the five points on the AI Use Card).
