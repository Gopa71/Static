from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'index.html')
def contact(req):
    return render(req,'contact.html')
def dest(req):
    return render(req,'destinations.index')
def news(req):
    return render(req,'news.html')
def elements(req):
    return render(req,'elements.html')