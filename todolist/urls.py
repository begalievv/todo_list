from django.urls import path

from .views import *


urlpatterns = [
    path('', Main.as_view(), name="main_list"),
    path('delete/<int:pk>/', delete_todo, name='delete_todo'),
    path('check/<int:pk>/', check_todo, name='check_todo'),
    path('update/<int:pk>/', UpdateTodo.as_view(), name='update_todo'),
]
