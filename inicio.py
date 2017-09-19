# Python's Libraries
import os

# Own's Libraries
from libtools.filesystem import Carpeta
from ocio import YouTuber

folder = Carpeta(
    os.path.abspath(os.path.join(os.getcwd(), 'downloads'))
)
you = YouTuber(folder)

you.get_Audio("https://www.youtube.com/watch?v=ysSvX21PYBs")
