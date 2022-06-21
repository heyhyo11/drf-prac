from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from rest_framework.views import APIView
from rest_framework import status
from datetime import timedelta
from django.utils import timezone

from blog.models import Article
from .serializers import ArticleSerializer
# from user.serializers import UserSerializer

class RegistedMoreThanThreeDaysUser(BasePermission):
   
  # 가입일 기준 3일 이상 지난 사용자만 접근 가능
  message = '가입 후 3일 이상 지난 사용자만 사용하실 수 있습니다.'

  def has_permission(self, request, view):
    # GET 방식은 모두 접근 가능
    if request.method == 'GET':
      return True

    # POST 방식은 가입일 확인해야 함
    return bool(request.user and request.user.join_date < (timezone.now() - timedelta(days=3)))


class ArticleView(APIView):

  serializer_class = ArticleSerializer
  
  # 로그인한 사용자의 정보, 게시글을 보여준다.
  def get(self, request):
    user = request.user
    # queryset = list(Article.objects.filter(writer=self.request.user).values())
    articles = ArticleSerializer(instance=Article.objects.filter(user=user), many=True)
    # return Response(ArticleSerializer(user).data, status=status.HTTP_200_OK)
    return Response(articles.data, status=status.HTTP_200_OK)
    
  # <글 제목, 카테고리, 글 내용>을 입력받아 게시글을 작성해준다.
  def post(self, request):
    
    user = request.user
    title = request.data.get('title', '')
    category = eval(request.data['category']) # [1, 2] ([1, 2])
    content = request.data.get('content', '')
    
    print(category)
    print(type(category))
    
    new_article = Article.objects.create(
      user=request.user,
      title=title,
      content=content,
    )
    
    new_article.category.add(*category)
    
    return Response({'message': '게시글 작성완료!', 'title': title, 'content': content, 'category': category})