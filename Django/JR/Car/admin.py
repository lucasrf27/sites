from django.contrib import admin
from .models import Post, Images
from django.contrib import admin
from .models import Veiculos, Imagens


class VeicleAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'potencia', 'cor', 'preco', 'ano', 'created_time', 'updated_time')


class ImagensAdmin(admin.ModelAdmin):
    list_display = ('veicle', 'imagem')


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')


admin.site.register(Veiculos, VeicleAdmin),
admin.site.register(Imagens, ImagensAdmin),
admin.site.register(Post),
admin.site.register(Images, ImagesAdmin),
