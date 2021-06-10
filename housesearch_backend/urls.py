from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from house.urls import router as house_router

urlpatterns = [
    path('admin/', admin.site.urls),
    url('api/', include(house_router.urls),),
    url('api/', include('house.urls'),),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
