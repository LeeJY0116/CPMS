from django.shortcuts import render

# Create your views here.
def cpms_main(request):
    return render(request, 'index.html')

def cpms_login(request):
    return render(request, 'login.html')