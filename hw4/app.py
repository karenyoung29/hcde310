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

# function for getting data
def get_artworks(term):
    url = "https://api.artic.edu/api/v1/artworks/search"
    params = {"q" : term, "fields" : FIELDS}
    headers = {"AIC-User-Agent" : "HCDE310 student project"}
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None

    # response checks
    if response.status_code != 200:
        print(response.status_code, "error", response.reason)
        return None                                  
    else:
        data = response.json()
        results = data["data"]

        if len(results) == 0:
                print(f'No artwork found for "{term}".')
        else:
            print(f'Found results for "{term}":')
            save_results(results, "results.txt")

        return results                                




# html lines / building page

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/results")
def results():
    term = request.args.get("q", "")

    if term == "":
        return render_template("home.html", message="Please type something to search for, like \"cats\" or \"Monet\".")

    artworks = get_artworks(term)

    if artworks is None:
        return render_template("results.html", term=term, artworks=[], error=True)

    add_image_urls(artworks)
    return render_template("results.html", term=term, artworks=artworks, error=False)


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

# AI written end

# for readme
# open http://127.0.0.1:5000
# Ctrl+C to stop


