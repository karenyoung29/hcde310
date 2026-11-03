# app.py: the routes for the books app.
# SKELETON: the whole path works (form → /results → results page) with fake data.
# Next: replace one piece at a time, and commit each time something works.
from flask import Flask, render_template, request   # request (Flask), not requests!
from api import get_books
from api import get_books_real

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/results")
def results():
    # 1. Read the search term from the form
    author = request.args.get("author_search", "")

    # 2. Empty input? → home page + message (check BEFORE calling the API)
    if author == "":
        return render_template("home.html", message="Please type something to search for.")
    # 3. Call the API (fake data for now)
    books = get_books_real(author)

    # 4. API error? (get_books returned None) → home page + message
    if books is None:
        return render_template("home.html", message="Something went wrong reaching the API, try again.", author=author)

    # 5. No results, or nothing useful to show? → home page + message
    if len(books) == 0:
        return render_template("home.html", message=f"No books found for \"{author}\". Try a different spelling or name.",
                               author=author)
    # 6. Otherwise → results page
    return render_template("results.html", books=books, author=author)
