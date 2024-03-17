from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Hello everyone, this is home page here..")
