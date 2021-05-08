from django.urls import path,include
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, indexfunc, reviewfunc, expensefunc, postreviewfunc, postexpensefunc, deletereviewfunc, deleteexpensefunc, MakerCardViewSet, ReviewViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('makers', MakerCardViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('', listfunc, name='index'),
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
    path('deleteexpense/<int:pk>', deleteexpensefunc, name='deleteexpense'),
]
