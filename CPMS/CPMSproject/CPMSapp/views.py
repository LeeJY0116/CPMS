from django.db import models
from django.shortcuts import render, redirect
from .models import MyTicket, Profile

# Create your views here.

def cpms_main(request):    
    return render(request, 'index.html', {'bool_logIO':False})

def cpms_not_login(request):
    error_message = {
        'login_error' : '로그인이 필요한 서비스입니다.',
    }    
    # login_error = '로그인이 필요한 서비스입니다.'    
    return render(request, 'login.html', error_message)

def cpms_go_main(request):
    return redirect('not_login')

def cpms_go_main_login(request, user_name):
    return redirect('login_of_user_name', user_name)

def cpms_try_logout(request, user_name):
    user = Profile.objects.get(userName=user_name)
    user.bool_logIO = False  # 로그인 변수 True로 변경
    user.save()     # Update후, save() 필수!
    return redirect('not_login')

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
    if not log_now :
        return redirect('not_login')
    return render(request, 'index.html', {'bool_logIO':log_now, 'user_name':userName})

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

    if request.method == 'POST':
        # user = Profile.objects.get(userName=user_name)
        # print(user)
        ticket_name = request.POST['ticketname']
        print(ticket_name)
        ticket_code = request.POST['ticketcode']
        print(ticket_code)
        ticket_deadline = request.POST['Validity']
        print(ticket_deadline)

        # 주차권 생성
        MyTicket.objects.create(
            profile = user,
            ticket_name = ticket_name,
            ticket_code = ticket_code,
            deadline_date = ticket_deadline,
        )
        
        return redirect('myticket', user_name)

    context = {
        'userName' : user.userName,
        'userID' : user.userID,
    }

    return render(request, 'createTicket.html', context)

def cpms_ticket_details(request, user_name, ticket_code):
    try:
        user = Profile.objects.get(userName=user_name)
    except:
        return redirect('not_login')

    # 로그인했는지 확인하는 bool변수
    log_now = user.bool_logIO    
    if not log_now:
        return redirect('not_login')

    tickets = MyTicket.objects.filter(profile=user)
    
    if not tickets:
        # return redirect('myticket', user_name)
        error_message = {
            'userName':user_name,
            'userID':user.userID,
            'tickets':tickets,
            'find_error':(user_name + '님의 주차권을 찾을 수 없습니다.'),
        }
        return render(request, 'createTicket.html', error_message)
    
    try:
        ticket = tickets.get(ticket_code=ticket_code)
    except:
        # return redirect('myticket', user_name)
        error_message = {
            'userName':user_name,
            'userID':user.userID,
            'tickets':tickets,
            'find_error':'해당 주차권을 찾을 수 없습니다.',
        }
        return render(request, 'myTicket.html', error_message)

    context = {
        'userName':user_name,
        'userID':user.userID,
        'ticketName':ticket.ticket_name,
        'ticket_code':ticket_code,
        'createDate':ticket.create_date,
        'deadlineDate':ticket.deadline_date,
    }
    
    return render(request, 'ticketdetails.html', context)