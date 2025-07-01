from django.http import HttpResponse


def index(request):
    return HttpResponse("DevOpse Operation Second ")