from .base import *


SECRET_KEY = env('DJANGO_SECRET_KEY', default='or(qnmx*g(6wv#7)b+aq*v%t#gx31w*b2=tx()0tv#zfmv(vt-')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
