from django.urls import path

from kapela import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bands/<int:pk>/', views.BandDetailView.as_view(), name='band_detail'),
    path('member/<int:pk>/', views.MemberDetailView.as_view(), name='member_detail'),
]
