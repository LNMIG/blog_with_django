from .models import Article, Comment, Category, Category_Article
from django.contrib import admin

# Register your models here.
# admin.site.register(User)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Category_Article)
# admin.site.register(Rol)
