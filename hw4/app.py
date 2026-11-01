# imports
import requests


# get fields
FIELDS = "title,artist_title,date_display,image_id"

# search results 


# function for getting data



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


