from django.urls import path, include
from rest_framework import routers

from blog.views import UserViewSet, CategoryViewSet, ArticleViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'article', ArticleViewSet, basename='article')

urlpatterns = [
    path('', include(router.urls)),
]