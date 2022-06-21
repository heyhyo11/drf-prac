from django.urls import path
from blog.views import ArticleView

urlpatterns = [
    path('', ArticleView.as_view()),
]