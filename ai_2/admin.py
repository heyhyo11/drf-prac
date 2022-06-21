from django.contrib import admin
from blog.models import Article
from blog.models import Category
from user.models import User, UserProfile

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
  list_display = ["id", "name"]

admin.site.register(UserProfile)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article)
admin.site.register(User)


