from django.shortcuts import render, redirect
from .models import Profile

# Create your views here.

def cpms_main(request):    
    return render(request, 'index.html', {'bool_logIO':False})

def cpms_login(request):
    return render(request, 'login.html')

def cpms_main_login(request, user_name):
    try: 
        user = Profile.objects.get(userName=user_name)
    except:
        return redirect('not_login')

    # 로그인했는지 확인하는 bool변수
    log_now = user.bool_logIO
    userName = user.userName
    if not log_now:
        return redirect('not_login')
    return render(request, 'index.html', {'bool_logIO':log_now, 'user':userName})