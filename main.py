from pytube import YouTube
link = input('enter a link vedeo')
file = YouTube(link).streams.first()
name = file.title
print(name)
path = file.download('download')