from django.urls import path
from . import views




urlpatterns = [
    path('',views.api, name='api'),
    path('post/',views.post, name='post'),
    path('put/<id>',views.put,name='put')
]

