from django.contrib import admin
from mlibrary import MusicKind,Artist,Album,Borrower,Borrow

class MusicKind(admin.ModelAdmin):
    list_display=['mkshortdesc','mklongdesc']
    ordering='mkshortdesc'

class Artist(admin.ModelAdmin):
    list_display=['artname','art_est_date']
    ordering='artname'

class BorrowInline(admin.TabularInline):
    model=Borrow
    extra=1
#model many to many konfiguracja dla admina admin.TabularInline 
# nazwa zamiast id wstawic metode

class Album(admin.ModelAdmin):
    list_display=['albname','albreleasedate','albmusickind','alblabel']
    inlines=[BorrowInline]


class Borrower(admin.ModelAdmin):
    list_display=['brname','brsurname','brmail','brphone']
    ordering=['brsurname']
    inlines=BorrowInline

    

# Register your models here.

admin.site.Register(MusicKind,MusicKindAdmin)
admin.site.Register(Artist,ArtistdAdmin)
admin.site.Register(Album,AlbumAdmin)
admin.site.Register(Borrower,BorrowerAdmin)
admin.site.Register(Borrow,BorrowAdmin)







