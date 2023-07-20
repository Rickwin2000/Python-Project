from django.urls import path
from .import views




urlpatterns = [
    path('',views.save_book, name='save_book'),
    path('add/',views.add, name='add'),
    path('update/',views.update, name='update'),
    path('delete/',views.delete, name='delete'),
    path('view/',views.view, name='view'),
    path('add_form/',views.add_form, name='add_form'),
    path('delete_form/',views.delete_form, name='delete_form'),
    path('validate/',views.validate, name='validate'),
    path('validate_form/',views.validate_form, name='validate_form')
    ]
