from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''

    return HttpResponse('Welcome to 6310742405 Arpapas Boonchaluay views!')

def item_view(request, item_id):
    context_data = {
        "item_id": item_id
    }
    return render(request, 'index.html', context=context_data)

def homepage(request):
    return render(request, 'homepage.html')

def category_view(request, category_id):
    context_data = {
        "category_id": category_id
    }
    return render(request, 'category.html', context=context_data)

def product_page(request, product_id):
    #product = Product.objects.get(id=product_id)#
    context_data = {
        "product_id": product_id
    }
    return render(request, 'product.html', context=context_data)

def checkout_page(request):
    return render(request, 'checkout.html')

def contact_page(request):
    return render(request, 'contact.html')