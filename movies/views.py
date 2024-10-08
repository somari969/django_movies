from django.shortcuts import render , HttpResponse , redirect
from .models import Movie
from . import forms

def movie_list(request):
    movies = Movie.objects.all().order_by('date')
    return render(request, template_name='movies/movie_list.html', context={'movies':movies})

def movie_detail(request, slug):
    movie = Movie.objects.get(slug=slug)
    return render(request, template_name='movies/movie_detail.html', context={'movie':movie})

# def movie_detail(request, slug):
#     movie = Movie.objects.get(slug=slug)
#     if request.method == "POST":
#         form = forms.CommentMovie(request.POST, request.FILES)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.comment = request.user
#             instance.save()
#             return redirect('movies:list')
#     else:
#         form = forms.CommentMovie()
#     return render(request, template_name='movies/movie_detail.html', context={'movie':movie})
