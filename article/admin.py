from django.contrib import admin

from article.models import Article

# admin 페이지에 보이기 위해 작성
admin.site.register(Article)
