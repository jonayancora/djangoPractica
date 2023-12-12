from django.urls import path
from . import views
urlpatterns =[
  
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('', views.index),
    path('projects/', views.projects),
    path('tasks/int:id', views.tasks),
]