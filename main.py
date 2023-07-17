import os
import youtube_dl

# URL del video de YouTube
video_url = 'https://www.youtube.com/watch?v=N1EhXF1lskA'

# Opciones de configuración para la descarga
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': '%(title)s.%(ext)s',
}

# Descargar el audio del video de YouTube
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(video_url, download=False)
    video_title = info_dict.get('title', None)
    ydl.download([video_url])

# Renombrar el archivo descargado con la extensión .mp3
base, ext = os.path.splitext(video_title + '.mp3')
new_file = base + '.mp3'
os.rename(video_title + '.mp3', new_file)

print(video_title + " ha sido descargado correctamente.")
print("¡Todo listo!")