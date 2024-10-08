from django.urls import path
from . import views
app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='list'),                 ## root Path - home page of movies App.
    path('<slug:slug>', views.movie_detail, name='detail')
]