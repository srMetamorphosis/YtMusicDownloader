from pytube import YouTube
from moviepy.editor import *


url = {'link placeholder'}

yt = YouTube(url)

#Get the audio stream
audio_streaam = yt.streams.filter(only_audio=True, file_extension='webm').first()

#Print video title
print("Title: ", yt.title)

#Download audio stream
download_path = audio_streaam.download(output_path='Path Placeholder')

# Convert downloaded audio to mp3

audio_clip = AudioFileClip(download_path)
mp3_path = download_path.replace(".webm", ".mp3")
audio_clip.write_audiofile(mp3_path, codec='mp3')

#Remove origial .webm file for storage purposes after conversion
import os
os.remove(download_path)

print(f"Audio saved as ${mp3_path}")






