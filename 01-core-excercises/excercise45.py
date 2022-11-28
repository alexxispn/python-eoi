class File:
    def __init__(self, path: str):
        self.path = path
        self.contents = []

    def add_content(self, *content: str):
        self.contents.extend(content)

    def info(self) -> str:
        return f'{self.path}  [size={self.size}B]'

    @property
    def size(self) -> int:
        return sum(len(letter) for letter in self.contents)


class MediaFile(File):
    def __init__(self, path: str, codec: str, geoloc: tuple, duration: int):
        super().__init__(path)
        self.codec = codec
        self.geoloc = geoloc
        self.duration = duration

    def info(self) -> str:
        return f'{super().info()}\nCodec: {self.codec}\nGeolocalization:' \
               f' {self.geoloc}' \
               f'\nDuration: {self.duration}s'


class VideoFile(MediaFile):
    def __init__(self, path: str, codec: str, geoloc: tuple, duration: int,
                 dimensions: tuple):
        super().__init__(path, codec, geoloc, duration)
        self.dimensions = dimensions

    def info(self) -> str:
        return f'{super().info()}\nDimensions: {self.dimensions}'


video = VideoFile('/home/python/vanrossum.mp4', 'h264', (23.5454, 31.4343), 487,
                  (1920, 1080))
video.add_content('audio/ogg', 'video/webm')
print(video.info())
