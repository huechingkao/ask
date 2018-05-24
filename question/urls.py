from django.urls import path
from . import views

urlpatterns = [
    path('q/', views.QuestionListView.as_view()),   
    path('q/<int:pk>/', views.QuestionDetailView.as_view(), name="question_detail"),
    path('q/create/', views.QuestionCreate.as_view()),
    path('q/<int:pk>/update/', views.QuestionUpdate.as_view()),
    path('q/<int:pk>/delete/', views.QuestionDelete.as_view()),  
    path('q/<int:q>/a/create/', views.AnswerCreate.as_view()),
    path('q/<int:q>/a/<int:pk>/update/', views.AnswerUpdate.as_view()),
    path('q/<int:q>/a/<int:pk>/delete/', views.AnswerDelete.as_view()),  
]