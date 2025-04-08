from django.urls import path
from . import views

urlpatterns = [
    path('', views.donate_view, name='donate'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),

]
