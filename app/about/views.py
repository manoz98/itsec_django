from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> this is About page. 2 </h1> ")