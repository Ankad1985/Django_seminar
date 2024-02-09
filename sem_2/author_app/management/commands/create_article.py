from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from author_app.models import AuthorsModel, ArticleModel
from random import choice

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
            authors = AuthorsModel.objects.all()
            for i in range(0,5):
                article = ArticleModel(
                        author=choice(authors),
                        title=f'Статья № {i}',
                        text=lorem_ipsum.paragraphs(4),
                        category=f'Категория {i}',
                  )

                article.save()
            print('Создание авторов выполнено')