from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

app_name = 'posts'

router.register('posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),

]