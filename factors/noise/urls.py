from django.urls import path
from . import views

urlpatterns = [
    path('', views.noise_home, name='noise'),
    path('create_noise', views.noise_create, name='noise_create'),
    path('<int:pk>', views.NoiseDetailView.as_view(), name='noise-detail'),
    path('<int:pk>/alert', views.nature_of_the_noise, name='calculations'),
    path('<int:pk>/update', views.NoiseUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.NoiseDeleteView.as_view(), name='delete'),

]