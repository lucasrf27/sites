from django.core.management.base import BaseCommand
from c2vconfig.models import MP4
from pprint import pprint

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):

        with open('test123.txt', 'r') as file:
            all_music = []
            for row in file:
                spl = row.split('-')
                all_music.append(spl)
            for music in all_music:
                if len(music) > 1:


                    song = MP4(
                        nome = music[0],
                        url = 'youtube.com',
                        imagem = None,
                        artista = music[1]
                    )
                    print('OK')
                    song.save()
