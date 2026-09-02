# convert video to mp3

import os
import subprocess

files = os.listdir("videos")
for file in files:
    # 1. Take part after '#', then take the first number before the space
    tutorial_number = file.split("#")[1].split()[0]

    # 2. Split on ' _ ' (not ' | ') and take the first part after vidssave.com
    file_name = file.split("vidssave.com ")[1].split(" _ ")[0]
    print( tutorial_number, file_name)

    
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])







