from django.forms import ModelForm
from .models import Produto


class AddForm(ModelForm):
    class meta:
        model = Produto
        fields = ['nome', 'preco', 'foto', 'year_in_school']
