import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "YOUR CLIENT ID"
CLIENT_SECRET = "YOUR CLIENT SECRET"
REDIRECT_URI = "http://127.0.0.1:8080/callback"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="playlist-read-private playlist-read-collaborative",
    ),
    requests_timeout=30,
    retries=5,
)

playlist_id = "58PZ6P2ms78M2NDBCutETn"

rows = []
offset = 0

while True:
    page = sp.playlist_items(
        playlist_id,
        limit=100,
        offset=offset,
        additional_types=["track"]
    )

    for playlist_item in page["items"]:
        track = playlist_item.get("item")
        if not track:
            continue

        artists = ", ".join(a["name"] for a in track.get("artists", []))
        album = track.get("album", {}).get("name", "")
        popularity = track.get("popularity", "")

        rows.append([
            "2025-05-01",
            len(rows) + 1,
            track.get("name", ""),
            artists,
            album,
            popularity
        ])

    if page["next"] is None:
        break

    offset += len(page["items"])

df = pd.DataFrame(
    rows,
    columns=["date", "position", "song", "artist", "album", "popularity"]
)

df.to_csv("france_top50.csv", index=False)

print("France Top 50 data saved successfully!")
print("Total rows:", len(df))

