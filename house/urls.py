from .views import MakerCardViewSet, ReviewViewSet, ExpenseViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'makers', MakerCardViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'expense', ExpenseViewSet)

urlpatterns = []
