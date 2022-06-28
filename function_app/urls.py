from django.urls import path
from function_app import views

urlpatterns = [
    path('form/', views.student_list, name='student-list'),
    path('form/<int:pk>/', views.student_detail, name='student-detail'),
]
