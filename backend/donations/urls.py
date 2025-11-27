from django.urls import path
from . import views

# Thse are the URLs for the different webpages
urlpatterns = [
    path('', views.donate_view, name='donate'),                # Homepage: donation form
    path('thank-you/', views.thank_you_view, name='thank_you'),# After form submission
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),  # See all donations
]
