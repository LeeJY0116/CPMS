<<<<<<< HEAD
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Profile
=======
from django.db import models
from django.shortcuts import render, redirect
from .models import MyTicket, Profile
>>>>>>> 708934baab6a3b5f32aaf5fca91b7b60848011c9

# Create your views here.

def cpms_main(request):    
    return render(request, 'index.html', {'bool_logIO':False})

def cpms_signup(request):
    bool_nameCheck = False
    bool_idCheck = False

    if request.method == 'POST':
        nickname = request.POST['s_user_name']
        id = request.POST['s_userId']
        password = request.POST['s_userPw1']
        password_reconfirm = request.POST['s_user_Pw2']

        context = {
            'nickname':nickname,
            'id':id,
            'password':password,
            'password_reconfirm':password_reconfirm,
        }

        if Profile.objects.filter(userName=nickname):
            context['error_message'] = '해당 닉네임이 이미 존재합니다.'
            return render(request, 'signup.html', context)
        
        if Profile.objects.filter(userID=id):
            context['error_message'] = '해당 아이디는 이미 존재합니다.'
            return render(request, 'signup.html', context)

        if password != password_reconfirm:
            context['error_message'] = '비밀번호가 동일하지 않습니다.'
            return render(request, 'signup.html', context)
        
        Profile.objects.create(
            userName=nickname,
            userID = id,
            userPassword = password,
        )
        return redirect('trying_login')

    return render(request, 'signup.html')

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
<<<<<<< HEAD
    return render(request, 'index.html', {'bool_logIO':log_now, 'user':userName})
=======
    return render(request, 'index.html', {'bool_logIO':log_now, 'user':userName})

def cpms_ticket(request, user_name):
    try:
        user = Profile.objects.get(userName=user_name)
    except:
        return redirect('not_login')

    # 로그인했는지 확인하는 bool변수
    log_now = user.bool_logIO    
    if not log_now:
        return redirect('not_login')

    tickets = MyTicket.objects.filter(profile=user)
    context = {
        'userName' : user.userName,
        'userID' : user.userID,
        'tickets' : tickets,
    }

    return render(request, 'myTicket.html', context)

def cpms_create_ticket(request, user_name):
    try:
        user = Profile.objects.get(userName=user_name)
    except:
        return redirect('not_login')

    # 로그인했는지 확인하는 bool변수
    log_now = user.bool_logIO    
    if not log_now:
        return redirect('not_login')

    return render(request, 'createTicket.html')

def cpms_ticket_details(request, user_name):
    try:
        user = Profile.objects.get(userName=user_name)
    except:
        return redirect('not_login')

    # 로그인했는지 확인하는 bool변수
    log_now = user.bool_logIO    
    if not log_now:
        return redirect('not_login')

    return render(request, 'ticketdetails.html')
>>>>>>> 708934baab6a3b5f32aaf5fca91b7b60848011c9
