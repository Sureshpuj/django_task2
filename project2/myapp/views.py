from django.shortcuts import render

# Create your views here.
def any(request):
    return render(request,'myapp\index.html')
