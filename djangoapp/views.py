from django.shortcuts import render
from django.http import HttpResponse

#home page.
def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request,'contact.html')
    # return HttpResponse("This is the contact page")

def about(request):
    return render(request,'about.html')


def blog(request):
    return render(request,'blog.html')