from pytube import YouTube
link = input('enter a link video')
file = YouTube(link).streams.first()
name = file.title
print(name)
path = file.download('download')