from django.core.management.base import BaseCommand
from c2vconfig.models import MP4

#TENTAR PASSAR ARTISTAS E URL POR UMA LISTA#


def generate_nome():
    with open('nome.txt')as file:
        for rows in file:
            nome = rows
    return nome


def generate_url():
    with open('url.txt')as file:
        for row in file:
            url = row
    return url


def generate_artista():
    with open('artista.txt')as file:
        for rows in file:
            artista = rows
    return artista



class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name', type=str, help='ok')

    def handle(self, *args, **kwargs):
        nome = generate_nome()
        url = generate_url()
        artista = generate_artista()
        
        mp4 = MP4(
            nome=nome,
            url=url,
            artista=artista,
            )

        mp4.save()

        # with open('nomes.txt', 'urls.txt') as file:#
            # for row in file:#
            #    nome = row#
            #    url = row#

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
