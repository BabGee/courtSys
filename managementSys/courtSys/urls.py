from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='court-home'),
    path('solved', views.solved, name='solved'),
    path('pending', views.pending, name='pending'),
    path('case/<int:pk>/', views.case_detail, name='case_detail'),
    path('search/', views.search_results, name='search-results'),
]