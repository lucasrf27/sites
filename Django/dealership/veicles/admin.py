from django.contrib import admin
from .models import Veiculos, Imagens, Componentes


class VeicleAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'potencia', 'cor', 'preco', 'ano', 'created_time', 'updated_time')


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('veicle', 'imagem')


class ComponentesAdmin(admin.ModelAdmin):
    list_display = ('veicle', 'componente')


admin.site.register(Veiculos, VeicleAdmin),
admin.site.register(Imagens, ImagesAdmin),
admin.site.register(Componentes, ComponentesAdmin),
