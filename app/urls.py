from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ana', views.teste_ana),
    path('usuario/', views.users),
    path('usuario/<int:id>', views.user_detail, name='user_detail'),
]