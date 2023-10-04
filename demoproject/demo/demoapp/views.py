from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(request):
    return HttpResponse("WELCOME")
def about(request):
    return  render(request,'about.html')
def contact(request):
    return HttpResponse("contact here")
def detail(request):
    return  render(request,'detail.html')
def thanks(request):
    return HttpResponse("Thank You")
