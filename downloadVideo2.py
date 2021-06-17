import pytube

video_url = input('Inserte la URL del video: ')
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download(r'D:\Descargas')