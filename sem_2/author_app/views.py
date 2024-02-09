'''
Доработаем задачи из прошлого семинара по созданию
моделей автора, статьи и комментария.
Создайте шаблон для вывода всех статей автора в виде
списка заголовков.
○ Если статья опубликована, заголовок должен быть
ссылкой на статью.
○ Если не опубликована, без ссылки.
Не забываем про код представления с запросом к базе
данных и маршруты.

'''

from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from .models import ArticleModel

def all_article(request: HttpRequest, author_id):
    articles = ArticleModel.objects.filter(author_id=author_id)
    return render(request, 'author_app/blog.html', {'articles':articles})

'''
Доработаем задачу 4.
Создай шаблон для вывода подробной информации о
статье.
Внесите изменения в views.py - создайте представление и в
urls.py - добавьте маршрут.

*Увеличивайте счётчик просмотра статьи на единицу при
каждом просмотре

'''

def article_page(request: HttpRequest, article_id):
    article = get_object_or_404(ArticleModel, pk=article_id)
    article.views_count += 1
    article.save()
    return render(request, 'author_app/article.html', {'article':article})