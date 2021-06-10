from .views import MakerCardViewSet, ReviewViewSet, ExpenseViewSet
from django.conf.urls import url
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'v1/makers', MakerCardViewSet)
router.register(r'v1/reviews', ReviewViewSet)
router.register(r'v1/expense', ExpenseViewSet)

urlpatterns = []
