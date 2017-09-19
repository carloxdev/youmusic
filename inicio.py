# Python's Libraries
import os

# Own's Libraries
from libtools.filesystem import Carpeta
from ocio import YouTuber

folder = Carpeta(
    os.path.abspath(os.path.join(os.getcwd(), 'downloads'))
)
you = YouTuber(folder)

lista = [
    'https://www.youtube.com/watch?v=iAMkzH_dI2Y',
    'https://www.youtube.com/watch?v=UPYzQQEsW90',
    'https://www.youtube.com/watch?v=RA_90_hOBEg',
    'https://www.youtube.com/watch?v=4at9k0OD2yk',
    'https://www.youtube.com/watch?v=nWxFoucx9ug',
    'https://www.youtube.com/watch?v=wnJ6LuUFpMo',
    'https://www.youtube.com/watch?v=bQgJls7N3R4',
    'https://www.youtube.com/watch?v=JVWJbmZoLvU',
    'https://www.youtube.com/watch?v=HM0jL-WRwOc',
    'https://www.youtube.com/watch?v=YeVOQBq7hq0',
    'https://www.youtube.com/watch?v=jx6ZcYPX_5A',
    'https://www.youtube.com/watch?v=xBdD78Xml8U',
    'https://www.youtube.com/watch?v=YSrWL3QfXmw',
    'https://www.youtube.com/watch?v=QuZvZwnrbPI',
    'https://www.youtube.com/watch?v=YoDh_gHDvkk',
    'https://www.youtube.com/watch?v=sW7iupEcrC8',
    'https://www.youtube.com/watch?v=aDCcLQto5BM',
    'https://www.youtube.com/watch?v=di93b_q0wlk',
    'https://www.youtube.com/watch?v=IA1_NR4BxqQ',
    'https://www.youtube.com/watch?v=Eg7-3HZnGYs'
]

for l in lista:
    you.get_Audio(l)
