from django.http import HttpResponse


def index(request):
    return HttpResponse("Django: inside polls app.")

def show_candidates(request):
    return HttpResponse("polls: showing candidates")

