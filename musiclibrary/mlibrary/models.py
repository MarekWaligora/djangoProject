from django.db import models

# Create your models here.
# !!!!! Zweryfikowac modele w realcji wiele do wielu !!!!!!!!

class MusicKind(models.Model):
    mkshortdesc=models.CharField(max_length=2,verbose_name="Music Kinds short",unique=True)
    mklongdesc=models.CharField(max_length=20,verbose_name="Music Kind Long descr")
    
    class Meta:
        pass
        # consider which field and how should be presented
    
    
    def __str__(self):
        return self.mklongdesc



class Artist(models.Model):
   
    # music kind in separate table witjh relation to to band and albums

    artname=models.CharField(max_length=200,verbose_name="Artist Name",unique=True)
    artkind=models.ForeignKey(MusicKind,on_delete=models.SET_NULL,null=True,verbose_name="Kind of Music")
    art_est_date=models.DateTimeField(verbose_name="Raise Date")

   
    class Meta:
        pass
        # consider which field and how should be presented

    def __str__(self):
        return self.artname



 

class Album(models.Model):
    #foreign key artist PK
    albartist=models.ForeignKey(Artist,on_delete=models.CASCADE)
    albname=models.CharField(max_length=100,verbose_name="Album Name")
    albreleasedate=models.DateField(verbose_name="Relase Date")
    albmusickind=models.ForeignKey(MusicKind,on_delete=models.SET_NULL,null=True,verbose_name="Kind of Music")
    alblabel=models.CharField(max_length=100,verbose_name="Labelled by")
    # albtype=models.CharField(max_length=50,verbose_name="carrier type")
    ALBCARIER=[
        ('CD' 'Plyta CD'),
        ('DVD' 'Plyta DVD'),
        ('BRAY' 'Plyta Blue Ray'),
        ('OCD','Original CD')
    ]
    ALBSTATUS=[('H','On Hand'),('B','Borrowed')]
    
    class Meta:
        pass
        # consider which field and how should be presented

    def __str__(self):
        return f"{self.albartist.artname}, {self.albname}" 

  

class Borrower(models.Model):
    brname=models.CharField(max_length=100,verbose_name="Name")
    brsurname=models.CharField(max_length=100,verbose_name="Surname")
    brmail=models.CharField(max_length=40,verbose_name="Mail")
    brphone=models.CharField(max_length=20,verbose_name="Phone")
    bralbums=models.ManyToManyField(
        Album,
        through='Borrow',
    )
    class Meta:
        pass
        # consider which field and how should be presented

    def __str__(self):
        return f"{self.brname},{self.brsurname}"




class Borrow(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE,verbose_name="Album Id")
    borrower=models.ForeignKey(Borrower,on_delete=models.CASCADE,verbose_name="Borrower ID")
    borrow_date=models.DateField(verbose_name="Borrow Date")
    exp_return_date=models.DateField(verbose_name="Expect Return Date")
    #???? Wyrzucic to pole z modelu i obliczac go dunamicznie jako borrow_date +parametr
    return_date=models.DateField(verbose_name="Return Date",null=True)
    first_monit_date=models.DateField(verbose_name="1st Monit Date", null=True)
    second_monit_date=models.DateField(verbose_name="2nd Monit Date",null=True)

    class Meta:
        pass
        # consider which field and how should be presented

    def __str__(self):
        return f"{self.borrower.brname} {self.borrower.brsurname}" 
         






