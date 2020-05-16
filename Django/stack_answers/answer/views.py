from django.shortcuts import render, redirect
from .forms import ProductName
from .models import Product_sell_create

def form_test(request):
    if request.method == 'POST':
        form = ProductName(request.POST)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.save()
            return redirect('../thanks')
    else:
        form = ProductName()

        context = {
            'form': form
        }

        return render(request, "form_test.html", context)


def thanks_view(request):
    query = Product_sell_create.objects.all()
    return render (request, 'thanks.html', {'query' : query})