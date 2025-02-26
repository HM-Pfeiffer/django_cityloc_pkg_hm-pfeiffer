from django.urls import path
from citylocations import views

urlpatterns = [
    path('loc-nyc', views.loc_nyc, name='loc-nyc'),
]