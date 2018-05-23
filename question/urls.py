from django.urls import path
from . import views

urlpatterns = [
    path('q/', views.QuestionListView.as_view()),   
    path('q/<int:pk>', views.QuestionDetailView.as_view(), name="question_detail"),
    path('q/create/', views.QuestionCreate.as_view()),
    path('q/<int:pk>/update/', views.QuestionUpdate.as_view()),
    path('q/<int:pk>/delete/', views.QuestionDelete.as_view()),  
    path('a/create/<int:q>', views.AnswerCreate.as_view()),
    path('a/<int:q>/<int:pk>/update/', views.AnswerUpdate.as_view()),
    path('a/<int:q>/<int:pk>/delete/', views.AnswerDelete.as_view()),  
]