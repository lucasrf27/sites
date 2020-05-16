from django.contrib import admin
from .models import Produto, Imagem, Modelo, Banner, BannerImages




class ModeloAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'publico', 'sexo', 'idade_min', 'tamanho', 'id')
    

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('model', 'nome', 'preco', 'id')
    

class ImagensAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'id')

class BannerAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo')


class BannerImagesAdmin(admin.ModelAdmin):
    list_display = ('bannering', 'imagem')


admin.site.register(Modelo, ModeloAdmin),
admin.site.register(Produto, ProdutoAdmin),
admin.site.register(Imagem, ImagensAdmin),
admin.site.register(Banner, BannerAdmin),
admin.site.register(BannerImages, BannerImagesAdmin),