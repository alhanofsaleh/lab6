from django.shortcuts import render 
from django.http import HttpResponse

from .models import Book 


def complex_query(request):
    mybooks = Book.objects.filter(
        author__isnull=False,
        title__icontains='and',
        edition__gte=2
    ).exclude(price__lte=100)[:10]

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')  
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodules/index.html" , {"name": name})  #your render line
 
def index2(request, val1 = 0):   #add the view function (index2)
    return HttpResponse("value1 = "+str(val1))

def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodules/show.html', context)

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def index(request):
    return render(request, "bookmodules/index.html")
def list_books(request):
    return render(request, 'bookmodules/list_books.html')
def viewbook(request, bookId):
    return render(request, 'bookmodules/one_book.html')
def aboutus(request):
    return render(request, 'bookmodules/aboutus.html') 
def links(request):
    return render(request, 'bookmodules/links.html') 
def formatting(request):
    return render(request, 'bookmodules/formatting.html') 
def listing(request):
    return render(request, 'bookmodules/listing.html') 
def tables(request):
    return render(request, 'bookmodules/tables.html') 
def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodules/bookList.html', {'books':newBooks})

    return render(request, 'bookmodules/search.html') 

