from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> Hello IT Security Nepal <h1> new line check blah blah ")