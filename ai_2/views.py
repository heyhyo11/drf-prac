from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def message(request):
  message = {'message': 'success!'}
  return JsonResponse(message)