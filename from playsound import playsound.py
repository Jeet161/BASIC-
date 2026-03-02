from playsound import playsound
import time

# Lyrics stored in a list line-by-line
lyrics = [
    "Tum hi ho, ab tum hi ho",
    "Zindagi ab tum hi ho",
    "Chain bhi, mera dard bhi",
    "Meri aashiqui ab tum hi ho"
]

print("🎵 Playing song...")

# Play song in background (non-blocking)
import threading
threading.Thread(target=playsound, args=("song.mp3",), daemon=True).start()

# Print lyrics with delay
for line in lyrics:
    print(line)
    time.sleep(2)   # delay between lyrics