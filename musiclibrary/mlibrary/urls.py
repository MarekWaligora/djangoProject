from django.urls import path
from . import views

urlpatterns = [
#mlibrary/artists
    path('artists/',views.ListArtist.as_view(),name="artist-list"),
#mlibrary/borrow-register
    path('borrow-register/',views.BorrowCreate.as_view(),name="borrow-register"),   
#mlibrary/borrow-list
    path('borrow-list/',views.BorrowsView.as_view(),name="borrow-list")     
]