from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def sqpractice(request):
    
    
    Books=Book.objects.all()
    context={'Books':Books}
    return render(request, 'Form.html', context)

