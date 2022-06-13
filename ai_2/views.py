from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

## hw_01 ============================================================================================
def message(request):
  message = {'message': 'success!'}
  return Response(message)



## hw_02 ============================================================================================
class StudentView(APIView):
  permission_classes = [permissions.AllowAny] # 누구나
  # permission_classes = [permissions.IsAdminUser] # Admin만
  # permission_classes = [permissions.IsAuthenticated] # 로그인 사용자만
  
  def get(self, request):
    return Response({'message': 'GET 방식입니다!'})
    
  def post(self, request):
    return Response({'message': 'POST 방식입니다!'})
  
  def put(self, request):
    return Response({'message': 'PUT 방식입니다!'})
  
  def delete(self, request):
    return Response({'message': 'Delete 방식입니다!'})