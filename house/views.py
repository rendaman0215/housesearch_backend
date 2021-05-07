from .models import MakerCard, Reviews, Expense

from django.utils import timezone
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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
            post.update_date = timezone.now()
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
                tenant = pk,
                create_date = timezone.now(),
                update_date = timezone.now()
            )
            post.save()
            return redirect('review', pk=pk)
        else:
            return render(request, 'postreview.html',{'object':object,'post':"", 'isPosted':False})
    return render(request, 'postreview.html',{'object':object})

@login_required
def postexpensefunc(request, pk):
    object = MakerCard.objects.get(pk=pk)
    user = request.user
    try:
        post = Expense.objects.get(author=user.username, tenant=pk)
        # 更新する場合
        if request.method == 'POST':
            post.cost = request.POST['cost'],
            post.landarea = request.POST['landarea'],
            post.gradecomment = request.POST['gradecomment'],
            post.costupcomment = request.POST['costupcomment'],
            post.costdowncomment = request.POST['costdowncomment'],
            #post.image = request.FILES.get('image'),
            post.update_date = timezone.now()
            post.save()
            print("update root end")
            return redirect('expense', pk=pk)
        else:
            context = {
                'object':object, 
                'post':post,
                'isPosted':True,
            }
            return render(request, 'postexpense.html',context) 
    except Exception as e:
        # 新規作成する場合
        if request.method == 'POST':
            print(e)
            print("create root")
            post = Expense.objects.create(
                author = user.username,
                cost = request.POST['cost'],
                landarea = request.POST['landarea'],
                gradecomment = request.POST['gradecomment'],
                costupcomment = request.POST['costupcomment'],
                costdowncomment = request.POST['costdowncomment'],
                #image = request.FILES.get('image'),
                tenant = pk,
                create_date = timezone.now(),
                update_date = timezone.now()
            )
            post.save()
            print("create root end")
            return redirect('expense', pk=pk)
        else:
            context = {
                'object':object, 
                'post':"",
                'isPosted':True,
            }
            return render(request, 'postexpense.html', context)

@login_required
def deletereviewfunc(request, pk):
    user = request.user
    post = Reviews.objects.get(author=user.username, tenant=pk)
    post.delete()
    return redirect('review', pk=pk)

@login_required
def deleteexpensefunc(request, pk):
    user = request.user
    post = Expense.objects.get(author=user.username, tenant=pk)
    post.delete()
    return redirect('review', pk=pk)