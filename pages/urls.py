from django.urls import path

from .views import HomePageView, AboutPageView
from snacks.views import SnacksListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('snacks/',SnacksListView.as_view(), name='snacks'),
]
