# import results
import requests

# get fields
FIELDS = "title,artist_title, date_display, image_id"

# search results 


# function for getting data



# saving results
def save_results(artworks, filename):
    with open("results.txt", "a") as f:
         
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
        for work in results:
            print_artwork(work)
        save_results(results, "results.txt")




# html lines / building page
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
   artworks = [{"title": "Lilies"},
               {"title": "Nighthawks"}]
   return render_template("home.html", artworks=artworks)



@app.route("/about")
def about():
   return "About us"




# for readme
# open http://127.0.0.1:5000
# Ctrl+C to stop


