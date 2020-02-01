from django.contrib import admin
from .models import MusicKind,Artist,Album,Borrower,Borrow

class MusicKindAdmin(admin.ModelAdmin):
     list_display=['mkshortdesc','mklongdesc']
     ordering=['mkshortdesc']

class ArtistAdmin(admin.ModelAdmin):
     list_display=['artname',]
     ordering=['artname']

class BorrowInline(admin.TabularInline):
     model=Borrow
     extra=1
 #model many to many konfiguracja dla admina admin.TabularInline 
# # nazwa zamiast id wstawic metode

class BorrowAdmin(admin.ModelAdmin):
    list_display=['album','borrower','borrow_date','return_date']


class AlbumAdmin(admin.ModelAdmin):
    list_display=['albname','albreleasedate','albmusickind','alblabel']
    inlines=[BorrowInline]


class BorrowerAdmin(admin.ModelAdmin):
     list_display=['brname','brsurname','brmail','brphone']
     ordering=['brsurname']
     inlines=[BorrowInline]

    

# Register your models here.
admin.site.register(MusicKind,MusicKindAdmin)
admin.site.register(Artist,ArtistAdmin)
admin.site.register(Album,AlbumAdmin)
admin.site.register(Borrower,BorrowerAdmin)
admin.site.register(Borrow,BorrowAdmin)







