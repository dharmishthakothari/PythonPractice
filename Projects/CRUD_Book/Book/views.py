from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from .models import Book
from django.contrib import messages

def add_book(request):
    if request.method == "POST":
        id=request.POST['book_id']
        name=request.POST['book_name']
        publisher=request.POST['book_publisher']
        price=request.POST['book_price']
        obj=Book(book_id=id,book_name=name,book_publisher=publisher,book_price=price)
        obj.save()
        data = Book.objects.all()
        template = loader.get_template("AllBooks.html")
        context = {
            'data' : data,
        }
        messages.info(request,"Book added successfully!")

        return HttpResponse(template.render(context,request))
    return render(request,"add_book.html")

def read_book(request):
    data = Book.objects.all()
    template = loader.get_template("AllBooks.html")
    context = {
        'data' : data,
    }
    return HttpResponse(template.render(context,request))


def update(request,book_id):
    #records = Book.objects.all()
    #print(f"Records are {records}")
    data=Book.objects.get(book_id=book_id)
    template = loader.get_template("Update.html")

    context = {
        'data' : data,
    }
    
    print(f"Data is {context}")
    #return HttpResponse(template,render(context,request))
    return render(request,"Update.html",context)

def updateRecord(request,book_id):
    book_title=request.POST.get('title')
    book_publisher=request.POST.get('pub')
    book_price=request.POST.get('price')
    print(book_id,book_title,book_publisher,book_price)
    data=Book.objects.get(book_id=book_id)
    print(data)
    data.book_publisher=book_publisher
    data.book_name=book_title
    data.book_price=book_price
    data.save()
    data = Book.objects.all()
    template = loader.get_template("AllBooks.html")
    context = {
            'data' : data,
        }
    messages.info(request,"Book Updated successfully!")
    return HttpResponse(template.render(context,request))

def delete_book(request,book_id):
    data=Book.objects.get(book_id=book_id)
    data.delete()
    records = Book.objects.all()
    template = loader.get_template("AllBooks.html")
    context = {
        'data' : records,
    }
    return HttpResponse(template.render(context,request))
