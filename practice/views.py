from django.shortcuts import render
from django.http import HttpResponse
from django.http import request
from .models import Details




# Create your views here.
def practice(request):
    ob1=Details()
    ob1.image='img1.jpg'
    ob1.title='Taj Mahal'
    ob1.description='Place in Delhi'
    
    ob2=Details()
    ob2.image='img2.jpg'
    ob2.title='Wayanad'
    ob2.description='Place in Kerala'
    
    ob3=Details()
    ob3.image='img3.jpg'
    ob3.title='Alappuzha'
    ob3.description='Place in Kerala'    
    
    obj=[ob1,ob2,ob3]
    
    return render(request, 'practice.html', {'obj':obj})

