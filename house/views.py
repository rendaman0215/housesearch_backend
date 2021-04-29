from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import MakerCard, Reviews, Expense
from django.contrib.auth.decorators import login_required

def indexfunc(request):
    return render(request, 'index.html')

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
            return redirect('list')
        else:  
            return redirect('login')
    return render(request, 'login.html')

def listfunc(request):
    object_list = MakerCard.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

def logoutfunc(request):
    logout(request)
    return redirect('index')

def detailfunc(request, pk):
    object = MakerCard.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':object})

def reviewfunc(request, pk):
    object = MakerCard.objects.get(pk=pk)
    review_list = object_list = Reviews.objects.filter(tenant=pk)
    return render(request, 'review.html', {'object':object, 'review_list':review_list})

def expensefunc(request, pk):
    object = MakerCard.objects.get(pk=pk)
    expense_list = object_list = Expense.objects.filter(tenant=pk)
    return render(request, 'expense.html', {'object':object, 'expense_list':expense_list})

@login_required
def upreviewfunc(request, pk):
    object = MakerCard.objects.get(pk=pk)
    if request.method == 'POST':
        author = request.User.username
        comment = request.POST['comment']
        return render(request, 'upreview.html', {'object':object})
    else:
        return render(request, 'upreview.html', {'object':object})
    return render(request, 'upreview.html', {'object':object})

@login_required
def upexpensefunc(request, pk):
    object = MakerCard.objects.get(pk=pk)
    return render(request, 'upexpense.html', {'object':object})