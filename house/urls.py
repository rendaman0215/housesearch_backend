from django.urls import path,include
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, indexfunc, reviewfunc, expensefunc, upreviewfunc, upexpensefunc

urlpatterns = [
    path('', indexfunc, name='index'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('review/<int:pk>', reviewfunc, name='review'),
    path('expense/<int:pk>', expensefunc, name='expense'),
    path('upreview/<int:pk>', upreviewfunc, name='upreview'),
    path('upexpense/<int:pk>', upexpensefunc, name='upexpense'),
]
