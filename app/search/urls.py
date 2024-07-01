from django.urls import path
from search.views import SearchArticles, SearchCategories, SearchUsers


urlpatterns = [
    path('user/<str:query>/', SearchUsers.as_view(), name='elasticsearch_user'),
    path('category/<str:query>/', SearchCategories.as_view(), name='elasticsearch_categories'),
    path('article/<str:query>/', SearchArticles.as_view(), name='elasticsearch_articles'),
]
