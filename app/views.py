from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import auth_login
from app.models import Level, Exam, Point, Leaderboard
import random
import fractions
from django.views.decorators.csrf import csrf_exempt

def index (request) :
    
    # check if user is loged in or not 
    if request.user.is_authenticated :
        return redirect('profile')

    return render(request,'index.html')





# Leaderboard
def leaderboard (request) :
    leaders = Leaderboard.objects.all().order_by('-points')

    rank = 1
    for i in leaders :
        i.rank = rank
        i.save()
        rank = rank + 1

    data = []
    for leader in leaders :
        data.append({
            'user':leader.user.username,
            'points':leader.points,
            'rank':leader.rank,
        })

    return JsonResponse(data=data,safe=False)

# User profile
@login_required
def profile (request) :
    
    ex = Exam.objects.filter(user=request.user).order_by('-date')

    l = Leaderboard.objects.get(user=request.user)
    
    context = {
        'exams':ex,
        'points':l.points,
        'rank':l.rank,
    }




    return render(request,'profile.html',context)




# Exam
@login_required
@csrf_exempt
def exam (request,examType) :

    q = []
    a = []
    
    context = {}

    user = request.user
    exam_type = get_object_or_404(Level,name=examType)

    # get the points of exam
    points = Point.objects.filter(level=exam_type).all().order_by('?')[0:10]
    
    for point in points :
        q.append(point.question)
        a.append(point.answer)

    context['q'] = '@'.join(q)
    context['id'] = '@'.join(map(str,a))


    # work on client data
    if request.method == 'POST' :
        questions = request.POST.getlist('q[]')
        user_answers = request.POST.getlist('a[]')
        points = 0

        for i in range(len(questions)):
            q = Point.objects.filter(question=questions[i]).first()

            if q.answer == user_answers[i] :
                points = points + 1
        
        
        # create exam history
        Exam.objects.create(
            user=user,
            total_points=f"{points} / {len(questions)}",
        )

        return HttpResponse('ok')


    return render(request,'exam.html',context)


# Congratulation page
@login_required
def congrats (request) :
    
    # get the last exam by date
    res = Exam.objects.filter(user=request.user).order_by('-date')[0]
    
    
    context = {
        'result':res.total_points,
    }
    return render(request,'congrats.html',context)







# Authentications

def login(request) :

    context = {}
    # POST method
    if request.method == "POST" :
        msgs = []
        email = request.POST['email']
        password = request.POST['password']

        # get user of the email
        try :
            user = User.objects.get(email=email)

            auth = authenticate(username=user.username,password=password)
            if auth != None :
                auth_login(request,user=user)
                return redirect('profile')

            else :
                # Password is wrong
                context['msg'] = 'كلمة السر غير صحيحة'
            
        except :
            # The Email isn't on the system

            context['msg'] = 'البريد الالكروني غير موجود بالنظام'


    return render(request,'login.html',context)

def signup(request) :
    
    # POST method 
    if request.method == "POST" :
        
        # get data from the client
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Create the user
        user = User.objects.create(
            username=username,
            email=email,
            password=password
        )

        # Enter the user on the system
        auth_login(request,user=user)
        
        # redirect him to the profile page
        return redirect('profile')


    return render(request,'signup.html')
