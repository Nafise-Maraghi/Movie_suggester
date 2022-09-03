from django.http import HttpResponse
from django.shortcuts import render

from .models import Movies

import random


def suggestion(request):
    if request.method == "GET":
        random_pk = random.randrange(1, 1001)
        movie = Movies.objects.get(pk=random_pk)
        title = movie.title

        return HttpResponse(f"Lets watch  \"{title}\"")

    else:
        return HttpResponse("Only get method allowed!")
