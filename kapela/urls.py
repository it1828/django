from django.urls import path

from kapela import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bands/<int:pk>/', views.BandDetailView.as_view(), name='band_detail'),
    path('member/<int:pk>/', views.MemberDetailView.as_view(), name='member_detail'),
    path('band/create/', views.BandCreateView.as_view(), name='band_create'),
    path('band/<int:pk>/update/', views.BandUpdateView.as_view(), name='band-update'),
    path('band/<int:pk>/delete/', views.BandDeleteView.as_view(), name='band-delete'),

    path('member/create/', views.MemberCreateView.as_view(), name='member-create'),
    path('member/<int:pk>/update/', views.MemberUpdateView.as_view(), name='member-update'),
    path('member/<int:pk>/delete/', views.MemberDeleteView.as_view(), name='member-delete'),

    path('person/create/', views.PersonCreateView.as_view(), name='person-create'),

]
