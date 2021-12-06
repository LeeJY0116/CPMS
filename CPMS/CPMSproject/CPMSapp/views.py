from django.shortcuts import render, redirect
from .models import Profile

# Create your views here.

def cpms_main(request):    
    return render(request, 'index.html', {'bool_logIO':False})

def cpms_login(request):
    if request.method == 'POST':
        # 아이디 체크
        try:
            id = request.POST['user_id']
            user = Profile.objects.get(userID=id)
        except:
            return render(request, 'login.html', {'str_error':'존재하지 않는 ID입니다.'})
        # 비밀번호 체크
        try:
            password = request.POST['user_password']
            user = Profile.objects.filter(userID=id).get(userPassword=password)
        except:
            return render(request, 'login.html', {'str_error':'비밀번호가 잘못되었습니다.'})
        
        user.bool_logIO = True  # 로그인 변수 True로 변경
        user.save()     # Update후, save() 필수!
        user_name = user.userName   # 유저 닉네임
        return redirect('login_of_user_name', user_name)

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