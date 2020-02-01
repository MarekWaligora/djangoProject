from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views.generic import ListView,CreateView
from .models import Artist,Borrow,Borrower,Album
from django.db.models import F,ExpressionWrapper,DateField
from datetime import datetime, timedelta, timezone, tzinfo
# from django.views.generic import 
# Create your views here.

# /mlibrary
def index(request):
    artists=Artist.objects.all().order_by('artname')
    context = {
        'Name':'Artist' ,
        'artist': artists,
    }
    return render (request,"mlibrary/index.html",context)


class ListArtist(ListView):
    model = Artist
    template_name='mlibrary/artist-list.html'
    extra_context={
        'title':'Lista Wykonawców',
        # 'nazwa':model.artname,
        # 'raise_date':model.art_est_date,

    }
    # to jest wykorzystywane potem w HTMLu a odwolania do nazw pol tabeli 
    context_object_name='artist_list'

class BorrowCreate(CreateView):    
    model=Borrow
    # fields=['album','borrower','borrow_date','return_date','first_monit_date','second_monit_date',]
    fields = ['album','borrower','borrow_date','return_date',]
    template_name ='mlibrary/borrow-register.html'
    success_message ='Wypozyczenie  "%(album)s" zarejestrowano z sukcesem.'
    #PRZEKIEROWANIE MUSI ISC NA WIDOK A NIE NA FORMULARZ
    success_url = reverse_lazy('borrow-list')
    extra_context = {
        'title': "Zarejestruj Wypozyczenie",
    }
    # Po zapisaniu przekierowac go do listy wypozyczen


class BorrowsView(ListView):
    queryset = Borrow.objects.annotate(
        exp_return_date=ExpressionWrapper(
            F('borrow_date')+timedelta(days=25),
            output_field=DateField(),
        )
    )
    
    # model=Borrow 
    template_name='mlibrary/borrow-list.html'
    extra_context={
        'title': "Borrow's List"
    }
    context_object_name='borrow_list'
    
    