from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from house.urls import router as house_router
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("house.urls")),
    path('auth/', obtain_jwt_token),
    url('api/', include(house_router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
