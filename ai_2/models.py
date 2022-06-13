from django.db import models

# Create your models here.

class Student(models.Model):
  name = models.CharField('학생 이름', max_length=10, unique=True)
  subject = models.ManyToManyField('Teacher') # 수강과목
  
class Teacher(models.Model):
  name = models.CharField('선생님 이름', max_length=10, unique=True)
  subject = models.CharField('담당과목', max_length=20)
