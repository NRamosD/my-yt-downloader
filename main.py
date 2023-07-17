import os
from pytube import YouTube
from pytube import Playlist

###########PARA UNA
yt = YouTube('https://www.youtube.com/watch?v=am13PJ-6-hY&list=PL7pkSK1xbGD6Gb_00CupzPrzIiWHiKS4W&index=34')
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

# playlist = Playlist('https://www.youtube.com/watch?v=stQ0xae350Y&list=RDstQ0xae350Y&start_radio=1&rv=stQ0xae350Y&t=6')
# # check for destination to save file
# print("Descargando tu música...")
# destination = "." 

# print(f"Cantidad de músicas: {len(playlist.video_urls)}")

# for video in playlist.videos:
#     music = video.streams.filter(only_audio=True).first()
#     out_file = music.download(output_path=destination)  
#     # save the file
#     base, ext = os.path.splitext(out_file)
#     new_file = base + '.mp3'
#     os.rename(out_file, new_file)

# print("All rigth!")