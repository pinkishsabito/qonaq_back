from django.http import HttpResponse


def default(request):
    return HttpResponse("birdene")
