from django.contrib import admin
from .models import Parceiros, Servicos, Imagens

class ParceirosAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'nome', 'endereco', 'responsavel', 'tel', 'created_at', 'updated_at')

class ServicosAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'id', 'parceiro', 'preco', 'telefone', 'objetivo')

class ImagensAdmin(admin.ModelAdmin):
    list_display = ('servicos','id', 'imagem')


admin.site.register(Parceiros, ParceirosAdmin),
admin.site.register(Servicos, ServicosAdmin),
admin.site.register(Imagens, ImagensAdmin),