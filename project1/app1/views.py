from django.shortcuts import render

# Create your views here.
name = "John"
age = 20
def any(request):
    return render(request,'app1\index.html')
