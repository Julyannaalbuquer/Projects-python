
import youtube_dl

link = [input('Link do vídeo:')]

with youtube_dl.YoutubeDL() as ydl:
    ydl.download(link)