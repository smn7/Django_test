from django.shortcuts import render, get_object_or_404
from .models import WishList

# Create your views here.
def index(request):
    return render(request,'index.html',{})

def about(request):
    return render(request,'about.html',{"title":'wishlist_about'})

def list_page(request,pk):
    """
    function based view
    Class based view

    """
    print(pk)
    list_page = get_object_or_404(WishList,pk=pk)
    return render(request,'list_page.html',{'wishlist': list_page})