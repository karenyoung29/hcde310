What:
KTRENZ is a free API with data on K-pop. You can search up artists by name, get an artist's AI citation with 7d momentum and tracking releases, get trending artists, and how much reacha a release gets. The API provides 4 GET endpoints and responses are JSON. A designer might care if they are building something relating to kpop and they can gather data on Naver and Youtube trends on artists and latest comebacks. This API is helpful for comeback trackers and trending rankings.

Setup:
- Install requests: pip install requests.
- No API key or sign-up is needed for the public tier of this API.


Working Example (AI was used to help write a working example, results are from my own terminal):
print(f"{a['name']} ({results[0].get('name_native', '')})")
print(f"  Naver search score:     {d.get('naver_search')}")
print(f"  YouTube views:          {d.get('youtube'):,}" if d.get("youtube") else "  YouTube views:          n/a")
print(f"  7-day momentum:         {d.get('momentum_7d_pct')}%")
print("  Latest coverage:")
for rel in (a.get("releases") or [])[:3]:
    print(f"    {rel['date']}  {rel['title']}")

Results:
RESCENE (리센느)
  Naver search score:     91
  YouTube views:          21,595,983
  7-day momentum:         -14%
  Latest coverage:
    2026-09-24  Circle Chart Week 38: Young Tak, RESCENE, HUNTR/X, aespa top the charts
    2026-10-06  RESCENE holds K탑스타 Best Rookie top spot for 4 straight weeks ahead of Nov. 3 mini album 'PULSE'
    2026-09-18  RESCENE confirms November 3 album release, their first new original music in 7 months

Gotchas:
Rate Limit: There is a fair-use daily cap per IP, higher-volume use would require a licensed key.

Data: This API only contains Naver and Youtube streams, missing data from Spotify, Instagram, and other platforms.

Design Angle:
One project idea could be fans tracking comebacks for multiple groups to order their streams based on what comes first. One ethical consideration could be emphasizing where the data comes from, as rankings play a huge part in the kpop community and fans often have opinions on who #1 is.


