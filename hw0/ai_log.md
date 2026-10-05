# AI log

## HW0: Class 1, build an app with AI

Paste every prompt you sent, in order, with the AI's replies. A share link to the chat is fine too, but paste the prompts here either way. Your thinking about it goes in `day1.md`.

**Share link (optional):**

### Prompt 1

```
Build a single-page interactive web app. It calls the Art Institute of Chicago API (https://api.artic.edu/api/v1/artworks/search) when the user searches or filters, and shows results with images. Keep it under ~150 lines. It's for university level student researchers who want to see how the perception of animals change based on artwork created in the years. My sketch is attached; follow it. Explain how the code works in plain language, section by section.
```

**AI's reply: I built the page from your sketch, but I didn't publish it as a hosted artifact. Published pages can't make network requests to other sites or load outside images, so the Art Institute of Chicago API call and the artwork photos would both fail silently there. Instead it's a single ~130-line HTML file. Open it in a browser on your computer, or put it on your own site, and the API works. I haven't tested it against the live API.

The API request format is written from my memory of the museum's documentation, so run one search to confirm it returns results.

How the code works

Layout (HTML and CSS). This follows your sketch from top to bottom:

Search bar: a text box reading "animal, year…", a Search button, and a ✕ clear button.
Year slider: it runs from "present" on the left to 1678 on the right. A label above it shows the centre year and the 50-year window around it.
Artwork card: one framed image with ‹ › arrows on either side, and caption lines (title, artist, date and place) underneath.
Styling: a soft gallery-wall grey with one teal accent, and dark mode follows your device setting.

Setup.

API and IIIF hold the search address and the image-server address.
HALF = 25 means each search covers the chosen year ± 25 years.
results holds the artworks found, and i is the one currently on screen.

Slider to year. The slider stores a number from 0 to 348, meaning "years before now". The year is 2026 − slider value, so the left end is today and the right end is 1678. updateLabel redraws the "c. 1850 (1825–1875)" text as you drag.

Searching (search).

It reads the search box. If you typed a four-digit year, such as "horse 1850", it moves the slider to that year and treats the rest as the animal.
It sends the museum one request with the animal word plus three filters: the artwork's start date falls inside your window, it has an image, and it's public domain, so the image is free to display.
If you search again before the last request finishes, the old request is cancelled, so slow replies can't overwrite newer ones.
On failure it shows a plain error message, and an empty result shows a hint to widen the era or change the animal.

Showing one artwork (show).

It builds the image address from the artwork's image_id, then writes the title, artist, date and place into the caption.
Captions are inserted as plain text, so odd characters in museum data can't break the page.
The arrows grey out at the first and last result, and a status line reads "3 of 40".

Controls.

Enter or Search runs a search, and releasing the slider re-searches if there's text in the box.
‹ › and the left and right arrow keys step through results.
✕ resets everything.
For your research use

Comparing the same animal at 1700, 1800 and 1900 is the intended workflow. Only public-domain works appear, which favours older pieces. Some sketch details were hard to read, such as the "1678" end label, so please check that against what you meant.

If you'd rather have a hosted link, I can build a version that ships a few pre-saved example results instead of live search. It would publish fine, but it wouldn't search in real time. Would you like that?**

### Prompt 2

```
when the user searches for an animal, locate art in the database with that animal and arrange them in reverse chronological starting with present day
```

**AI's reply: I updated animals-in-art.html so a search now returns artworks of that animal in reverse chronological order, newest first. The file is still about 134 lines, and I haven't tested it against the live API.

What changed in the code

Search. The request now asks the museum for up to 100 matching public-domain artworks with images, sorted by start date from newest to oldest. The page sorts them again itself, so the order holds even if the API's sorting behaves differently. The first artwork you see is the most recent one, and the ‹ › arrows step backward through time.
Filters. The ±25-year window is gone. Everything the museum holds for that animal is now in the list, and the status line reads "1 of 87, newest first".
Slider. It now scrubs through the sorted list instead of filtering it. Drag it toward 1678 and the card jumps to the first artwork from that year or earlier. When you use the arrows, the slider moves to match the artwork on screen.
Typed years. Typing "horse 1850" still works. It searches for horse, then jumps to the first result from 1850 or earlier.

Limits to know about

The API returns at most 100 artworks per request, so a common animal like "horse" may show only the newest 100. If a search reaches 100 results, tell me and I'll add a "load older works" button that fetches more.
The slider stops at 1678, so anything older is reachable with the arrows but not the slider.
The ordering uses the artwork's start date. A work dated "1850–1900" sorts as 1850.

The same limitation as before applies: this has to be opened locally or hosted on your own site, because a published artifact page can't call the museum's API.**

### Prompt 3

```
insert comments in the code explaining how the code works
```

**AI's reply: I added comments throughout animals-in-art.html. The behavior is unchanged.

HTML: Four numbered comments mark the page sections in the order they appear in your sketch: search bar, year slider, artwork viewer with arrows, and the status line.
CSS: Short comments cover the colour settings at the top, dark mode, the layout of the artwork row, and the phone-screen adjustments.
JavaScript: The script has labelled sections: settings and shared state, slider helpers, searching, drawing the current artwork, wiring up the controls, and startup. Inside them, comments explain each API filter, why results are sorted a second time, and why captions are inserted as plain text.

The file is now about 184 lines, up from 134 because of the comments. You originally asked for under roughly 150, so the working code is still around that size and the extra is commentary. If you need to stay under the limit with comments included, I can trim the CSS down.**
