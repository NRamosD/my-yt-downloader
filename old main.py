import os
from pytube import YouTube
from pytube import Playlist

###########PARA UNA
yt = YouTube('https://www.youtube.com/watch?v=N5Vgm6-KO3o')
# extract only audio
video = yt.streams.filter(only_audio=True).first()
  
# check for destination to save file
print("Descargando tu música...")
destination = "." # str(input(">> ")) or '.'

 
out_file = video.download(output_path=destination)
  
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
  
print(yt.title + " has been successfully downloaded.")
print("All rigth!")





###########PARA MIX

"""playlist = Playlist('https://www.youtube.com/watch?v=N5Vgm6-KO3o&list=LL&index=1')
# check for destination to save file
print("Descargando tu música...")
destination = "." 

print(f"Cantidad de músicas: {len(playlist.video_urls)}")

for video in playlist.videos:
    music = video.streams.filter(only_audio=True).first()
    out_file = music.download(output_path=destination)  
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

print("All rigth!")"""