from pytube import YouTube
url = input("URL: ")
yt = YouTube(url)
yt.title
yt.author
quality = input("Bitrate 140(128kbps), 249(50kbps), 251(webm 160kbps): ")
yt.streams.get_by_itag(quality).download(r"D:\Descargas")
