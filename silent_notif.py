import subprocess

def play_spotify_playlist():
    script = '''
    tell application "Spotify"
        activate
        play track "https://open.spotify.com/playlist/1AruNTM8lMombNj5Vq9oVz?si=31dfa9cd7a344972"
    end tell
    '''
    subprocess.run(['osascript', '-e', script])

# Example usage
if __name__ == "__main__":
    play_spotify_playlist()
