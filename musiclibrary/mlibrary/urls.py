from django.urls import path
from . import views

urlpatterns=[
#mlibary/artist
path('artists/',views.ListArtist.as_view(),name="artist-list")
]