from django.db import models
from users.models import User

# Create your models here.
# class Rol(models.Model):
#     type = models.CharField(max_length=12, null=False, blank=False)

#     def __str__(self):
#         return self.type


# class User(models.Model):
#     first_name = models.CharField(max_length=50, null=False, blank=False)
#     last_name = models.CharField(max_length=50, null=False, blank=False)
#     phone = models.CharField(max_length=20, null=True, blank=True)
#     username = models.CharField(max_length=50, unique=True, null=False, blank=False)
#     email = models.CharField(max_length=50, unique=True, null=False, blank=False)
#     password = models.CharField(max_length=20, null=False, blank=False)
#     avatar = models.CharField(max_length=500, null=True, blank=True)
#     rol = models.ForeignKey(Rol, default='public', on_delete=models.SET_DEFAULT)
#     is_active = models.BooleanField(default=True)
#     creation_date = models.DateTimeField('date created')

#     def __str__(self):
#         return self.first_name + ' ' + self.last_name

#     def created_at(self):
#         return self.creation_date
    
#     def state(self):
#         return self.is_active
    
#     def rol_type(self):
#       return self.rol


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.CharField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return self.name


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    resume = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=False, blank=False)
    image = models.CharField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateTimeField('date created', auto_now_add=True)
    categories = models.ManyToManyField(Category, through='Category_Article', through_fields=('article', 'category'))

    
    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(null=False, blank=False)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateTimeField('date created', auto_now_add=True)


class Category_Article(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)

    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')

    # def was_published_recentrly(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)