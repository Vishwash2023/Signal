from django.urls import path
from .views import UserModelView, UserModelView1

urlpatterns = [
    path('get/',UserModelView.as_view()),
    path('get/<int:pk>',UserModelView1.as_view()),
]