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
            post.costcomment = request.POST['costcomment']
            post.costrate = request.POST['costrate']
            post.designcomment = request.POST['designcomment']
            post.designrate = request.POST['designrate']
            post.layoutcomment = request.POST['layoutcomment']
            post.layoutrate = request.POST['layoutrate']
            post.speccomment = request.POST['speccomment']
            post.specrate = request.POST['specrate']
            post.attachcomment = request.POST['attachcomment']
            post.attachrate = request.POST['attachrate']
            post.guaranteecomment = request.POST['guaranteecomment']
            post.guaranteerate = request.POST['guaranteerate']
            post.salescomment = request.POST['salescomment']
            post.salesrate = request.POST['salesrate']
            post.save()
            return redirect('review', pk=pk)
        else:
            return render(request, 'postreview.html',{'object':object, 'post':post, 'isPosted':True}) 
    except:
        if request.method == 'POST':
            post = Reviews.objects.create(
                author = user.username,
                costcomment = request.POST['costcomment'],
                costrate = request.POST['costrate'],
                designcomment = request.POST['designcomment'],
                designrate = request.POST['designrate'],
                layoutcomment = request.POST['layoutcomment'],
                layoutrate = request.POST['layoutrate'],
                speccomment = request.POST['speccomment'],
                specrate = request.POST['specrate'],
                attachcomment = request.POST['attachcomment'],
                attachrate = request.POST['attachrate'],
                guaranteecomment = request.POST['guaranteecomment'],
                guaranteerate = request.POST['guaranteerate'],
                salescomment = request.POST['salescomment'],
                salesrate = request.POST['salesrate'],
                avgrate = float(
                    int(request.POST['costrate'])
                     + int(request.POST['designrate'])
                     + int(request.POST['layoutrate'])
                     + int(request.POST['specrate'])
                     + int(request.POST['attachrate'])
                     + int(request.POST['guaranteerate'])
                     + int(request.POST['salesrate']) )/ 7,
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