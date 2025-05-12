from django.urls import path
from . import views

urlpatterns = [

path('getData/',views.getData),
path('add/',views.addItem),
path('delete/<str:pk>',views.deleteItem),

] 