Documentation

- First go to spotify and create a developer account:
  - https://developer.spotify.com/dashboard/login
- Login with your spotify account
- Create an application on the dashboard
- Save your Client Id and Client Secret for later.
- Go to your Edit Settings -> Redirect URIs.
  - add http://google.com/ and http://localhost:80/
  (I'm not sure which one works, so I added both)
- Install Poetry
  - https://python-poetry.org/docs/

(If the pyproject.toml doesn't exist)
- `poetry init`
  - use the auto dependency to download "spotipy" and "datetime"

TODO: I should just be able to give you the pyproject.toml file
and it should be fine for you to just run `poetry shell`

- Add some environment variables
  - export SPOTIPY_REDIRECT_URI=http://localhost:8080
  - export SPOTIPY_CLIENT_ID={Client ID}
  - export SPOTIPY_CLIENT_SECRET={Client Secret}
- `poetry shell`
- `python3 main.py`
