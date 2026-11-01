# imports
import requests
from flask import Flask, render_template, request

# get fields
FIELDS = "title,artist_title,date_display,image_id"
URL = "https://api.artic.edu/api/v1/artworks/search"
HEADERS = {"AIC-User-Agent": "HCDE310 student project"}

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

params = {"q" : term, "fields" : FIELDS}  
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


# AI-written
def add_image_urls(artworks):
    """Takes a list of artwork dictionaries and returns the same list with an "image_url" added to each (None if no image_id)."""
    for art in artworks:
        art["image_url"] = None
        if art.get("image_id"):
            art["image_url"] = "https://www.artic.edu/iiif/2/" + art["image_id"] + "/full/843,/0/default.jpg"
    return artworks

print(add_image_urls([
    {"title": "Water Lilies", "image_id": "abc123"},
    {"title": "Nighthawks", "image_id": None},
]))
# AI written end

# for readme
# open http://127.0.0.1:5000
# Ctrl+C to stop


