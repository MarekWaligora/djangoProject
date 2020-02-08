from django.urls import path
from . import views

urlpatterns = [
#musiclibrary
path('',views.index,name="index"),


#mlibrary/artists
    path('artists/',views.ListArtist.as_view(),name="artist-list"),
#mlibrary/borrow-register   dodawanie wypozyczenia
    path('borrow-register/',views.BorrowCreate.as_view(),name="borrow-register"),   
#mlibrary/borrow-list
    path('borrow-list/',views.BorrowsView.as_view(),name="borrow-list") ,

]