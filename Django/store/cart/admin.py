from django.contrib import admin
from .models import Item, Pedido

class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ( 'product', 'order', 'is_ordered', 'date_added', 'date_ordered', 'quantity')



class PedidoAdmin(admin.ModelAdmin):
    list_display = ('ref_code', 'owner', 'is_ordered', 'date_ordered')


admin.site.register(Item, ItemAdmin),
admin.site.register(Pedido, PedidoAdmin)
