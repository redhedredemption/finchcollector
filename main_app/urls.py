from django.urls import path
from . import views
	
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # Route for finch index
  path('finches/', views.finches_index, name='index'),
  # Route for finch detail
  path('finches/<int:finch_id>/', views.finch_detail, name='detail'),
]