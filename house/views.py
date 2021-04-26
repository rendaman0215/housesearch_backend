from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import MakerCard

def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.get(username=username)
            return render(request, 'signup.html', {'error':'このユーザは登録されています'})
        except:
            user = User.objects.create_user(username, '', password)
            return render(request, 'signup.html', {'some':100})
    return render(request, 'signup.html', {'some':100})

def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('signup')
        else:  
            return redirect('login')
    return render(request, 'login.html')

def listfunc(request):
    object_list = MakerCard.objects.all()
    return render(request, 'list.html', {'object_list':object_list})