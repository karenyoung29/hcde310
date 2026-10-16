# HW2 Part 1 – Model first (in `design.md`, no code)

---

## 1. Why is `artworks` a list of dictionaries and not one big dictionary? What would you lose or gain the other way?

artworks.py is a list of dictionaries so that we can associate the data with a more specific category rather than just the overarching label - artworks. If it is one big dictionary, the categories would also become data values and not keys to find the data.

## 2. Which fields are sometimes missing? What should the app show when they are?

Besides title, all the other fields are missing at least once in the dictionary. The app should show none to avoid an error when trying to grab the data.