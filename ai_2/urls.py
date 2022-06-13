from django.urls import path
from . import views
from ai_2.views import StudentView

urlpatterns = [
    path('hw01/', views.message),
    path('hw02/', StudentView.as_view())
]
