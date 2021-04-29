from django.urls import path,include
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, indexfunc, reviewfunc, expensefunc, postreviewfunc, postexpensefunc, deletereviewfunc

urlpatterns = [
    path('', indexfunc, name='index'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('review/<int:pk>', reviewfunc, name='review'),
    path('expense/<int:pk>', expensefunc, name='expense'),
    path('postreview/<int:pk>', postreviewfunc, name='postreview'),
    path('postexpense/<int:pk>', postexpensefunc, name='postexpense'),
    path('deletereview/<int:pk>', deletereviewfunc, name='deletereview'),
]
