from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create/', views.create, name="create"),
    path('<str:id>/',views.showParticularNote, name="particular_note"),
    path('edit/<int:id>/', views.edit, name="edit_note"),
    path('delete/<int:id>/', views.delete_note, name="delete_note")
]