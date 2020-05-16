from django.core.management.base import BaseCommand
from c2vconfig.models import MP4


class Command(BaseCommand):
    file_name = ['nome.txt', 'artista.txt', 'url.txt']


    @classmethod
    def handle(cls, *args, **kwargs):
        with open(cls.file_name[0]) as file1, open(cls.file_name[1]) as file2, open(cls.file_name[2]) as file3:
            for data in zip(file1, file2, file3):
                nome, artista, url = data
                row = MP4(
                    nome=nome,
                    url=url,
                    artista=artista,
                    )
                row.save()
                print('ok')
                
        
        
        '''
        counter = 0
        for row in range(40):
            counter += 1 
            with open(cls.file_name[0]) as file:
                for linha in file:
                    nome = linha

            with open(cls.file_name[1]) as file:
                for linha in file:
                    artista = linha

            with open(cls.file_name[2]) as file:
                for linha in file:
                    url = linha
        
            row = MP4(
                nome=nome,
                url=url,
                artista=artista,
                id=MP4.objects.latest('id').id + 1
                )

            row.save()

                # with open('nomes.txt', 'urls.txt') as file:#
                    # for row in file:#
                    #    nome = row#
                    #    url = row#

            print('OK')
'''