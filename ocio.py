
# Thrid Party Libraries
import pafy


class YouTuber(object):

    def __init__(self, _folder):
        self.download_folder = _folder

    def get_Audio(self, _url):
        video = pafy.new(_url)
        audio = video.getbestaudio()
        audio.download(self.download_folder.abspath)
        print video.audiostreams
        print audio.bitrate

    def get_Video(self, _url):
        video = pafy.new(_url)
        archivo = video.getbest()
        archivo.download(self.download_folder.abspath)
