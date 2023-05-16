from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=d6mgALO9hUU')

print(yt.title)

print(yt.streams.filter(file_extension='mp4'))

stream = yt.streams.get_by_itag(18)
stream.download()

#pip install 
