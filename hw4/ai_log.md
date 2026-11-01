# HW3 Part 4 – Save the results

AI Use: Stage 3 (Little helper)

You may have the AI write this function (about 10 lines) using the **[Stage 3 helper prompt](https://canvas.uw.edu/courses/1959879/pages/stage-3-little-helper-prompt)** (rules on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)). Copilot autocomplete stays off. With or without AI, write each step in `ai_log.md` **as you go**:

---

## 1. Try
*paste your own attempt or plan for the function, even if it doesn't work*

templates/results.html

<!DOCTYPE html>
<html>
<head><title>Results for {{ term }}</title></head>
<body>
  <h1>Results for "{{ term }}"</h1>

  {% if artworks %}
    <ul>
      {% for art in artworks %}
        <li>{{ art.title }} - {{ art.artist_title }} ({{ art.date_display }})</li>
      {% endfor %}
    </ul>
  {% else %}
    <p>No artwork found for "{{ term }}".</p>
  {% endif %}

  <a href="/">New search</a>
</body>
</html>
templates/home.html

<!DOCTYPE html>
<html>
<head><title>Art Search</title></head>
<body>
  <h1>Search the Art Institute</h1>
  <form action="/results" method="get">
    <input type="text" name="q" placeholder="e.g. cats" required>
    <button type="submit">Search</button>
  </form>
</body>
</html>
app.py

# imports
import requests


# get fields
FIELDS = "title,artist_title,date_display,image_id"


# saving results
def save_results(artworks, filename):
    with open(filename, "a") as f:
         
        for i in artworks:
            title = i.get("title") or "Unknown"
            artist = i.get("artist_title") or "Unknown"
            year = i.get("date_display") or "Unknown"
            f.write(f"{title} - {artist} ({year}) \n")

# user input
term = input("Search the Art Institute for: ")

url = "https://api.artic.edu/api/v1/artworks/search"
params = {"q" : term, "fields" : FIELDS}  
headers = {"AIC-User-Agent" : "HCDE310 student project"} 
response = requests.get(url, params=params, headers=headers)

# response checks   
if response.status_code != 200:
    print(response.status_code, "error", response.reason)
else:
    data = response.json()
    results = data["data"]

    if len(results) == 0:
            print(f'No artwork found for "{term}".')
    else:
        print(f'Found results for "{term}":')
        # for work in results:
            # print_artwork(work)
        save_results(results, "results.txt")




# html lines / building page
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/results")
def results():
    term = request.args.get("q", "")
    artworks = [
        {"title": "Water Lilies", "artist_title": "Claude Monet", "date_display": "1906"},
        {"title": "Nighthawks", "artist_title": "Edward Hopper", "date_display": "1942"},
        {"title": "American Gothic", "artist_title": "Grant Wood", "date_display": "1930"},
    ]

    return render_template("results.html", term=term, artworks=artworks)


if __name__ == "__main__":
    app.run(debug=True)





# for readme
# open http://127.0.0.1:5000
# Ctrl+C to stop

## 2. Chat (AI only)
*paste the whole conversation, your messages and the AI's replies in order, or a share link from the Share button (the link in your address bar only works for you). No AI? Write "No AI used."*

https://claude.ai/share/d185934a-6239-4538-92bb-0dd1118a51d8


## 3. Predict, then compare
*before you run the function, write what you think the file will contain for the sample data (`check.py` uses it) or for your search. Then paste what it actually contains. (A wrong prediction gets full credit. Don't edit it after running.)*

water lilies would have an image, but nighthawks would not
image_url : https://www.artic.edu/iiif/2/abc123,
image_url : https://www.artic.edu/iiif/2/


actual
[{'title': 'Water Lilies', 'image_id': 'abc123', 'image_url': 'https://www.artic.edu/iiif/2/abc123/full/400,/0/default.jpg'}, {'title': 'Nighthawks', 'image_id': None, 'image_url': None}]

## 4. What surprised me
*one or two sentences. Where were you wrong, or what did you learn? For example: "I thought a missing artist would print `none`, but `.get` gave the fallback `unknown`."*

I thought the AI would help with the html part, but the prompt did say python and I got an additional function to work with while I try to figure out the image situation for the html side.

## 5. Change one thing yourself
*once the function works, change one thing about it by hand, no AI. For example: a different line format (date first), a filename based on the search term, or sorted lines. Write what you changed and why, in one or two sentences.*

I changed the image width from 400px to 843px just to play with the image length. 