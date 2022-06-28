from tkinter import CASCADE
from django.db import models
from user.models import User


# Create your models here.
class Category(models.Model):
  name = models.CharField('카테고리 이름', max_length=20)
  detail = models.TextField('카테고리 설명')
  
  def __str__(self):
    return self.name


class Article(models.Model):
  user = models.ForeignKey(User, verbose_name='작성자', on_delete=models.CASCADE, db_column="user")
  title = models.CharField('제목', max_length=30)
  category = models.ManyToManyField("Category", verbose_name='카테고리')
  content = models.TextField('내용') 
  
  def __str__(self):
    return self.title
  
  
class Comment(models.Model):
  article = models.ForeignKey(Article, verbose_name='게시글', on_delete=models.CASCADE, db_column='article')
  writer = models.ForeignKey(User, verbose_name='작성자', on_delete=models.CASCADE, db_column='writer')
  created = models.DateField('작성시간', auto_now_add=True)
  content = models.TextField('내용')
  
  def __str__(self):
    return self.content
  