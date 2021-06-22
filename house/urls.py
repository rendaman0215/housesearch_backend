from . import views

from django.urls import path

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()
router.register(r'v1/makers', views.MakerCardViewSet)
router.register(r'v1/reviews', views.ReviewViewSet)
router.register(r'v1/expense', views.ExpenseViewSet)

urlpatterns = [
    path('v1/isposted/<slug:targetmaker>/', views.isPosted.as_view()),
    path('v1/user/', views.PingViewSet.as_view()),
    path('auth/', obtain_jwt_token),
]
