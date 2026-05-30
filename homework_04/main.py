from media import File, VideoFile, AudioFile, ImageFile, FileFormat
from utils import convert
from storage import S3Storage, SMBShare
from pathlib import Path
from datetime import time

FileFormat.add("mkv")
# FileFormat.add("jpg")
# FileFormat.add("txt")

video_file = VideoFile(
    name="movie.mkv",
    format=FileFormat.MKV,
    resolution=(1920, 1080),
    duration=time(0, 2, 0),
    color_depth=24,
)
video_file.properties = {"frame_rate": 110}

audio_file = AudioFile(
    name="song.mp3", format=FileFormat.MP3, bitrate=192000, duration=time(0, 3, 45)
)
jpg_file = ImageFile(
    name="picture.jpg", format=FileFormat.JPG, resolution=(1920, 1080), color_depth=24
)

print(video_file.properties)
print(audio_file.properties)
print(jpg_file.properties)

gif_file = convert(jpg_file, new_format=FileFormat.GIF)
print(gif_file.properties)

for storage in [SMBShare]:
    storage = storage()
    path: Path = Path(
        r"C:\Users\Dev\Desktop\2d054fbb455711f0bfc416362698692b_1.jpg"
        # r"C:\Users\Dev\Desktop\test.txt"
    )
    file: File = storage.read(path)
    storage.save(path, video_file)
