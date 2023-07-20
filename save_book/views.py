from django.shortcuts import render
from django.http import HttpResponse
from sqpractice.models import Book
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


def save_book(request):
    return render(request, "Display.html")

def add_form(request):
    return render(request, "Form.html")

def add(request):
    if request.method == 'GET':
        try:
            author = request.GET['author']
            title = request.GET['title']
            publication_date = request.GET['publication_date']

            book = Book(author=author, title=title, publication_date=publication_date)
            book.save()
            content="Added Successfully"
            context={'content':content}
            return render(request, "Information.html", context)
        
        except Exception as e:
           content="Not added"
           context={'content':content}
           return render(request, "Information.html", context)
    else:
        content="Not a suitable method"
        context={'content':content}
        return render(request, "Information.html", context)

def update(request):
    return HttpResponse("Updated")

def delete(request):
    if request.method == 'POST':
        try:
            
            category = request.POST['category']
            del_value=request.POST['details']
            if category == 'author':
                book = Book.objects.filter(author=del_value)
                print(book)
            elif category == 'title':
                book = Book.objects.filter(title=del_value)
            elif category == 'publication_date':
                book = Book.objects.filter(publication_date=del_value)
            
            
            if book.exists():
           
                book.delete()
                content="Deleted Successfully"
                context={'content':content}
                return render(request, "Information.html", context)
            else:
                content="Match not found"
                context={'content':content}
                return render(request, "Information.html", context)
        except ValueError:
           
            content = "Invalid date format. Please use the format 'YYYY-MM-DD'."
            context={'content':content}
            return render(request, "Information.html", {'content': content})
            
        except Exception as e:
           content="Error Found"
           context={'content':content}
           return render(request, "Information.html", context)
    else:
        content="Not a suitable method"
        context={'content':content}
        return render(request, "Information.html", context)


def delete_form(request):
    return render(request, 'Delete.html')

def view(request):
    Books=Book.objects.all()
    context={'Books':Books}
    return render(request, 'view.html', context)


def validate(request):
    try:
        
        email=request.GET['email']
        EmailValidator(email)        
        return HttpResponse("Everything is okay")
    except ValidationError as e:
   
        return HttpResponse("Not fine")

def validate_form(request):
    return render(request,'Form1.html')