import os
import pytube
from moviepy.editor import *

run = 1

while run != 0:
    url = input("Input link to video: ")
    path = input("Input path to download: ")
    choice = input("Choose option\n1. Download video\n2. Download audio\n3. Download video and audio\n")

    yt = pytube.YouTube(url)
    if choice == "2" or choice == "3":
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=path)
        base, ext = os.path.splitext(out_file)

        # Convert to mp3
        FILETOCONVERT = AudioFileClip(out_file)
        FILETOCONVERT.write_audiofile(base+".mp3")
        FILETOCONVERT.close()
        os.remove(out_file)
        print(f"Audio downloaded.\nPath: {base}.mp3")

    if choice == "1" or choice == "3":
        video = yt.streams.get_highest_resolution()
        out_file = video.download(output_path=path)
        print(f"Video downloaded.\nPath: {out_file}")
    run = input("To exit input 0\n")