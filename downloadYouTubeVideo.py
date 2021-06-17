from pytube import YouTube
url = input("URL: ")
yt = YouTube(url)
yt.title
yt.author
quality = input("HD 22(hd) or 18(low quality): ")
yt.streams.get_by_itag(quality).download(r"D:\Descargas")
