from django.urls import path
from . import views

app_name = 'author_app'

urlpatterns = [
    path('blog/<int:author_id>/', views.all_article, name='all_article'),
    path('article/<int:article_id>/', views.article_page, name='article_page'),
]
