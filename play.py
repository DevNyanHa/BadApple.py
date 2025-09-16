import json
import time
import sys
import os
import winsound

delay = 1 / 30 #fps

def playBadApple(path):
    os.system("cls")
    with open("./sampling/"+path, "r") as f:
        file = json.load(f)

    winsound.PlaySound("./assets/sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    for frame in file:
        sys.stdout.write("\033[H")
        for row in frame["value"]:
            print(row)
        sys.stdout.flush()
        time.sleep(delay)
