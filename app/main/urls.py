from django.contrib import admin
from django.urls import path, include
from drf import views as drf_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', drf_views.User_Viewset)
router.register('groups', drf_views.Group_Viewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
