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
            return render(request, 'signup.html', {'error':'このユーザは既に登録されています'})
        except:
            user = User.objects.create_user(username, '', password)
            return render(request, 'index.html', {})
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
    review_list = Reviews.objects.all()
    return render(request, 'list.html', {'object_list':object_list, 'review_list':review_list})

def logoutfunc(request):
    logout(request)
    return redirect('list')

def detailfunc(request, pk):
    object = MakerCard.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':object})

def reviewfunc(request, pk):
    object = MakerCard.objects.get(pk=pk)
    review_list = Reviews.objects.filter(tenant=pk)
    user = request.user
    return render(request, 'review.html', {'object':object, 'review_list':review_list, 'user':user})

def expensefunc(request, pk):
    object = MakerCard.objects.get(pk=pk)
    expense_list = Expense.objects.filter(tenant=pk)
    return render(request, 'expense.html', {'object':object, 'expense_list':expense_list})

@login_required
def postreviewfunc(request, pk):
    object = MakerCard.objects.get(pk=pk)
    user = request.user
    try:
        post = Reviews.objects.get(author=user.username, tenant=pk)
        if request.method == 'POST':
            post.comment = request.POST['comment']
            post.rate = request.POST['rate']
            post.save()
            return redirect('review', pk=pk)
        else:
            return render(request, 'postreview.html',{'object':object, 'post':post.comment, 'isPosted':True}) 
    except:
        if request.method == 'POST':
            post = Reviews.objects.create(
                author = user.username,
                comment = request.POST['comment'],
                rate = request.POST['rate'],
                tenant = pk
            )
            post.save()
            return redirect('review', pk=pk)
        else:
            return render(request, 'postreview.html',{'object':object,'post':"", 'isPosted':False})
    return render(request, 'postreview.html',{'object':object})

@login_required
def postexpensefunc(request, pk):
    object = MakerCard.objects.get(pk=pk)
    return render(request, 'upexpense.html', {'object':object})

@login_required
def deletereviewfunc(request, pk):
    user = request.user
    post = Reviews.objects.get(author=user.username, tenant=pk)
    post.delete()
    return redirect('review', pk=pk)