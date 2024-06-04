from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.FinchListView.as_view(), name='index'),
    path('finches/<int:pk>/', views.FinchDetailView.as_view(), name='detail'),
    path('finches/add/', views.FinchCreateView.as_view(), name='finch_add'),
    path('finches/<int:pk>/edit/', views.FinchUpdateView.as_view(), name='finch_edit'),
    path('finches/<int:pk>/delete/', views.FinchDeleteView.as_view(), name='finch_delete'),
    path('finches/<int:pk>/add_feeding/', views.add_feeding, name='add_feeding'),
]
