from . import views

from django.conf.urls import url
from django.urls import path

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()
router.register(r'v1/makers', views.MakerCardViewSet)
router.register(r'v1/reviews', views.ReviewViewSet)
router.register(r'v1/expense', views.ExpenseViewSet)

urlpatterns = [
    url('v1/isposted/', views.isPosted.as_view()),
    url('v1/user/', views.PingViewSet.as_view()),
    path('auth/', obtain_jwt_token),
]
