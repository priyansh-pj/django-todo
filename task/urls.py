from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="index"),
    path('category/view/', viewCategory, name='viewCategory'),
    path('task/view/<str:id>/', viewTask, name='viewTask'),
    path('task/update/<str:id>/', updateTask, name='updateTask'),
    path('category/edit/<str:id>/',updateCategory, name='updateCategory'),
    path('api/category/', apiCategory),
    path('api/task/', apiTask)

]
