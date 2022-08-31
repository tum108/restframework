from django.shortcuts import render
from .models import Category, Book


# Create your views here.
def index(request):
    categories = Category.objects.all()
    books = Book.objects.filter(published=True)

    categ_id = request.GET.get('categoryid')
    if categ_id:
        #ถ้ามีค่า category_id
        books = books.filter(category_id=categ_id)
    return render(request, 'book/index.html', {'categories': categories, 'books': books, 'categ_id': categ_id})
        

