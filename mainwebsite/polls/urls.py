from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('candidates/', views.show_candidates, name='candidates'),
]
